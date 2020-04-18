import pandas as pd
from sklearn.model_selection import train_test_split
import numpy as np
import pickle
import os
from funcs import get,put,files_exist
from PIL import Image
def get_or_gen(seed = 420  ,test_size = 0.15,random_state = 0):

    """
    CHECK IF PICKLE FILE NOT EXIST THEN CREATE THEM
    """
    print("""
    LET'S CREATE DATA.
    """)
    np.random.seed(seed)
    def one_hot_encoding(Y):
        lenght_Y =len(Y)
        unqiue_Y = np.unique(Y)
        lenght_unqiue_Y = len(unqiue_Y)
        onc_Y = np.zeros(( lenght_Y, lenght_unqiue_Y))

        for idx in range(len(Y)):
            onc_Y[idx][np.where(unqiue_Y == Y[idx])] = 1
        return onc_Y , unqiue_Y
        
    def read_all_files_as_numpy(dataset_path = 'dataset' ):
        dataset_classes = os.listdir(dataset_path)
        X = []
        Y = []
        for dataset_class in dataset_classes:
            class_files = os.listdir('./{}/{}'.format(dataset_path,dataset_class))
            class_files = [np.array(Image.open('./{}/{}/{}'.format(dataset_path,dataset_class,file))) for file in class_files]
            for file_np_array in class_files:
                X.append(file_np_array)
                Y.append(dataset_class)
        # one hot encoding Y
        Y , lables = one_hot_encoding(Y)
        # as numpy
        X = np.array(X) / 255.0
        Y = np.array(Y)
        return X , Y , lables
        



  
    files_list = ['label.pickle' ,'X_train.pickle','y_train.pickle','X_val.pickle','y_val.pickle' ]
    if files_exist(files_list):
        print("""
        check and all need file sound like exist! Let's Read Them.
        """)
        X_train = get('X_train')
        X_val= get('X_val',)
        y_train = get('y_train')
        y_val = get('y_val')
        lables = get('lables')
        print("""
        Read Done, Let's use them.
        """)
        return X_train , X_val , y_train , y_val , lables
        


    else:
        print("""
        DATA GENRATOR CONFIGED BY
        NUMPY SEED: {}
        TEST SIZE: {}
        RANDOM SKLEARN SEED: {}
        """.format(seed, test_size, random_state))
        # save lable in file
        label_map = ['Anger', 'Disgust', 'Fear', 'Happy', 'Sad', 'Surprise', 'Neutral']
        #save lable in file
        put('label',label_map)
        
        # get data and X and Y and split
        X, Y , lables= read_all_files_as_numpy()


        X_train, X_val, y_train, y_val = train_test_split(X, Y, test_size=test_size, random_state=random_state)

        # save in file
        put('X_train',X_train)
        put('X_val',X_val)
        put('y_train',y_train)
        put('y_val',y_val)
        put('lables',lables)
        print("""
        All file created! Let's Use Them.
        """)
        return X_train , X_val , y_train , y_val , lables

def decode(y , lables):
    pass

def resizer(paths= [], size_w = 128, size_h = 128):
    import cv2
    for path in paths:
        path_files = os.listdir(path)
        for file in path_files:
            src = '{}/{}'.format(path,file)
            img = cv2.imread(src, cv2.IMREAD_UNCHANGED)
            dim = (size_w, size_h)
            resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
            cv2.imwrite(src,resized)


    pass





