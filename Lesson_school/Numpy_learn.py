import numpy as np

data = np.array([[1,2,3,4,5],[2,3,4,5,6]])
print(data)

'''
创建全零数组
'''

d2 = np.zeros(shape=(2,3))
print(d2)

'''创建全空数组'''

d3 = np.empty(shape=(2,3))
print(d3)

# d4 = np.arange(2,1000000000,2)
# print(d4)
np.save('my11np.npy',d3)
