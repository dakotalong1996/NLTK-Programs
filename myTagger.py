#Dakota Long
#myTagger.py
#03/26/2018

import nltk
import time
from random import shuffle
from nltk.corpus import brown

start_time = time.time()
brown_tagged_sents = [sentence for sentence in nltk.corpus.brown.tagged_sents()]
fold_n = 10                         #Number of folds to create.  Can be changed by changing this variable.
ids = brown.fileids()
shuffle(ids)                        #Shuffles the file ids and tagged sentences.
shuffle(brown_tagged_sents)
amount_to_train = len(ids) / fold_n #Get the amount of file ids to train with at a time.
amount_to_train_sents = len(brown_tagged_sents)/fold_n  #Gets amount of sents to train with at a time.

#get_sents_by_id() uses the shuffled file ids and creates 10 folds.  Each fold is then passed to the tagger.
def get_sents_by_id():
    print('FILE IDS\nTest Fold\t\tResult')
    n2 = amount_to_train
    n1 = 0
    for x in range(10):
        test_ids = [i for i in ids[n1:n2]]
        train_ids = []
        for id in ids:
            if id not in test_ids:
                train_ids.append(id)
        test_sents = brown.tagged_sents(fileids=test_ids)
        train_sents = brown.tagged_sents(fileids=train_ids)
        n1 += amount_to_train       #n1 and n2 are incremented to access the next fold.
        n2 += amount_to_train
        train_tagger(train_sents, test_sents, x)

#get_sents_by_sents() uses the shuffled tagged sentences and creates 10 folds.  Each fold is then passed to the tagger.
def get_sents_by_sents():
    n2 = amount_to_train_sents
    n1 = 0
    print('TAGGED SENTENCES\nTest Fold\t\tResult')
    for x in range(10):
        test_sents = [i for i in brown_tagged_sents[n1:n2]]
        train_sents = []
        for sent in brown_tagged_sents:
            if sent not in test_sents:
                train_sents.append(sent)
        n1 += amount_to_train_sents     #n1 and n2 are incremented to access the next fold.
        n2 += amount_to_train_sents
        train_tagger(train_sents, test_sents, x)

#train_tagger(train_sents, test_sents, fold) trains the tagger using the training sentences and tests it against the
#test sentences. fold is an integer that tells the tagger which fold it is testing on.
def train_tagger(train_sents, test_sents, fold):
    t0 = nltk.DefaultTagger('NN')
    t1 = nltk.UnigramTagger(train_sents, backoff=t0)
    t2 = nltk.BigramTagger(train_sents, backoff=t1)
    per = (t2.evaluate(test_sents)) * 100
    print (str(fold) + "\t\t\t\t" + str(round(per, 1)) + "%")

get_sents_by_id()
get_sents_by_sents()
print("--- %s seconds ---" % (time.time() - start_time))