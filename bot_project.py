pip install python-telegram-bot
pip install telebot
pip3 install PyTelegramBotAPI
import telebot
from telebot import types
import pandas as pd
import nltk

pip install markovify
import markovify

from sklearn.utils import shuffle
from collections import Counter
import itertools
import random
from nltk.tokenize import sent_tokenize, word_tokenize
import nltk
nltk.download('punkt')

from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.layers import LSTM, TimeDistributed, Bidirectional
from keras.models import Sequential
from keras.layers import Dense, Activation, Embedding, Flatten, Dropout

df = pd.read_csv("C:/Users/Валерия/Desktop/wiki_movie_plots_deduped.csv'")
with open('markov_chain.pkl', 'rb') as f:
     markov = pickle.load(f)

def neural_network(name):
    


TOKEN = ('851227046:AAH5_p3gvo2hoClaj6CSwSzIMdYleva8gHs')
bot = telebot.TeleBot(TOKEN)

@botmessagehandler(commands ['start'])
def startCommand(m):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard = True)
    keyboard.add(*[types.KeyboardButton(name) for name in ['Markov Chain', 'Neural Network']])
    msg = bot.send_message(m.chat_id, 'Press the button to generate a movie plot!', reply_markup = keyboard)
    bot.register_next_step_handler (msg, name)

def name(m):
    if m.text == 'Markov Chain':
        
       
        
        
        
        
        
bot.polling()        
    
    
    




    

    
    

