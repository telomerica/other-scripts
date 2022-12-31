from array_builder import *
from img_map import *
from convoluter import *
import numpy as np

for i in range(1):
    array = (array_builder(
        map_array=np.zeros((500,500)),
        steps=[
    {"method":bias_,"args":{"bias":0.1,"float":True}},
    {"method":perlin_,"args":{"octaves":random.choice([3,5,10]),"seed":random.randint(0,100),"object":1,
    "bias":random.choice([0,-0.1,-0.2,-0.25]),"float":True}},
    {"method":perlin_,"args":{"octaves":random.choice([10,20,30]),"seed":random.randint(0,100),"object":1,
    "bias":random.choice([0,-0.2,-0.4,-0.5]),"float":True}},
    {"method":random_,"args":{"probability":random.choice([0.5,0.1,0.15,0.2]),"float":True}},

    ]
    ))

    #img=draw_map(array,color_dict=False,float=True)
    #img.show()
    #print(array)
    #save_map(array,color_dict=None,draw=True,float=True)
    #print(i)
    ls=convolute(array,3,1)
    ls1=convolute(array,10,3)

    img=draw_map(array,color_dict=False,float=True)
    img.show()

    img1=draw_map(ls,color_dict=False,float=True)
    img1.show()

    img2=draw_map(ls1,color_dict=False,float=True)
    img2.show()