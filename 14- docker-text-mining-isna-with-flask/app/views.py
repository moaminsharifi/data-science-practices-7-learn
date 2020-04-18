from app import app, render_template,jsonify, get,put , request
from hazm import word_tokenize
from hazm.Stemmer import Stemmer


@app.route('/' , methods=['POST','GET'])
def home():
    
    if request.method == 'POST':
        inputText = request.form['text']
        nltk_stopwords = get('stopwords')
        # stemmer = Stemmer()
        title_body_tokenized = word_tokenize(inputText)
        title_body_tokenized_filtered = [w for w in title_body_tokenized if not w in nltk_stopwords]
        # title_body_tokenized_filtered_stemming =  [stemmer.stem(w) for w in title_body_tokenized_filtered]
        # print(title_body_tokenized_filtered_stemming)

        vectorizer = get('vectorizer')
        title_body_tokenized_filtered_stemming_vectorized = vectorizer.transform(title_body_tokenized_filtered)
        model = get('model')
        predict = model.predict(title_body_tokenized_filtered_stemming_vectorized)
        
        lables = get('lables')
        lable = lables[predict]
        return render_template('index.html', lable=lable , stemer=title_body_tokenized_filtered_stemming)
    else:
        return render_template('index.html')


    

