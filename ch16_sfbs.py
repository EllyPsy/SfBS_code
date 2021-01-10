#
# examples for how to use SfBS_utils
# reference: SfBS Page 555, Demo 16.1
from SfBS_utils import *

X = [0, 2, 8, 6, 4]
Y = [4, 1, 10, 9, 6]

"""
r = sfbs_correlation_pearson(X, Y)

b = sfbs_correlation_slope(X, Y)
a = sfbs_correlation_intercept(X, Y)

SS_y = sfbs_correlation_ss(Y)

SS_regression = r * r * SS_y
SS_residual = (1 - r * r) * SS_y

df_regression = 1
df_residual = len(X) - 2

MS_regression = SS_regression / df_regression
MS_residual = SS_residual / df_residual

F_score = MS_regression / MS_residual
"""
F_score = sfbs_regression_significance(X, Y)
print("F-score: ", round(F_score, 2))