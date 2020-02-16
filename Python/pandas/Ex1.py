import numpy as np

a = np.array([1,2,4,6,8,10])
b = a.reshape(2,3)
print(b)
c = np.array([1,2.0,3.14,44])
print(a.dtype)
print(b.dtype)
print(c.dtype)

d = np.arange(10)
print(d)

e = np.eye(3)
print(e)

f = np.diag([1,2,3,4])
print(f)

g = np.empty((4,4,4), dtype=int)
print('matrix g:\n',g)