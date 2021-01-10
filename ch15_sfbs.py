#
# examples for how to use SfBS_utils
# reference: SfBS Page 523, Demo 15.1
from SfBS_utils import *

X = [0, 2, 8, 6, 4]
Y = [4, 1, 10, 9, 6]
r = sfbs_correlation_pearson(X, Y)
print("r: ", round(r,2))