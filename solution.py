import pandas as pd 
import numpy as np 
from scipy.stats import ttest_rel 
 
 
chat_id = 968976840 # Ваш chat ID, не меняйте название переменной 
 
def solution(x: np.array, y: np.array) -> bool: # Одна или две выборке на входе, заполняется исходя из условия 
    t_statistic, p_value = ttest_rel(x, y) 
    alpha = 0.02 
    return p_value < alpha
