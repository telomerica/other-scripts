from PIL import Image, ImageDraw
import random
import numpy as np
import os

def draw_map(map_array,color_dict=None,float=False):
    if color_dict==None:
        color_dict = {0:(11,180,60),1:(105,119,46),2:(157,206,243),3:(0,0,0)}
    
    if float==True:
        color_dict = {}
        for i in range(255):
            color_dict[i]=(i,i,i)
        map_array = np.rint(map_array*255)

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


def save_map(map_array,color_dict=None,draw=True,float=False):
    zeroeth = np.flip(map_array,0)
    oneth = np.flip(map_array,1)
    z_one = np.flip(zeroeth,1)

    all_arrays = [map_array,zeroeth,oneth,z_one]
    extend_list = ["f0","f1","f2","f3"]
            
    already_saved = (os.listdir("saved_arrays"))
    a_ls = []
    for i in already_saved:
        l,b = i.split("-")
        a_ls.append(int(l))


    a_ls.sort()
    last_number = int(a_ls[-1])
    next_number = last_number+1

    for i in range(len(all_arrays)):
        extend = extend_list[i]
        generated_name = f"{next_number}-{extend}"
        if draw==True:
            img = draw_map(all_arrays[i],color_dict,float)        
            img.save(f"saved_images/{generated_name}.png")
        
        with open(f'{os.getcwd()}/saved_arrays/{generated_name}.npy', 'wb') as f:
            np.save(f, all_arrays[i])
