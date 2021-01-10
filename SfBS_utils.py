import math
import numpy as np # only employed when scipy is used
import scipy.stats as st

#
# functions for frequency distribution
# applied range: Chapter 2
def sfbs_freq_dist(data_list, range_list):
    f_list = list()
    for range_item in range_list:
        lower = range_item[0]
        upper = range_item[1]
        temp_f = 0
        for data_item in data_list:    
            if ((data_item >= lower) and (data_item <= upper)):
                temp_f = temp_f + 1
        f_list.append(temp_f)

    cf_list = list()
    temp_cf = 0
    for i in range(0, len(f_list)):
        temp_cf = sfbs_sum(f_list[i:])
        cf_list.append(temp_cf)

    c_perc = list()
    for i in range(0, len(cf_list)):
        temp_perc = round(cf_list[i] / cf_list[0], 2)
        c_perc.append(temp_perc)

    return f_list, cf_list, c_perc

#
# functions for central tendency
# applied range: All
def sfbs_pow(num_, expo_):
    if (expo_ == 0):
        return 1
    produit = num_
    for i in range(0, expo_-1):
        produit = produit * num_
    return produit

def sfbs_sum(data_list, expo=1):        
    temp_sum = 0
    for item in data_list:
        temp_sum = temp_sum + sfbs_pow(item, expo_=expo)
    return temp_sum

def sfbs_mean(data_list):
    temp_sum = sfbs_sum(data_list)
    temp_mean = temp_sum / len(data_list)
    return temp_mean

def sfbs_median(data_list):
    data_list.sort()
    if ((len(data_list) % 2) == 1):
        return data_list[int(len(data_list)/2)]
    else:
        return (data_list[int(len(data_list)/2) - 1] + \
                data_list[int(len(data_list)/2)]) / 2

def sfbs_mode(data_list):
    unique_elems = list(set(data_list))
    unique_elems_count = list()
    max_count = 0
    for elem in unique_elems:
        current_elem_count = 0
        for item in data_list:
            if (item == elem):
                current_elem_count = current_elem_count + 1
        if (current_elem_count > max_count):
            max_count = current_elem_count
        unique_elems_count.append(current_elem_count)
    mode_list = list()
    for i in range(0, len(unique_elems)):
        if (unique_elems_count[i] == max_count):
            mode_list.append(unique_elems[i])
    return mode_list

def sfbs_sum_square_deviation(data_list):
    temp_sum = sfbs_sum(data_list)
    temp_square_sum = sfbs_sum(data_list, 2)
    sum_squared_deviation = temp_square_sum - \
                            temp_sum * temp_sum / len(data_list)
    return sum_squared_deviation

def sfbs_sample_variance(data_list):
    sum_squared_deviation = sfbs_sum_square_deviation(data_list)
    sample_variance = sum_squared_deviation / (len(data_list) - 1)
    return sample_variance

def sfbs_sample_std(data_list):
    sample_variance = sfbs_sample_variance(data_list)
    sample_std = math.sqrt(sample_variance)
    return sample_std

def sfbs_square_deviation_mean(data_list, mode='poplulation'):
    temp_mean = sfbs_mean(data_list)
    temp_ss = 0
    for item in data_list:
        temp_ss = temp_ss + (item - temp_mean) * (item - temp_mean)
    if (mode == 'poplulation'):
        return temp_ss / len(data_list)
    else:
        return temp_ss / (len(data_list) - 1) 

def sfbs_std(data_list):
    temp_ss = sfbs_square_deviation_mean(data_list)
    temp_std = math.sqrt(temp_ss)
    return temp_std

def sfbs_z_score_single(x, mu, sigma):
    z_score = (x - mu) / sigma
    return z_score

def sfbs_z_score_list(data_list):
    z_score = list()
    mu = sfbs_mean(data_list)
    sigma = sfbs_std(data_list)
    for item in data_list:
        z_score.append((item - mu) / sigma)
    return z_score

#
# functions for fundamental hypothesis testing
# applied range: Chapter 9, 10, 11
# Chapter 8 only involve z-score example, not implemented here
def sfbs_t_for_single(scores, mu_0):
    M = sfbs_mean(scores)
    ss = sfbs_square_deviation_mean(scores)
    s_square = ss / (len(scores) - 1)
    s_M = math.sqrt(s_square / len(scores))
    t_score = (M - mu_0) / s_M
    return t_score

def sfbs_t_for_independent(group_1, group_2, mu_d=0):
    M_1 = sfbs_mean(group_1)
    ss_1 = sfbs_sum_square_deviation(group_1)
    M_2 = sfbs_mean(group_2)
    ss_2 = sfbs_sum_square_deviation(group_2)
    
    df1 = len(group_1) - 1
    df2 = len(group_2) - 1
    #df = len(group_1) - 1 + len(group_2) - 1
    pool_var = (ss_1 + ss_2) / (df1 + df2)
    s_diff = math.sqrt(pool_var/len(group_1) + pool_var/len(group_2))
    t_score = (M_1 - M_2 + mu_d) / round(s_diff,2)
    return t_score

def sfbs_t_for_related(X_before, X_after, mu_d=0):
    temp_D = list()
    for i in range(0, len(X_before)):
        temp_D.append(abs(X_before[i] - X_after[i]))
    Md = sfbs_mean(temp_D)
    ss = sfbs_sum_square_deviation(temp_D)
    df = len(X_before) - 1
    s_square = ss / df # variance
    s_Md = math.sqrt(s_square / len(X_before))
    t_score = (Md - mu_d) / s_Md
    return t_score

#
# functions for ANOVA
# applied range: Chapter 12, 13, 14
def sfbs_anova_square_deviation(data_list):
    temp_mean = sfbs_mean(data_list)
    temp_ss = 0
    for item in data_list:
        temp_ss = temp_ss + \
                  (item - temp_mean) * \
                  (item - temp_mean)
    return temp_ss

def sfbs_anova_T_list(data_list):
    T_list = list()
    for data_item in data_list:
        temp_T = sfbs_sum(data_item)
        T_list.append(temp_T)
    return T_list

def sfbs_anova_M_list(data_list):
    M_list = list()
    for data_item in data_list:
        temp_M = sfbs_mean(data_item)
        M_list.append(temp_M)    
    return M_list

def sfbs_anova_ss_list(data_list):
    ss_list = list()
    for data_item in data_list:
        temp_ss = sfbs_anova_square_deviation(data_item)
        ss_list.append(temp_ss)
    return ss_list

def sfbs_anova_N(data_list):
    temp_N = 0
    for data_item in data_list:
        temp_N = temp_N + len(data_item)
    return temp_N

def sfbs_anova_G(data_list):
    T_list = sfbs_anova_T_list(data_list)
    temp_G = 0
    for T_item in T_list:
        temp_G = temp_G + T_item
    return temp_G

def sfbs_anova_P(data_list):
    P = list()
    for i in range(0, len(data_list[0])):
        temp_p_total = 0
        for data_item in data_list:
            temp_p_total = temp_p_total + data_item[i]
        P.append(temp_p_total)
    return P

def sfbs_anova_square_sum(data_list):
    temp_square_sum = 0
    for data_item in data_list:
        for item in data_item:
            temp_square_sum = temp_square_sum + item * item
    return temp_square_sum

def sfbs_anova_ss_total(data_list):
    N = sfbs_anova_N(data_list)
    G = sfbs_anova_G(data_list)
    sigma_x_square = sfbs_anova_square_sum(data_list)
    ss_total = sigma_x_square - (G * G) / N
    return ss_total

def sfbs_anova_ss_within(data_list):
    ss_list = sfbs_anova_ss_list(data_list)
    ss_within = 0
    for item in ss_list:
        ss_within = ss_within + item
    return ss_within

def sfbs_anova_ss_between(data_list):
    t_list = sfbs_anova_T_list(data_list)
    G = sfbs_anova_G(data_list)
    N = sfbs_anova_N(data_list)
    ss_between = 0
    for i in range(0, len(data_list)):
        ss_between = ss_between + \
                     t_list[i] * t_list[i] / len(data_list[i])
    ss_between = ss_between - (G * G) / N
    return ss_between

def sfbs_anova_ss_between_subjects(data_list):
    P = sfbs_anova_P(data_list)
    t_list = sfbs_anova_T_list(data_list)
    G = sfbs_anova_G(data_list)
    N = sfbs_anova_N(data_list)
    ss_between_subjects = 0
    for item in P:
        ss_between_subjects = ss_between_subjects + \
                              item * item / len(data_list)
    ss_between_subjects = ss_between_subjects - (G * G) / N
    return ss_between_subjects

def sfbs_anova_ss_between_row(data_list, num_row=2):
    t_list = sfbs_anova_T_list(data_list)
    t_row_list = list()
    n_row_list = list()
    num_col = int(len(data_list) / num_row)
    for i in range(0, num_row):
        temp_t_row = 0
        temp_n_row = 0
        for j in range(0, num_col):
            temp_t_row = temp_t_row + t_list[i * num_col + j]
            temp_n_row = temp_n_row + len(data_list[i * num_col + j])
        t_row_list.append(temp_t_row)
        n_row_list.append(temp_n_row)

    G = sfbs_anova_G(data_list)
    N = sfbs_anova_N(data_list)
    ss_between_row = 0
    for i in range (0, len(t_row_list)):
        ss_between_row = ss_between_row + \
                         t_row_list[i] * t_row_list[i] / \
                         n_row_list[i]
    ss_between_row = ss_between_row - G * G / N
    return ss_between_row

def sfbs_anova_ss_between_col(data_list, num_col=2):
    t_list = sfbs_anova_T_list(data_list)
    t_col_list = list()
    n_col_list = list()
    num_row = int(len(data_list) / num_col)
    for i in range(0, num_col):
        temp_t_col = 0
        temp_n_col = 0
        for j in range(0, num_row):
            temp_t_col = temp_t_col + t_list[i + j * num_col]
            temp_n_col = temp_n_col + len(data_list[i + j * num_col])
        t_col_list.append(temp_t_col)
        n_col_list.append(temp_n_col)

    G = sfbs_anova_G(data_list)
    N = sfbs_anova_N(data_list)
    ss_between_col = 0
    for i in range(0, len(t_col_list)):
        ss_between_col = ss_between_col + \
                         t_col_list[i] * t_col_list[i] / \
                         n_col_list[i] 
    ss_between_col = ss_between_col - G * G / N
    return ss_between_col

def sfbs_anova_ss_error(data_list):
    ss_within = sfbs_anova_ss_within(data_list)
    ss_between_subjects = sfbs_anova_ss_between_subjects(data_list)
    ss_error = ss_within - ss_between_subjects
    return ss_error

def sfbs_anova_ss_interaction(data_list, num_row=2, num_col=2):
    ss_between = sfbs_anova_ss_between(data_list)
    ss_a = sfbs_anova_ss_between_row(data_list, num_row)
    ss_b = sfbs_anova_ss_between_col(data_list, num_col)
    ss_axb = ss_between - ss_a - ss_b
    return ss_axb

def sfbs_anova_df_total(data_list):
    df_total = 0
    for i in range(0, len(data_list)):
        df_total = df_total + len(data_list[i])
    df_total = df_total - 1
    return df_total

def sfbs_anova_df_between(data_list):
    df_between = len(data_list) - 1
    return df_between

def sfbs_anova_df_within(data_list):
    df_within = 0
    for i in range(0, len(data_list)):
        df_within = df_within + len(data_list[i]) - 1
    return df_within

def sfbs_anova_df_between_subjects(data_list):
    df_between_subjects = len(data_list[0]) - 1
    return df_between_subjects

def sfbs_anova_df_error(data_list):
    df_within = sfbs_anova_df_within(data_list)
    df_between_subjects = sfbs_anova_df_between_subjects(data_list)
    df_error = df_within - df_between_subjects
    return df_error

def sfbs_anova_df_interaction(data_list, num_row=2, num_col=2):
    df_between = sfbs_anova_df_between(data_list)
    df_axb = df_between - (num_row - 1) - (num_col - 1)
    return df_axb

#
# functions for Correlation
# applied range: Chapter 15, 16
def sfbs_correlation_ss(X):
    ss_x = 0
    x_sum = sfbs_sum(X)
    for item in X:
        ss_x = ss_x + item * item
    ss_x = ss_x - x_sum * x_sum / len(X)
    return ss_x

def sfbs_correlation_sp(X, Y):
    sp = 0
    x_sum = sfbs_sum(X)
    y_sum = sfbs_sum(Y)
    for i in range(0, len(X)):
        sp = sp + X[i] * Y[i]
    sp = sp - x_sum * y_sum / len(X)
    return sp

def sfbs_correlation_pearson(X, Y):
    sp = sfbs_correlation_sp(X, Y)
    ss_x = sfbs_correlation_ss(X)
    ss_y = sfbs_correlation_ss(Y)
    rs = sp / math.sqrt(ss_x * ss_y)
    return rs

def sfbs_correlation_spearman(X, Y):
    # the formula is for rank data ONLY
    d_square = 0
    n = len(X)
    for i in range(0, n):
        d_square = d_square + (X[i] - y[i]) * (X[i] - y[i])
    rs = 1 - 6 * d_square / (n * (n * n -1))
    return rs

def sfbs_correlation_slope(X, Y):
    sp = sfbs_correlation_sp(X, Y)
    ss_x = sfbs_correlation_ss(X)
    slope = sp / ss_x
    return slope

def sfbs_correlation_intercept(X, Y):
    slope = sfbs_correlation_slope(X, Y)
    M_x = sfbs_mean(X)
    M_y = sfbs_mean(Y)
    intercept = M_y - slope * M_x
    return intercept

def sfbs_regression_significance(X, Y):
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
    return F_score
#
# functions for Chi-square
# applied range: Chapter 17
def sfbs_chi_square(freq_list):
    freq_sum = sfbs_sum(freq_list)
    f_e = l / len(freq_list)
    chi_square = 0
    for item in freq_list:
        f_o = item / freq_sum
        chi_square = chi_square + (f_o - f_e) * (f_o - f_e) / f_e
    return chi_square
