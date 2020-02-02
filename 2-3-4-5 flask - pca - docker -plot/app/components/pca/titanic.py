import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import pyplot
from mpl_toolkits.mplot3d import Axes3D
from sklearn import decomposition, datasets

def drawPca(dataSetName='titanic'):
    """ open and get some condion of data set
    Get: dataset Name
    Return: dict of head and summery
    """
    # change current dir to main dir for unit check JUST
    #os.chdir("../../..")
    #print(os.getcwd())
    # open csv
    pathOfCsv = './app/static/datasets/csv/' + dataSetName + '.csv'
    csvDataFrame = pd.read_csv(pathOfCsv, index_col=0, parse_dates=True)
    csvDataFrame.fillna(method='bfill', inplace=True)

    # pca
    pcaList = []
    types = []

    # create Hist From All Cols
    flag = True
    pathOfImage = './app/static/images/'+dataSetName+'/pca.png'
    if flag: #or not os.path.exists(pathOfImage):
        flag = True
        for column in csvDataFrame.columns:
            if  np.issubdtype(csvDataFrame[column].dtype, np.number) and column != 'Survived':
                    types.append(column)
                

    if flag:
        X = csvDataFrame[types]
        y = csvDataFrame['Survived']

        figure = pyplot.figure(1, figsize=(4, 3))
        pyplot.clf()
        axes = Axes3D(figure, rect=[0, 0, 0.95, 1], elev=48, azim=134)
        pyplot.cla()
        
        pca = decomposition.PCA(n_components=len(types))
        pca.fit(X)
        X = pca.transform(X)
        for name, label in [('Dead', 0), ('Survived', 1)]:
            axes.text3D(X[y == label, 0].mean()+ np.random.randint(0,5) ,
               X[y == label, 1].mean() + np.random.randint(0,5),
                7 + np.random.randint(0,5),
               name,
               horizontalalignment='center')
        
        y = np.choose(y, [1, 0]).astype(np.float)
        axes.scatter(X[ :, 0 ] , X[ :, 1 ] , X[ :, 2 ], X[ :, 3 ]  , c=y, cmap=pyplot.cm.nipy_spectral, edgecolor='k')
        axes.w_xaxis.set_ticklabels([])
        axes.w_yaxis.set_ticklabels([])
        axes.w_zaxis.set_ticklabels([])
        figure.savefig(pathOfImage)



    pcaList.append({
                'title':'PCA  of Titanic',
                'type':'pca',
                'fileName': 'pca.png'
            })
    # relationship between cols


    return pcaList
