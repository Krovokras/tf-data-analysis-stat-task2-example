
import pandas as pd
import numpy as np
from scipy.stats import norm

chatid = 1134491798

def solution(p: float, x: np.array) -> tuple:
    a, b = 0.068, 6
    n = len(x)
    sumx = np.sum(x)
    sumxsq = np.sum(x  x)

    
    b_hat = (n  (sumx - n * 0.068) - sumxsq + 0.068 * n * (n + 1)) / (n * (n - 1) / 2)
    
    
    seb = np.sqrt((b - a)  2 / 12 / n / (n + 1)  (2  n + 1))
    
    
    z = norm.ppf(1 - (1 - p) / 2)
    ci = (bhat - z * seb, bhat + z * seb)
    
    return ci
