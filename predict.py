from tensorflow import keras
from nltk import word_tokenize
from keras.preprocessing import sequence
import sys

from params import maxlen, max_features

# necessary first time
# import nltk
# nltk.download()

review_text = sys.argv[1]

def review_preprocess(review_text):
    review_text = review_text.lower()
    review_text = ' '.join(e for e in review_text.split(' ') if e.isalnum())
    return review_text


def predict(review_text):
    model = keras.models.load_model('models/model1')
    word2index = keras.datasets.imdb.get_word_index()

    test = []
    for word in word_tokenize(review_text):
        if word in word2index.keys():
            test.append(word2index[word])

    test = [index for index in test if index < max_features]

    test = sequence.pad_sequences([test], maxlen=maxlen)
    rating_prediction = model.predict(test)

    return rating_prediction


if __name__ == '__main__':
    review_text = review_preprocess(review_text)
    print(predict(review_text))
