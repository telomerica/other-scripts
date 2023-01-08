import numpy as np
import random
from perlin_noise import PerlinNoise

def array_builder(map_array, steps):
    temp_array = map_array
    for step in steps:
        temp_array=step["method"](temp_array,**step["args"])
    return temp_array

def sigmoid_(array,float=False):
    return 1 / (1+np.exp(-array))

def bias_(array,bias,float=False):
    return array+bias

def random_(array,probability,float=False):
    x = array
    for row in x:
        coords = np.random.randint(0,len(row),size=(int(len(row)*probability)))
        r = np.random.rand(*row.shape)
        row[coords] = r[coords]
        #print(row)
    return x

def perlin_(array,octaves,seed,object,bias=0,float=False):
    grid = array.shape
    perlin = PerlinNoise(octaves=octaves, seed=seed)
    temp = ([[perlin([_/grid[0], __/grid[1]]) for __ in range(grid[0])] for _ in range(grid[1])])
    temp = np.array(temp)+bias
    
    if float==False:
        temp = (np.rint(sigmoid_(temp))).astype(int)
        temp_w = np.where(temp==1)
        for x in range(len(temp_w[0])):
            array[temp_w[0][x]][temp_w[1][x]] = object
    else:
        array = array+temp
    return array

