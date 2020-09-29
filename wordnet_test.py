#%%
import nltk
from nltk.corpus import wordnet   #Import wordnet from the NLTK
syn = list()
ant = list()
for synset in wordnet.synsets("friend"):
   for lemma in synset.lemmas():
      syn.append(lemma.name())    #add the synonyms
      if lemma.antonyms():    #When antonyms are available, add them into the list
        ant.append(lemma.antonyms()[0].name())
print('Synonyms: ' + str(syn))
#print('Antonyms: ' + str(ant))
# %%
synonyms = []
antonyms = []

for syn in wordnet.synsets("friend"):
   for l in syn.lemmas():
      print("l:", l)
      synonyms.append(l.name())
      if l.antonyms():
         antonyms.append(l.antonyms()[0].name())
# %%
w1 = wordnet.synset("friend.n.01")