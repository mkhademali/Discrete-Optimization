import numpy as np
D = np.array(['V', 'D', 'S'])
#           (['0', '1', '2'])
#           (['1', '2', '0'])
#           (['0', '2', '1'])


C = np.array(['A', 'B', 'C'])
DensityOrders = np.argsort(D)[::-1]
print(C[DensityOrders])
# print(C[~DensityOrders])
print(1/np.inf)
