'''
this ann gonna work without trainning because we already have a model.h5 file saved.
'''


from keras.datasets import mnist
import matplotlib.pyplot as plt # this is to visualize data
#from tensorflow.python.keras.models import load_model
from keras.models import load_model
import numpy as np
import cv2 #pip install opencv-python
# load data sets
import requests
import os

class Capsol:

    def __init__(self):
        pass

    def hcap(self):
        #================check whether the model working start=================
        # Now I should check with h5 file whether it is predicting with accuracy
        # to do this I must load the model first
        obj = load_model(os.path.join('appointment/model.h5'))
        #just checking summary not essential
        # print(obj.summary())

        '''
        but to remember: ANN/ fully connected NN a amra only can use 1 dimensional data but our shape show 28,28 that means 2 dimension
        '''
        # so reshape it to make one dimensional
        # below is the flatten shape

        #================check whether the model working end=================



        #========================================================================================
        #================New unknown data to read and classify starting===========================
        # in this section we need cv2
        # load data first
        img = cv2.imread(os.path.join('appointment/new.jpg'))
        #img = cv2.imread('air.jpg')
        #img = cv2.imread('bus.jpg')
        # just to know what is the img actually
        # plt.imshow(img)
        # plt.show()
        #to know the shpae
        # print(img.shape) # (28, 28, 3) it has three scale but trained data has only one scale
        # to shape it 28*28 and channel should be one
        shaped = cv2.resize(img, (100, 100))
        # print(shaped.shape) #(28, 28, 3) but still channel is 3
        # eita solve korar jonno first gray scale a convert korte hobe
        # img_gray = cv2.cvtColor(shaped, cv2.COLOR_BGR2GRAY)
        #print(img_gray.shape) #(28, 28)

        fallten_img = shaped.reshape(1, 100, 100, 3)
        #print(fallten_img.shape) # (1, 784)

        #now test it
        predicted = obj.predict(fallten_img)
        result_output = np.argmax(predicted, axis=1) #flatten korar karon hosse fully connected/ann only support one dimension
        result_output = result_output[0]
        # print(result_output) # this is the output of new img reading
        return result_output


#================New unknown data to read and classify end===========================

#=====================run the class========
# if __name__ == '__main__':
#     bot = Capsol()
#     bot.hcap()