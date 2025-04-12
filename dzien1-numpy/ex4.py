import numpy as np

a = np.arange(10,51,10)

# 1
print(a[2])
print(a[1:4])

print("-" * 30)

# 2
print(a[np.array([0,2,4])])
print(a[::2])

print("-" * 30)

# 3
b = np.arange(1,10)
b.shape = (3,3)
print(b)
print (b[1,])
print(b[0,],b[:,1:3])

print("-" * 30)

# 4
