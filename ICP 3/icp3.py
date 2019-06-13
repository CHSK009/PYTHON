import numpy as np
k=np.random.randint(1,20, size=15)
l= k==k.max()
print(k)
k[l]=0
print(k)