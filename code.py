import nltk
nltk.download('stopwords')
import pickle
import re
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from sklearn.feature_extraction.text import CountVectorizer
from flask import Flask
from flask import request


app = Flask(__name__)



ps = PorterStemmer()

filename = 'finalized_model.sav'
loaded_model = pickle.load(open(filename, 'rb'))
cv = pickle.load(open("vector.pickel", "rb"))

@app.route("/")
def hello():
  return "<h1>Running</h1>"
@app.route("/predict",  methods=['POST'])
def predict_title():
  rdata =  request.get_json()
  dt = rdata["name"]
  corpus = [dt]
  print(corpus)
  new_corpus = []
  for i in range(0, len(corpus)):
      review = re.sub('[^a-zA-Z]', ' ', corpus[i])
      review = review.lower()
      review = review.split()
      review = [ps.stem(word) for word in review if not word in stopwords.words('english')]
      review = ' '.join(review)
      new_corpus.append(review)
  g = cv.transform(new_corpus).toarray()
  pred = loaded_model.predict(g)
  if (pred[0] == 1):
    return "Unreliable"
  else:
    return "Reliable"