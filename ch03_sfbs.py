#
# examples for how to use SfBS_utils
# reference: SfBS Page 96, Demo 3.1
from SfBS_utils import *

data_list = [2, 5, 5, 6, 8, 9, 11, 11, 11, 14]

sample_mean = sfbs_mean(data_list)
print("sample mean: ", sample_mean)

sample_median = sfbs_median(data_list)
print("sample median: ", sample_median)

sample_mode = sfbs_mode(data_list)
print("sample mode: ", sample_mode)