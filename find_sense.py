#%%
from pprint import pprint
from CwnGraph import CwnBase
cwn = CwnBase()
import re
#%%
cwn.find_lemma("^朋友$")[0].senses[0]
# %%
all_lemma = cwn.find_lemma(".+")
#%%

# %%
all_senses = []
short = []
for lemma in all_lemma[1:500]:
    all_senses.append = lemma.senses
    for sense in all_senses:
        if re.match("簡省",sense):
            short.append(sense)
# %%
