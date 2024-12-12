import numpy as np
import time


# List operation

lst = [i for i in range(1_000_000)]
start = time.time()
sum_lst = [x + 1 for x in lst]
end = time.time()
print("List Time:", end - start)


# Array operation
arr = np.array(lst)
start = time.time()
sum_arr = arr + 1
end = time.time()
print("Array Time:", end - start)