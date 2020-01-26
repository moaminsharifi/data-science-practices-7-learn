
import pandas as pd
import os
def drawTable(dataSetName = 'melb'):
    """ open and get some condion of data set
    Get: dataset Name
    Return: dict of head and summery
    """
    #change current dir to main dir for unit check JUST
    #os.chdir("../../..")
    # open csv
    pathOfCsv = './app/static/datasets/csv/' + dataSetName + '.csv'
    csvDataFrame = pd.read_csv(pathOfCsv)

    # get 5 top of head dataset
    headOfDataFrame = csvDataFrame.head()

    # get  # get describe
    describeOfDataFrame = csvDataFrame.describe()

    # put in standard
    tables =[
        {
            'title': 'melb head',
            'dataset':headOfDataFrame
        },
        {
            'title': 'melb describe',
            'dataset':describeOfDataFrame.T
        }
    ]
    return tables
