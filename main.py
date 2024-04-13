# TypeError: type numpy.ndarray doesn't define __round__ method

import numpy as np

arr = np.array([1.3, 2.6, 3.4, 4.7, 5.9])

rounded_arr = np.round(arr)

# 👇️ [1. 3. 3. 5. 6.]
print(rounded_arr)