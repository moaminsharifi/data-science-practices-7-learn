import pandas as pd
import os
import matplotlib.pyplot as plt


def drawPlot(dataSetName='melb'):
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
        types.append(column)
        nameOfPlotFile = 'hist-'+column+'.png'
        if not os.path.exists('./app/static/images/'+dataSetName+'/hist-'+column+'.png'):
            data = csvDataFrame[column]
            figure = plt.figure(figsize=(6, 4))
            data.plot.hist(title=  dataSetName + ' ' + column + ' hist Plot',density=True,)
            plt.savefig('./app/static/images/'+ dataSetName +'/' + nameOfPlotFile )
            plt.close(figure)

        plots.append({
            'title':'historic  of ' + column,
            'type':'hist',
            'fileName': nameOfPlotFile
        })
    # relationship between cols


    return plots
