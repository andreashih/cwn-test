#%%
import re
import json

with open('ASBC_unigrams.json', encoding='utf-8') as f:
    word_freq = json.load(f)

cjk = re.compile(r'[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD]+')
sorted_wordfreq = sorted(((k, v) for k, v in word_freq.items() if cjk.match(k)), key=lambda x: x[1], reverse=True)

# %% 取詞頻最高的 8000 個詞彙
sorted_wordfreq[:8000]
# %%
# Extract words only
def Extract(lst): 
    return [item[0] for item in lst] 
#%%
# Initialize cwn
from CwnGraph import CwnBase
cwn = CwnBase()
# %%
# Find asbc8k not in cwn
words = Extract(sorted_wordfreq[:8000])
asbc_in_cwn = []
for word in words:
    if len(cwn.find_lemma(f"^{word}$")) == 0:
        asbc_in_cwn.append(word)

 # %%
# Write .csv
import pandas as pd
df = pd.DataFrame(asbc_in_cwn, columns=["colummn"])
df.to_csv('asbc8k_not_in_cwn.csv', index=False)
# %%
# Import huayu8000
import pandas as pd
df = pd.read_csv("huayu8000_NV.csv")
# %%
# Extracts words only
words2 = df.詞彙.to_list()
# %%
# Find huayu8000 not in cwn
huayu_in_cwn = []
for word in words2:
    word = re.sub('[/].+|[(].+[)]', '', word)
    if len(cwn.find_lemma(word)) == 0:
        huayu_in_cwn.append(word)
# %%
df3 = pd.DataFrame(huayu_in_cwn, columns=["colummn"])
df3.to_csv('huayu8k_not_in_cwn.csv', index=False)
# %%
