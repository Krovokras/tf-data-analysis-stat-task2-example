import pandas as pd
import numpy as np
from scipy.stats import norm

chat_id = 1134491798

def solution(p: float, x: np.array) -> tuple:

alpha = 1 - p
loc = x.mean()
scale = np.sqrt(np.var(x))/np.sqrt(len(x))

left_quantile = loc - scale * norm.ppf(1 - alpha / 2)
right_quantile = loc - scale * norm.ppf(alpha / 2)
return left_quantile, right_quantile
