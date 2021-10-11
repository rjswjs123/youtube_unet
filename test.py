import numpy as np
from PIL import Image
import os
path_dir='./dataset_test/'
file_list=os.listdir(path_dir)

for png in file_list:
    image = Image.open(path_dir + png)
    pixel = np.array(image)
    png = png.split('.')[0]
    np.save("./npy_test/" + png, pixel)

