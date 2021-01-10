#
# examples for how to use SfBS_utils
# reference: SfBS Page 406, Demo 12.1
from SfBS_utils import *

#data_1 = [0, 4, 0, 1, 0]
#data_2 = [6, 8, 5, 4, 2]
#data_3 = [6, 5, 9, 4, 6]

data_1 = [5, 1, 2, 3, 0, 1, 2, 2]
data_2 = [2, 6, 2, 3, 5, 3, 0, 3]
data_3 = [7, 3, 2, 4, 5, 2, 4 ,5]

t_1 = sfbs_anova_sum(data_1)
m_1 = sfbs_anova_mean(data_1)
ss_1 = sfbs_anova_square_deviation(data_1)

t_2 = sfbs_anova_sum(data_2)
m_2 = sfbs_anova_mean(data_2)
ss_2 = sfbs_anova_square_deviation(data_2)

t_3 = sfbs_anova_sum(data_3)
m_3 = sfbs_anova_mean(data_3)
ss_3 = sfbs_anova_square_deviation(data_3)

# compute N, G, Sigma(∑) x_square
N = len(data_1) + len(data_2) + len(data_3)
G = t_1 + t_2 + t_3
sigma_x_square = 0
for data_item in [data_1, data_2, data_3]:
    for item in data_item:
        sigma_x_square = sigma_x_square + item * item

# compute degree of freedom
df_within = (len(data_1) - 1) + \
            (len(data_2) - 1) + \
            (len(data_3) - 1)
df_between = 3 - 1
df_total = len(data_1) + len(data_2) + len(data_3) - 1

# compute various ss
ss_total = sigma_x_square - (G * G) / N
ss_within = ss_1 + ss_2 + ss_3
ss_between = ss_total - ss_within
ss_between_check = (t_1 * t_1) / len(data_1) + \
                   (t_2 * t_2) / len(data_2) + \
                   (t_3 * t_3) / len(data_3) - \
                   (G * G) / N
print("ss_between from subtraction: ", ss_between)
print("ss_between from calculation: ", ss_between_check)

MS_between = ss_between / df_between
MS_within = ss_within / df_within
    
F = MS_between / MS_within
effect_size = ss_between / ss_total

print("--------------------------------------")
print("Source\t\t\t SS\t MS\t\t")
print("--------------------------------------")
print("Between Treatment\t", ss_between_check, "\t", df_between, "\t F =", round(F, 2))
print("Within Treatment\t", ss_within, "\t", df_within, "\t")
print("Total\t\t\t",ss_total, "\t", df_total, "\t")
print("--------------------------------------")
print("Effect Size: ", round(effect_size, 2))