#%%
from CwnGraph import CwnBase
def search_cwn(word_ch):
    cwn = CwnBase() # initializa the cwn data as an object
    lemmas = cwn.find_lemma(word_ch)
    synonym = lemmas[0].senses[0].synonym
    #for i in range(0, len(word_ch)):
        