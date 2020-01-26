from app import app, render_template, Axes3D, PCA, preprocessing ,jsonify
from app.components.pandas.airbase import drawTable as airbaseTable
from app.components.pandas.flow import drawTable as flowTable
from app.components.pandas.melb import drawTable as melbTable
from app.components.pandas.titanic import drawTable as titanicTable
from app.components.plot.airbase import drawPlot as airbasePlot
from app.components.plot.flow import drawPlot as flowPlot
from app.components.plot.melb import drawPlot as melbPlot
from app.components.plot.titanic import drawPlot as titanicPlot
dataSets = ['airbase', 'flow', 'melb', 'titanic']


@app.route('/')
def home():
    return render_template('index.html', dataSets=dataSets)


@app.route('/github')
def github():
    return render_template('index.html', dataSets=dataSets)


@app.route('/table/<dataSetName>')
def showTable(dataSetName):
    if dataSetName in dataSets:
        tables = []
        if dataSetName == dataSets[0]:
            tables = airbaseTable()
        elif dataSetName == dataSets[1]:
            tables = flowTable()
        elif dataSetName == dataSets[2]:
            tables = melbTable()
        elif dataSetName == dataSets[3]:
            tables = titanicTable()

        return render_template('draw-table.html', tables=tables, name=dataSetName)
    else:
        return render_template('404.html', name=dataSetName, dataSets=dataSets, code=404)


@app.route('/plot/<dataSetName>')
def showPlot(dataSetName):
    if dataSetName in dataSets:
        plots = []
        if dataSetName == dataSets[0]:
            plots = airbasePlot()
        elif dataSetName == dataSets[1]:
            plots = flowPlot()
        elif dataSetName == dataSets[2]:
            plots = melbPlot()
        elif dataSetName == dataSets[3]:
            plots = titanicPlot()
        print(plots)
        return render_template('draw-plot.html', plots=plots, name=dataSetName)
    else:
        return render_template('404.html', name=dataSetName, dataSets=dataSets, code=404)


def DrawPlotAirBase():
    return
