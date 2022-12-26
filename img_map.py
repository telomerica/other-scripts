from PIL import Image, ImageDraw
import random
import numpy as np
import os

def draw_map(map_array,color_dict=None):
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
    return img


def save_map(map_array):
    zeroeth = np.flip(map_array,0)
    oneth = np.flip(map_array,1)
    z_one = np.flip(zeroeth,1)
    o_zero = np.flip(oneth,0)

    all_arrays = [map_array,zeroeth,oneth,z_one,o_zero]
    extend_list = ["f0","f1","f2","f3","f4"]
        
    ltr_list = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    nmr_list = "1234567890"
    ltr1,ltr2,ltr3 = random.sample(ltr_list,3)
    nmr1,nmr2,nmr3 = random.sample(nmr_list,3)

    for i in range(len(all_arrays)):
        extend = extend_list[i]
        generated_name = f"{extend}_{ltr1}{ltr2}{ltr3}{nmr1}{nmr2}{nmr3}"
        img = draw_map(all_arrays[i])        
        img.save(f"saved_images/{generated_name}.png")
        
        with open(f'{os.getcwd()}/saved_arrays/{generated_name}.npy', 'wb') as f:
            np.save(f, all_arrays[i])
