#
# examples for how to use SfBS_utils
# reference: SfBS Page 30, Demo 1.1
from SfBS_utils import *

data = [7, 3, 9, 5, 4]

# compute sigma x
sigma_x = sfbs_sum(data)
print(sigma_x)

# compute (sigma x)'s square
square_sigma_x = sigma_x * sigma_x
print(square_sigma_x)

# compute sigma (x's square)
data_square = list()
for item in data:
    data_square.append(item * item)
sigma_x2 = sfbs_sum(data_square)
print(sigma_x2)

#compute sigma (x + 5)
data_add_5 = list()
for item in data:
    data_add_5.append(item + 5)
sigma_x_add_5 = sfbs_sum(data_add_5)
print(sigma_x_add_5)

data_sub_2 = list()
for item in data:
    data_sub_2.append(item - 2)
sigma_x_sub_2 = sfbs_sum(data_sub_2)
print(sigma_x_sub_2)
