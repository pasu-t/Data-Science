import numpy as np
l1 = [1,2,3,4,5]
a = np.array([6,7,8,9])

for e in l1:
    print(e)
for e in a:
    print(e)

l1 = l1 +[10,11]
print(l1)

l2 = []
for e in l1:
    l2.append(e+e)

print(l2)
print(a+a)
print(2*a)
print(a*a)
print(2*l1)
print(np.sqrt(a))
print(np.log(a))
print(np.exp(a))
print(a[1])

