import numpy as np
import random as rd
def array_generator(m):
    x = []
    for i in range(m):
        x.append(rd.randint(0,10))
    return x

def matrix_generator(r,c):
    x = []
    for i in range(r):
        arr_hold = []
        for i in range(c):
            arr_hold.append(rd.randint(0,10))
        x.append(arr_hold)
    y = np.array(x)
    return y



a = matrix_generator(4,5)

print(a)