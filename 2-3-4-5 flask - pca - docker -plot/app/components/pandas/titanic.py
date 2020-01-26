
import pandas as pd
import os
def drawTable(dataSetName = 'titanic'):
    """ open and get some condion of data set
    Get: dataset Name
    Return: dict of head and summery
    """
    #change current dir to main dir for unit check JUST
    #os.chdir("../../..")

    # open csv
    pathOfCsv = './app/static/datasets/csv/' + dataSetName + '.csv'
    csvDataFrame = pd.read_csv(pathOfCsv)
    csvDataFrame.fillna(method='bfill', inplace=True)

    # get 5 top of head dataset
    headOfDataFrame = csvDataFrame.head()

    # get
    describeOfDataFrame = csvDataFrame.describe()

    # put in standard
    tables =[
        {
            'title': 'titanic head',
            'dataset':headOfDataFrame
        },
        {
            'title': 'titanic describe',
            'dataset':describeOfDataFrame.T
        }
    ]
    return tables
