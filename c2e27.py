#Dakota Long
#Average polysemy for n: 1.28
#Average polysemy for v: 2.19
#Average polysemy for a: 1.41
#Average polysemy for r: 1.25

import nltk
from nltk.corpus import wordnet as wn

pos_list = [wn.NOUN, wn.VERB, wn.ADJ, wn.ADV]       #list of wn parts of speech

def calc_syns(pos):
    for pos in pos_list:                            #iterates over all parts of speech
        num_of_syns = 0.0
        temp = 0.0                                  #temp counts the current number of meanings
        words = set()
        for syns in wn.all_synsets(pos):            #iterates over each synset
            for lemma in syns.lemmas():             #iterates over the lemma
                x = lemma.name()
                if x not in words:                  #prevents duplicates by using set
                    words.add(lemma.name())
                    temp = len(wn.synsets(x, pos))
                    num_of_syns = num_of_syns + temp
        avg = num_of_syns / len(words)
        avg_string = "{0:.2f}".format(avg)
        print ('Average polysemy for ' + str(pos) + ': ' + avg_string)

calc_syns(pos_list)