import numpy as np
import random
from perlin_noise import PerlinNoise

def sigmoid(array):
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

def data_generator(grid,pattern,options):
    
    if pattern[0]=="random":
        mappe = random_(grid)
        
    elif pattern[0]=="patches":
        mappe = perlin_(grid=grid,octaves=pattern[1])
    mappe = np.array(mappe)
    
    if options[0]=="sigmoid":
        mappe = sigmoid(mappe)
    
    elif options[0]=="bias":
        mappe = bias_(mappe,options[1])
        
    return mappe