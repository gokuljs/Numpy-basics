import numpy as np
import random
a=np.array([2,3,4]) # print an array
print(a)
a=np.arange(1,12,5) # prints the number betwwen 1 to12 in diffrence of 5
print(a)
a=np.linspace(1,12,6)
print(a)
print(a.reshape(3,2)) # prints like 3 rows 2 columns
print(a.reshape(2,3)) # prints like 2 rows 3column
print(a.size) # tells total no of elements in the array independent of shape
print(a.dtype) # it prints the datatype
print(a.itemsize)# it tell  hw much each element takes up in the memory
b=np.array([(1.2,2,3,4),(2.3,3,4,4,)]) # creating multi dimensional array
print(b)
print(a<4) # it comapres all the elements in the array check weather it is lesser than array
print(a*20)# way to nultiply each element in the array
print(a.reshape(3,2))
a=np.zeros((7,7))
print(a) # this like u want to create an empty array
a=np.ones((2,3))
print(a) # printing an array with all ones
a=np.array([2,3,4],dtype=np.int16) # this is like creating an array and which datatype is required
print(a)
print(a.size)
c= np.random.random((2,3)) # creates an matrix of 2 rows and three columns with random numbers
# it gives valus from o to one

c=np.random.randint(0,10,5) # it prints random values

print(c)
print(c.min())
print(c.max())# prints both min and max value
print(c.mean())# prints the mean value
print(c.var()) # for getting the variance
print(c.std())# prints standard deviation
