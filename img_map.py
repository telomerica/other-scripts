from PIL import Image, ImageDraw
import random
import numpy as np
import os

def draw_map(map_array,save=False,color_dict=None):
    if color_dict==None:
        color_dict = {0:(120,180,60),1:(105,119,46),2:(157,206,243),3:(0,0,0)}
    img = Image.new("RGB", (map_array.shape))
    img1 = ImageDraw.Draw(img)  
    img1.rectangle( [(0,0),(map_array.shape)] ,fill="white",outline="white")
    
    for element in color_dict:
        b,a = np.where(map_array==element)
        color = color_dict.get(element)
        for index,x in enumerate(a):
            y = b[index]
            img.putpixel((x,y),(color))

     
    nym = ""
    for x in range(5):
        nym = nym+str(random.randint(0,10))
    img.save(f"maps/{nym}.png")
    img.show()
    if save==True:
        with open(f'{os.getcwd()}/saved_arrays/{nym}.npy', 'wb') as f:
            np.save(f, map_array)
