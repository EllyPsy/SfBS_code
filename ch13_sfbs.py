#
# examples for how to use SfBS_utils
# reference: SfBS Page 439, Demo 13.1
from SfBS_utils import *

data_1 = [0, 1, 0, 4, 0]
data_2 = [0, 3, 1, 5 ,1]
data_3 = [6, 5, 5, 9, 5]

data_1 = [39,38,44,40,34]
data_2 = [40,39,46,42,33]
data_3 = [49,44,50,46,41]
data_4 = [52,55,60,56,52]

data_list = [data_1, data_2, data_3, data_4]
"""
t_list = list()
m_list = list()
ss_list = list()

t_list = sfbs_anova_T_list(data_list)
m_list = sfbs_anova_M_list(data_list)
ss_list = sfbs_anova_ss_list(data_list)

# Personal total
P = sfbs_anova_P(data_list)

# compute N, G, Sigma(∑) x_square
N = sfbs_anova_N(data_list)
G = sfbs_anova_G(t_list)
sigma_x_square = sfbs_anova_square_sum(data_list)
"""

# stage 1
ss_total = sfbs_anova_ss_total(data_list)
ss_within = sfbs_anova_ss_within(data_list)
ss_between = sfbs_anova_ss_between(data_list)

df_within = sfbs_anova_df_within(data_list)
df_between = sfbs_anova_df_between(data_list)
df_total = sfbs_anova_df_total(data_list)

# stage 2
ss_between_subjects = sfbs_anova_ss_between_subjects(data_list)
ss_error = sfbs_anova_ss_error(data_list)

print("ss_between_subjects: ", ss_between_subjects, ss_error)
df_between_subjects = sfbs_anova_df_between_subjects(data_list)
df_error = sfbs_anova_df_error(data_list)

MS_between = ss_between / df_between
MS_error = ss_error / df_error

F = MS_between /MS_error
effect_size = ss_between / (ss_between + ss_error)

print("--------------------------------------")
print("Source\t\t\t SS\t df\t MS\t\t")
print("--------------------------------------")
print("Between Treatment\t",    ss_between,         "\t", df_between, "\t", MS_between, "\t F =", round(F, 2))
print("Within Treatment\t",     ss_within,          "\t", df_within,  "\t", "\t")
print("  Between Subjects\t",   ss_between_subjects,"\t", df_between_subjects, "\t", )
print("  Error\t\t\t",          ss_error,           "\t", df_error,   "\t", round(MS_error,2), "\t")
print("Total\t\t\t",            ss_total,           "\t", df_total,   "\t", "\t")
print("--------------------------------------")
print("Effect Size: ", round(effect_size, 2))
