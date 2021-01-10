#
# examples for how to use SfBS_utils
# reference: SfBS Page 154, Demo 5.1
from SfBS_utils import *

mu = 60
sigma = 12
X = 75

z_score = sfbs_z_score_single(X, mu, sigma)
print("z_score: ", z_score)