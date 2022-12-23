import numpy as np
import random
from perlin_noise import PerlinNoise

def sigmoid_(array):
    return 1 / (1+np.exp(-array))

def bias_(array,bias):
    return array+bias

def random_(grid):
    ls = []
    biasdirection = random.choice([1,-1])
    bias = random.random()*biasdirection
    for row in range(grid[0]):
        ls1 = []
        for column in range(grid[1]):
            ls1.append(random.random()+bias)
        ls.append(ls1)
    return ls

def perlin_(grid,octaves,seed=False):
    perlin = PerlinNoise(octaves=octaves, seed=random.randint(0,1000))
    array = ([[perlin([_/grid[0], __/grid[1]]) for __ in range(grid[0])] for _ in range(grid[1])])
    return array

def array_builder(grid,functionslist):
    grid = np.zeros(grid)
    
    dict_of_functions={"random":random_,"perlin":perlin_,"sigmoid":sigmoid_,"bias":bias_}
    for fc in functionslist:
        function = dict_of_functions.get(fc[0])
        print(fc[1])
        mappe = function(*fc[1]) #fc0 = function's string name, fc1 = function's options
    return mappe