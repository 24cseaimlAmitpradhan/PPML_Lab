import numpy as np
arr=np.array([1,2,3,4])
np.save=('My_array',arr)
loaded_arr=np.load('My_array.npy')
print("Loaded array:",loaded_arr)