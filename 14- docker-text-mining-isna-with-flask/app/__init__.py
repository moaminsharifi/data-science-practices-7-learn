from flask import Flask, render_template, jsonify,request
from app.funcs import get,put
app = Flask(__name__ , static_url_path='/static')
app.debug = True
app.config['TEMPLATES_AUTO_RELOAD'] = True

# section one


# plot


from mpl_toolkits.mplot3d import Axes3D

# sklearn

from sklearn.decomposition import PCA
from sklearn import preprocessing


from app import views