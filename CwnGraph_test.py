# %%
from pprint import pprint
from CwnGraph import CwnBase
CwnBase.install_cwn("cwn_graph.pyobj")
# %%
from CwnGraph import CwnBase
cwn = CwnBase()
# %%
lemmas = cwn.find_lemma("^朋友$")
lemmas
# %%
senses = lemmas[0].senses
senses
# %%
friend = senses[0]
friend.relations
# %%
friend.synonym
