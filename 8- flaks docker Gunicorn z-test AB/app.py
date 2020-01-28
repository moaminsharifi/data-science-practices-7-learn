
from flask import Flask, render_template, flash, request, redirect, url_for , jsonify
import pandas as pd
import os
from werkzeug.utils import secure_filename
UPLOAD_FOLDER = '/static/uploads/'
ALLOWED_EXTENSIONS = {'csv'}
application = Flask(__name__)
application.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
@application.route("/")
def index():
    return render_template("index.html", data=[])

@application.route("/submit", methods = ['POST'])
def submit():
    if request.method == 'POST':
        if 'afile' not in request.files or 'bfile' not in request.files:
            flash('No file part')
            return redirect(request.url)
        afile = request.files['afile']
        bfile = request.files['bfile']
        if afile.filename == '' or bfile.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if (afile and allowed_file(afile.filename)) and (bfile and allowed_file(bfile.filename)):
            afile.save(afile.filename)
            bfile.save(bfile.filename)

            adf = pd.read_csv(afile.filename)
            bdf = pd.read_csv(bfile.filename)

            import statsmodels.api as sm

            convert_old = len(adf[adf['converted'] == 1])
            convert_new = len(bdf[bdf['converted'] == 1])
            n_old = len(adf.index)
            n_new = len(bdf.index)
            z_text = ''
            p_text = ''
            z_score, p_value = sm.stats.proportions_ztest([convert_old, convert_new], [n_old, n_new], alternative='smaller')



            if float(z_score) > 1.95:
                z_text ='میتونیم بگیم  که b به نسبت a بهبود پیدا کرده'
            else:
                z_text = 'میتونیم بگیم  که b به نسبت a بهبود پیدا نکرده است!'
            if float(p_value) > 0.49:
                p_text = 'بهبود گزینه a نیست به گزینه b بیشتربوده و ما نسبت به a بهبدی نداشتیم'
            else:
                p_text = 'بهبود گزینه b نسبت به گزینه a بیشتربوده '


            data = [{'z_score':z_score , 'p_value':p_value , 'z_text':z_text , 'p_text':p_text}]
            return render_template("index.html" , data=data)





if __name__ == "__main__":
    application.secret_key = 'fa7r62xuyax9x9wk69d7rnh4nejrawg3'
    application.config['SESSION_TYPE'] = 'filesystem'
    # sess.init_app(application)
    application.debug = True
    application.run(host="0.0.0.0", port=90)