#libraries
import numpy as np
import scipy
import csv
from PIL import Image
import glob
import os
import imageio
import csv
import ipdb
import sys
import base64
import random
import json
import matplotlib.pyplot as plt
from matplotlib.pyplot import imshow
import matplotlib.image as mpimg

def image_generator(dpi_set, a_min, a_max):
    # image generation
    airfoil_file=[os.path.basename(x) for x in glob.glob('./data_geometry/*.txt')]
    airfoil_list =[i.rsplit('.',1)[0] for i in airfoil_file]
    my_dpi= dpi_set

    #airfoil_list

    for file in airfoil_list:
        data = np.loadtxt('./data_geometry/%s.txt' % (file))
        data = data.T

        #looping through different angles
        for alpha in range(a_min, a_max+1):
            theta = alpha*np.pi/180

            #changing the origin to (0.5,0)
            data_R = data - np.array([[0.5],[0]])

            #rotation matrix
            R = np.array([[np.cos(-theta),-np.sin(-theta)],
                             [np.sin(-theta),np.cos(-theta)]])
            data1 = R @ data_R

            #changing origin back to (0,0) and extracting X and Y
            data1 = data1 + np.array([[0.5],[0]])
            X = data1[0,:]
            Y = data1[1,:] 


            plt.figure(figsize = (1500/my_dpi,1500/my_dpi), dpi=my_dpi)
            plt.fill(X,Y,'b')
            plt.axis('off')
            plt.xlim(-0.1,1.1)
            plt.ylim(-0.5,0.5)
            plt.gca().set_aspect('equal')
            plt.savefig('./data_images/%s_%s.png' % (file,alpha),dpi=my_dpi)
            plt.close()

            image = Image.open('./data_images/%s_%s.png' % (file,alpha)).convert('L')
            image.save('./data_images/%s_%s.png' % (file,alpha))

            
#Example implementation in console
# Place aerofoil coordinate list data_geometry folder. Then define dpi, min and max angles of attack for the aerofoil in sequential manner as follows: image_generator(dpi_set = 1000, a_min = 0, a_max = 1)

# from image_generator import image_generator
# image_generator(1000,0,1)