#
# examples for how to use SfBS_utils
# reference: SfBS Page 128, Demo 4.1
from SfBS_utils import *

data_list = [10, 7, 6, 10, 6, 15]

SS = sfbs_sum_square_deviation(data_list)
print("SS: ", SS)
print(sfbs_square_deviation_mean(data_list))

s_square = sfbs_sample_variance(data_list)
print("s2: ", s_square)

s = sfbs_sample_std(data_list)
print("s: ", round(s, 2))
print(sfbs_std(data_list)) 