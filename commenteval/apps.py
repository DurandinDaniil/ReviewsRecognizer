from django.apps import AppConfig
import joblib
import re
from nltk.stem.porter import PorterStemmer

vectorizer = joblib.load('commenteval/models/vectorizer.pkl')

regressor = joblib.load('commenteval/models/MLP_model.pkl')

with open('commenteval/models/english') as f:
    stopwords = f.read().split('\n')

class CommentevalConfig(AppConfig):
    name = 'commenteval'


class ML:

    
    def __init__(self):

        self.vectorizer = vectorizer
        self.regressor = regressor


    def text_preprocessing(self, input_text):
    
        review = re.sub('[^a-zA-Z]', ' ', input_text)
        review = review.lower()
        review = review.split()
        ps = PorterStemmer()
        review = [ps.stem(word) for word in review if not word in set(stopwords)]
        review = ' '.join(review)

        return review