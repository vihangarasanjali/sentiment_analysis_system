from flask import Flask,render_template,request,redirect
from predict import preprocessing,vectorizer,get_prediction
from logger import logging

app = Flask(__name__)
logging.info('Flask app running on port 5000')

data = dict()
reviews = []
positive_reviews = 0
negative_reviews = 0

@app.route('/')
def index():
    data['reviews'] = reviews
    data['positive'] = positive_reviews
    data['negative'] = negative_reviews
    logging.info('Rendering index.html with data:', data)
    return render_template('index.html', data=data)

@app.route('/', methods=['POST'])
def my_post():
    text = request.form['text']
    logging.info(f'Received text: {text}')

    preprocessed_text = preprocessing(text)
    logging.info(f'Preprocessed text: {preprocessed_text}')

    vectorized_text = vectorizer(preprocessed_text)
    logging.info(f'Vectorized text: {vectorized_text}')

    prediction = get_prediction(vectorized_text)
    logging.info(f'Prediction: {prediction}')

    if prediction == 'negative':
        global negative_reviews
        negative_reviews += 1
    else:
        global positive_reviews
        positive_reviews += 1

    reviews.insert(0, text)
    return redirect(request.url)

if __name__ == '__main__':
    app.run(debug=True)