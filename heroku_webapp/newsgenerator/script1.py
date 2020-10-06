from flask import Flask, render_template
import numpy as np
import pandas as pd
# import os
# import sys
#from app.main import app 

app = Flask(__name__) 

# headlines filepath
LSTM_HEADLINES_CSV_PATH = './static/generated_LSTM_headlines.csv'
RNN_HEADLINES_CSV_PATH = './static/generated_RNN_headlines.csv'

#load all headlines from csv to dataframe
headlines_lstm_df = pd.read_csv(LSTM_HEADLINES_CSV_PATH, header = None)
headlines_rnn_df = pd.read_csv(RNN_HEADLINES_CSV_PATH, header = None)

@app.route("/")
def home():
    #return '<h1>Newsgenerator</h1>'
    return render_template("home.html")

@app.route('/generate_news/')
def generate_news():
    # LSTM Headlines section
    # set variables for for random headline sampling 
    total_lstm_headlines = len(headlines_lstm_df) +1
    lstm_headlines_to_load = 5
    lstm_headlines = []
    random_lstm_headline_index = []

    # loop through num_headlines to retrieve 
    for n in range(lstm_headlines_to_load):
        rand_num = np.random.randint(0, total_lstm_headlines-1, size = 1)[0]
        while rand_num in random_lstm_headline_index:
            rand_num = np.random.randint(0, total_lstm_headlines-1, size = 1)[0]
        random_lstm_headline_index.append(rand_num)
        lstm_headlines.append(headlines_lstm_df[0][rand_num])


    # RNN Headlines section
    # set variables for for random headline sampling 
    total_rnn_headlines = len(headlines_rnn_df) +1
    rnn_headlines_to_load = 5
    rnn_headlines = []
    random_rnn_headline_index = []

    # loop through num_headlines to retrieve 
    for n in range(rnn_headlines_to_load):
        rand_num = np.random.randint(0, total_rnn_headlines-1, size = 1)[0]
        while rand_num in random_rnn_headline_index:
            rand_num = np.random.randint(0, total_rnn_headlines-1, size = 1)[0]
        random_rnn_headline_index.append(rand_num)
        rnn_headlines.append(headlines_rnn_df[0][rand_num])

    return render_template('generate_news.html', news_content1=lstm_headlines, news_content2=rnn_headlines)

#@app.route('/generate_news2', methods=("POST", "GET"))
#def generate_news2():
#    return render_template('generate_news2.html',  tables=[df1.to_html(classes='data')], titles=df1.columns.values)

if __name__ == "__main__": 
    app.run(debug=True)
