import numpy as np
import random
from perlin_noise import PerlinNoise

def sigmoid(ls):
    return 1 / (1+np.exp(-ls))

def bias(ls,bias):
    return ls+bias

def data_generator(grid,pattern,options):
    
    if pattern[0]=="random":
        ls = []
        biasdirection = random.choice([1,-1])
        bias = random.random()*biasdirection
        for row in range(grid[0]):
            ls1 = []
            for column in range(grid[1]):
                ls1.append(random.random()+bias)
            ls.append(ls1)
        
    elif pattern[0]=="patches":
        perlin = PerlinNoise(octaves=pattern[1], seed=random.randint(0,1000))
        ls = ([[perlin([_/grid[0], __/grid[1]]) for __ in range(grid[0])] for _ in range(grid[1])])
    
    ls = np.array(ls)
    
    if options[0]=="sigmoid":
        ls = sigmoid(ls)
    
    elif options[0]=="bias":
        ls = bias(ls,options[1])
        
    return ls