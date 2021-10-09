

# Movie review sentiment classification

This is an implementation of a movie review sentiment classifier based in IMDB data

Documentation about model and data:

[Bidirectional LSTM on IMDB]('https://keras.io/examples/nlp/bidirectional_lstm_imdb/')


## How to run it

1. Create virtual environment and install libraries

`pip install -r requirements.txt`

2. Train the model

`python model.py`

3. Use the model to make a prediction on a new movie review that can be passed via terminal

`python predict.py "This movie is so bad I could not finish it"`

`python predict.py "Amazing movie. Will watch it again"`

The score will be printed in the terminal. It takes values from 0 to 1. The higher the score the more positive is the review.



