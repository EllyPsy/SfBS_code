#
# examples for how to use SfBS_utils
# reference: SfBS Page 358, Demo 11.1
from SfBS_utils import *

X_before = [15,11,10,11,14,10,11]
X_after = [15,13,18,12,16,10,19]

t_score = sfbs_t_for_related(X_before, X_after)
print("t_score", round(t_score,2))