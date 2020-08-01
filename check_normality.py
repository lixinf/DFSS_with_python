
"""
This code is used to identify the normality of data.
Code will return false if Data is empty or less than 2 number
Otherwise, code will return p_value for normality. p>0.05 means data is normal distribution
- For small sample-numbers (<300), you should use the "normaltest"
- the Kolmogorov-Smirnov(Kolmogorov-Smirnov) test should only be used for large sample numbers (>300)
"""

import numpy as np
import scipy.stats as stats

def check_normality(data):
    n = len(data)
    if n<=1:
        return False

    elif n<=300:
        _, p_value = stats.normaltest(data, nan_policy='omit')

    else:
        _, p_value = stats.kstest((data-np.mean(data))/np.std(data,ddof=1),'norm')

    return p_value

if __name__ =='main':
    pass