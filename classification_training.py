import pickle
from tqdm import tqdm
import numpy as np
from PIL import Image
import numpy as np
import os
import json
from PIL import Image
from keras.models import Sequential, Model
from keras.layers import Input, Conv2D, MaxPooling2D, Flatten, Dense
from keras.applications import ResNet50, VGG19
from keras import activations, losses, optimizers
import numpy as np
import shapely.wkt
import shapely
from shapely.geometry import Polygon



vgg_model = VGG19()

vgg_model.trainable = False
model = Model(inputs = vgg_model.input, outputs = vgg_model.layers[-3].output)

with open('training_data.pkl', 'rb') as handle:
    training_data = pickle.load(handle)

from sklearn.model_selection import train_test_split
from tqdm import tqdm
def preprocess_data(training_data, train_size=0.7):
    xdata, ydata = [], []
    for img_name in tqdm(list(training_data.keys())):
        for uid in list(training_data[img_name].keys()):
            pre_img = np.array(Image.fromarray(training_data[img_name][uid]['pre']).resize((224, 224)))
            post_img = np.array(Image.fromarray(training_data[img_name][uid]['post']).resize((224, 224)))
            
            X1 = model.predict(pre_img.reshape(-1, 224, 224, 3))
            X2 = model.predict(post_img.reshape(-1, 224, 224, 3))
        
            
            xdata.append(np.multiply(X1, X2) / (np.linalg.norm(X1, 2) * np.linalg.norm(X2, 2)))
            ydata.append(training_data[img_name][uid]['label'])
    X, y = np.array(xdata), np.array(ydata)
    Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, train_size=train_size)
    return Xtrain, Xtest, ytrain, ytest

Xtrain, Xtest, ytrain, ytest = preprocess_data(training_data)

np.save('xtrain', Xtrain)
np.save('xtest', Xtest)
np.save('ytrain', ytrain)
np.save('ytest', ytest)