import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 1134491798 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
a, b = 0.068, 6
    loc = (a + b) / 2
    scale = (b - a) / np.sqrt(12)
    alpha = 1 - p
    return loc - scale * uniform.ppf(1 - alpha / 2), \
           loc - scale * uniform.ppf(alpha / 2)
