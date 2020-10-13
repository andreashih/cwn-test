#%%
import re
import json

with open('ASBC_unigrams.json', encoding='utf-8') as f:
    word_freq = json.load(f)

cjk = re.compile(r'[\u2E80-\u2FD5\u3190-\u319f\u3400-\u4DBF\u4E00-\u9FCC\uF900-\uFAAD]+')
sorted_wordfreq = sorted(((k, v) for k, v in word_freq.items() if cjk.match(k)), key=lambda x: x[1], reverse=True)

# %% 取詞頻最高的 8000 個詞彙
sorted_wordfreq[:8000]