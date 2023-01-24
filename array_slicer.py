import numpy as np 

def sum_rectangle(arr, x1, y1, x2, y2):
    x1, y1, x2, y2 = min(x1,x2), min(y1,y2), max(x1,x2), max(y1,y2)
    return arr[y1:y2+1,x1:x2+1].sum()
