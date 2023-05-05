def convert_img(directory):
    img = mpimg.imread(directory)
    img = np.array(img)
    array = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])

    return array

def convolute(array,kernel,stride,return_image=False):
    rows = array.shape[0]
    columns = array.shape[1]

    ls = []
    for row in range(rows-kernel):
        ls1=[]
        for i in range(columns-kernel):
            tile_value=np.sum(array[0+(row*stride):kernel+(row*stride),0+(i*stride):kernel+(stride*i)])/(kernel*kernel)
            ls1.append(tile_value)
        ls.append(ls1)
    ls=np.array(ls)
    #if return_pillow_image:
    return ls


#kernel_size = 20
#stride = 1

#array = convert_img("image.png")
#result = convolute(kernel=kernel_size, stride=stride, array=array, return_image=True)

#plt.imshow(result, cmap='gray')
#plt.show()
