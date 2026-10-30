import torch


from transformers import AutoTokenizer
from transformer import AutoModel 

#Pretraind model name
model_name = "distilgpt2"

# Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load Pretrained Languag model
model = AutoModelForCausalU.for_pretrained(model_name)

#input sentance
sentance = " India is my countryx"


#Convert text into pytorch tensor
input = tokenizer(
    sentance,
    return_tensors = "pt"
)


#Extract token ID
token_ids = input["input_ids"]

#Acces the pretraind input embedding layers
embedding_Layer = model.get_input_embeddings()

# Retrive the embedding vectors
embeddings = embedding_layers(token_ids)

print("input sentances :",sentance)

print("Tokens IDs :")
print(token_ids)

print("Embedding shapes :")
print(embedding.shape)

