#%%
import re
from googletrans import Translator
from nltk.corpus import wordnet as wn
from CwnGraph import CwnBase
cwn = CwnBase()

def search_word(word):
    cwn_senses = cwn.find_lemma(word)[0].senses
    
    word1 = re.sub('\^|\$', '', word) # remove the anchors

    translator = Translator() # Initialize the translator
    tran_result = translator.translate(word1).text # translate CH to EN
    synset = wn.synsets(tran_result)

    num = []
    df = []
    result = []
    
    for i in range(0, len(synset)):
        df.append(synset[i].definition()) # find the definition of the word
        num.append('{}-{}'.format(str(wn.synset(synset[i].name()).offset()).zfill(8), wn.synset(synset[i].name()).pos())) 
        # Find the id num of the synset. It has to be 8-digit with a pos tag.
    
    return cwn_senses, { id_: def_ for id_, def_ in zip(num, df) }

# %%
search_word("^朋友$")
# %%
