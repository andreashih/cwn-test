# %%
from CwnGraph import CwnBase
cwn = CwnBase()

# %%
lemmas = cwn.find_lemma("^朋友$")
senses = lemmas[0].senses

# %%
import re

sense_id_ = re.search(r"CwnSense", str(tuple(map(str, senses)))).group(0)
sense_id_


# %%
