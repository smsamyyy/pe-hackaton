import numpy as np

bo={}

bo['b5X12']= np.ones((5,12))
bo['b6X10']= np.ones((6,10))
bo['b4X15']= np.ones((4,15))
bo['b3X20']= np.ones((3,20))
m= np.ones((8,8))
m[4,4]=-1
m[4,3]=-1
m[3,4]=-1
m[3,3]=-1
print(m)
bo['b8X8_obst_2X2mid'] = m
bo['2xb5X6']= np.array([np.ones((5,6)),np.ones((5,6))])
print(bo['2xb5X6'])