#
# examples for how to use SfBS_utils
# reference: SfBS Page 60, Demo 2.1
from SfBS_utils import *

data_list = [14, 8, 27, 16, 10, 22, 9, 13, 16, 12,
             10, 9, 15, 17, 6, 14, 11, 18, 14, 11]

range_list = [[25, 29],
              [20, 24],
              [15, 19],
              [10, 14],
              [5 ,  9],]

f_list, cf, c_perc = sfbs_freq_dist(data_list, range_list)

print("--------------------------------------")
print("X\t\t f \t cf \t c% \t")
print("--------------------------------------")
for i in range(0, len(f_list)):
    print("range",i+1, "\t", f_list[i], "\t", \
                cf[i], "\t", c_perc[i], "\t")
print("--------------------------------------")
