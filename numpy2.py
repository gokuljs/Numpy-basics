import numpy as np
a=np.random.randint(1,10,6)
print(a)
a=a.reshape(3,2)
print(a)
print(a.sum())# gives the sum of all the elements inthe array
print(a.sum(axis=1))
# it adds up each row in the element
print(a.sum(axis=0)) # it adds up wach column in the array

