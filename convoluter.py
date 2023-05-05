def convert_img(directory):
    img = mpimg.imread(directory)
    img = np.array(img)
    array = np.dot(img[..., :3], [0.2989, 0.5870, 0.1140])
    return array



def convolute(array, kernel, stride):
    rows, columns = array.shape
    out_rows = (rows - kernel) // stride + 1
    out_columns = (columns - kernel) // stride + 1

    strides = (array.strides[0] * stride, array.strides[1] * stride, *array.strides)
    strided_array = as_strided(array, shape=(out_rows, out_columns, kernel, kernel), strides=strides)

    ls = np.average(strided_array, axis=(2, 3))

    return ls

#kernel_size = 20
#stride = 1

#array = convert_img("imgae.png")
#result = convolute(kernel=kernel_size, stride=stride, array=array)

#plt.imshow(result, cmap='gray')
#plt.show()
