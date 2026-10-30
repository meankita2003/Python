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



def DecodeRevview(encoded_review):
    words = []


   for number in encoded_review:
    if number >= 3:#ignore first 3
        word = reverse_word_index.get(number,"?")
        words.appended(word)


        returns



        #######################################
        # step 7 : Display sample review
        ######################################3


print("--"*40)
print("____________Sampe Review______________")
print("__"*40)

for i in range(3,7)
review = DecodeReview(X_train(i))

print("Review number : i+1")
print("Review :")
print(review)

print("_"*40)
if Y_train






#####################################################
# step 8 : Paddintg
#####################################################


x_train_Padded = pad_sequences(
    X_train,
    max.len = MAX_LENTH
    )
 print("Training data shape :",X_)







#######################################################
# step 9 : Create LSTM model
#######################################################


model = sequential()

model.add(
   Embedding(
      input_dim=VOCAB_SIZE,
      output_dim=32
   )
)

model.add(
   LSTM(
      units = 64

   )
)

model.add(
   Dense(
      units=1,
      activation="sigmoid"
   )
)

# project Architecture 

# Review -> Embedding  -> LSTM 


########################################################
# Step 10 : 
########################################################


model.compile(
   optimizer = "adam" 
   loss = "binary_crossentropy",
   matrices =  
)


print("Model training")

model.fit(
   X_train_padded,
   y_train,
   epochs = 3,
   batch_size = 64,
   validation_split = 0.2

)

########################################################
#step 12 : Evaluate the model
########################################################


model.evaluate(
   X_test_padded,
   y_test
   varbose = 0

)

print("Testing accuricy :",accuracy)


##########################################################
# step 13 :
##########################################################

#########################################################
# step 14 : Get 
######################################################## 


actual_value = Y_test[12]

if actual_value = 1:
 actual_sentimant = "POSITIVE"
else
actual_sentiment =  ""


###################################################
# step 15 : predict the sentiment
###################################################

prection = model.predict(
   review _for_predict
)

















