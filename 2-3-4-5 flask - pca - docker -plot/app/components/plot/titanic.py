import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np

def drawPlot(dataSetName='titanic'):
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

    # plots
    plots = []
    types = []

    # create Hist From All Cols
    for column in csvDataFrame.columns:
        if  np.issubdtype(csvDataFrame[column].dtype, np.number):
            types.append(column)
            nameOfPlotFile = 'hist-'+column+'.png'
            if not os.path.exists('./app/static/images/'+dataSetName+'/hist-'+column+'.png'):
                data = csvDataFrame[column]
                figure = plt.figure(figsize=(6, 4))
                if column == 'age':
                    data.plot.hist(title=  dataSetName + ' ' + column + ' - hist Plot' ,bins=1)
                else:
                    data.plot.hist(title=  dataSetName + ' ' + column + ' hist Plot',density=True,)
                plt.savefig('./app/static/images/'+ dataSetName +'/' + nameOfPlotFile )
                plt.close(figure)

            plots.append({
            'title':'hist  of ' + column,
            'type':'hist',
            'fileName': nameOfPlotFile
        })
    # relationship between cols


    return plots
