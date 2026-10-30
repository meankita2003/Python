from tensorflow.keras.datasets import imdb
from tensorflow.keras.models import sequential
from tensorflow.keras.layers import Embedding, LSTM, Dense
from tensorflow.keras.preprocessing.sequence import pad_sewuences





VOCA_SIZE = 10000
MAX_LENTH = 200

print("MovieReview Sentiment Analysis using LSTM...")

(x_train, Y_train), (X_text, Y_text) = imdb.load_data(num_words = )

print("IMDB dataset loaded Succesfully")

print("Number of training reviews : ",len(X_train))
print("")













word_index = imdb.get_word_index()

#Dictonary contains mapping of word and its corresponding numbers
#drisham is good movie     -> (20 56 78 43)
#20
# 56
# 78
# 43
##############################################
# step 5 : create reverse dictonary
##############################################

reverse_word_index ={}

for word