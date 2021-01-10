#
# examples for how to use SfBS_utils
# reference: SfBS Page 328, Demo 10.1
from SfBS_utils import *

group_1 = [4,4,3,2,5,1,1,4]
group_2 = [3,7,8,5,4,7,6,8]

t_score = sfbs_t_for_independent(group_1, group_2)
print("t_score: ", round(t_score,2))