#
# examples for how to use SfBS_utils
# reference: SfBS Page 476, Demo 14.1
from SfBS_utils import *


# ------ table structure ------ #
#
#                 Factor B
#          ---------------------
#          | data_11 | data_12 |   T_row
# Factor A |---------|---------|
#          | data_21 | data_22 |   T_row
#          ---------------------
#             T_col     T_col
#

num_row = 2
num_col = 2

data_11 = [11, 8, 9,  10, 7]
data_12 = [4,  4, 8,  5,  4]
data_21 = [10, 7, 10, 6,  7]
data_22 = [10, 6, 10, 10, 9]

data_list = [data_11, data_12, data_21, data_22]


# stage 1
ss_total = sfbs_anova_ss_total(data_list)
ss_within = sfbs_anova_ss_within(data_list)
ss_between = sfbs_anova_ss_between(data_list)

df_total = sfbs_anova_df_total(data_list)
df_within = sfbs_anova_df_within(data_list)
df_between = sfbs_anova_df_between(data_list)

# stage 2
ss_a = sfbs_anova_ss_between_row(data_list)
df_a = num_row - 1
ss_b = sfbs_anova_ss_between_col(data_list)
df_b = num_col - 1

ss_axb = sfbs_anova_ss_interaction(data_list)
df_axb = sfbs_anova_df_interaction(data_list)

MS_within = ss_within / df_within
MS_a = ss_a / df_a
MS_b = ss_b / df_b
MS_axb = ss_axb / df_axb

F_a = MS_a / MS_within
F_b = MS_b / MS_within
F_axb = MS_axb / MS_within

print(F_a, F_b, round(F_axb,2))