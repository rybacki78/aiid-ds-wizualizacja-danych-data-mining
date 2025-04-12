# tablice numpy sa wydajniejsze :)

import numpy as np
import time

start_time = time.time()
my_arr = np.arange(10000000)
my_list = list(range(10000000))
start_time = time.time()
my_arr2 = my_arr * 5
print("--- %s seconds ---" % (time.time() - start_time))
start_time = time.time()
my_list2 = [x * 5 for x in my_list]
print("--- %s seconds ---" % (time.time() - start_time))