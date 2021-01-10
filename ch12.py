# this is a python script for ch12 experiment
#
import numpy as np

raw_data_1 = [0, 4, 0, 1, 0]
raw_data_2 = [6, 8, 5, 4, 2]
raw_data_3 = [6, 5, 9, 4, 6]

#raw_data_1 = [5, 1, 2, 3, 0, 1, 2, 2]
#raw_data_2 = [2, 6, 2, 3, 5, 3, 0, 3]
#raw_data_3 = [7, 3, 2, 4, 5, 2, 4 ,5]

data_1 = np.array(raw_data_1)
data_2 = np.array(raw_data_2)
data_3 = np.array(raw_data_3)

# compute intra-group stats
t_1 = data_1.sum()
m_1 = data_1.mean()
ss_1 = ((data_1 - m_1) * (data_1 - m_1)).sum()

t_2 = data_2.sum()
m_2 = data_2.mean()
ss_2 = ((data_2 - m_2) * (data_2 - m_2)).sum()

t_3 = data_3.sum()
m_3 = data_3.mean()
ss_3 = ((data_3 - m_3) * (data_3 - m_3)).sum()

# compute N, G, Sigma(∑) x_square
N = len(data_1) + len(data_2) + len(data_3)
G = t_1 + t_2 + t_3
sigma_x_square = (data_1 * data_1).sum() + \
                 (data_2 * data_2).sum() + \
                 (data_3 * data_3).sum()

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

print("--------------------------------------")
print("Source\t\t\t SS\t MS\t\t")
print("--------------------------------------")
print("Between Treatment\t", ss_between_check, "\t", df_between, "\t F =", np.round(F, 2))
print("Within Treatment\t", ss_within, "\t", df_within, "\t")
print("Total\t\t\t",ss_total, "\t", df_total, "\t")
print("--------------------------------------")


