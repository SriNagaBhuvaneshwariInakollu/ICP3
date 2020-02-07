import numpy as np

#a=np.array([1,4,5,2,4,7,9,3,2,3,0,1,3,6,8])

a = np.random.randint(size=15, low= 1, high=20)
print (a)
b=a.reshape((3,5))
print (b)


max_value=np.max(b,axis=1)
print(max_value)

b=np.where(b==np.max(b,axis=1).reshape(-1,1),0,b)
print(b)








