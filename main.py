import time

import normal_code
import cython_code

t1 = time.time()
cython_code.fun(10000000)
t2 = time.time()
print(f"cython code time consumed {t2-t1}")
t1 = time.time()
normal_code.fun(10000000)
t2 = time.time()
print(f"cython code time consumed {t2-t1}")
