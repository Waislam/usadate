'''batch size holo how many images will be train on each epoch

rescaling holo protita img er pixel/value k nia ekta arrray create kora
'''
#===========================install and import requirements start ======================
# for data processing
import matplotlib.pyplot as plt # for img visualization (imshow)
import numpy as np # special for array/ list operation
import cv2  # pip install opencv-python (this is actually for img conversion) (convert img into array)
import os
import random

# for model trannnng purpose
import tensorflow as tf
from tensorflow import keras
from keras.models import Sequential
from keras.layers import Conv2D, Dense, MaxPooling2D, Flatten, Activation


#===========================install and import requirements end ======================

######============DATA PRE PROCESS============
'''steps 1. make data directory, and subdirectory
2. loop over directory
3. make a list of subdirectory and loop over 
4. read img from sub directory
5. convert img to array/matrics 
6. resize img
7 create and list of data with label by appending img array/list
8. shuffling/random to mix up newly data
9. create two seperate list of img and label
10. convert those list into array to avoid trainning problem
11. rescaling/feature value reducing rescaling'''
#==============defining directory path start =============
DATADIR = os.path.join(r"mydata")
CATEGORIES = ['bus', 'motorcycle', 'airplane', 'truck', 'bicycle', 'seaplane', 'boat']

data = []
#try to connect with these above directory
for category in CATEGORIES:
    folder = os.path.join(DATADIR, category)
    label = CATEGORIES.index(category) # this will show folder index value
    # now fetch img from every folder
    for img in os.listdir(folder):# os.listdir just make a list of all contents from the folder
        image = os.path.join(folder, img)

        #now I need to convert img to array... to do this I need to read img
        img_arr = cv2.imread(image) #it makes a matrics/array
        '''note: as every imgae may not be the same size so we should resize every img according to a certain size using cv2'''
        img_arr = cv2.resize(img_arr, (100, 100))

        # plt.imshow(img_arr)
        # plt.show()
        data.append([img_arr, label])
        #######it is time to bring label for every img
        ######### category er index value k lavel hishebe nite pari

        # break;
# shuffling the data
shuffled_data = random.shuffle(data)


# making seperate list for img and label
x = []
y = []

for features, labels in data:
    x.append(features)
    y.append(labels)


# convert above list into array/matrics
x = np.array(x)
y = np.array(y)

# rescaling
x = x/255 #it won't effect on img quality and reduce the memory space size (eita muloto value k 0 and 1 er moddhe ana)



#==============defining directory path end =============


#============Model creating===============
'''
1. create model 2. add convolution layer 3. add max pooling layer 4. add droupout layer, flattenning and dense layer
'''

model = Sequential()
# more than on e conv and maxpooling layer increase the accuracy
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=x.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Conv2D(32, kernel_size=(3,3), activation='relu', input_shape=x.shape[1:]))
model.add(MaxPooling2D(pool_size=(2, 2)))


model.add(Flatten())
model.add(Dense(7, activation='softmax'))

# optimizer = tf.keras.optimizers.Adam()
optimizer = "adam"
# loss = tf.keras.losses.categorical_crossentropy
loss = "sparse_categorical_crossentropy"
# compile now
model.compile(loss=loss,
            optimizer=optimizer,
            metrics=['accuracy'])
#============Model creating end===============

####################train now
model.fit(x, y,
        batch_size=20,
        epochs=25, #how many times trainning will be done
        # validation_data=(x_test, y_test))
        validation_split=0.1)

model.save(os.path.join('model.h5'))
#===================test an img start=========================
# test_img = x[0].reshape(100, 100, 3)
# plt.imshow(test_img)
# plt.show()
# test_img = test_img.reshape(1, 100, 100, 3)
#
# pred = model.predict(test_img)
# output = np.argmax(pred, axis=1)
# print('this is the ouput')
# print(output)
#===================test an img end=========================