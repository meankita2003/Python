import torch


from transformers import AutoTokenizer
from transformer import AutoModel 

#Pretraind model name
model_name = "distilgpt2"

# Load Tokenizer 
tokenizer = AutoTokenizer.from_pretrained(model_name)

# Load Pretrained Languag model
model = AutoModelForCausalU.for_pretrained(model_name)

# input prompt
prompt = "ILove"

# Convert input into token ids
input_tensor = "pt"


# Emble evaluation mode 
model.eval()

# perform inference
with torch.no_grad():
    outputts = model(**inputs)

    #Extract logits for final input posuition
    logits = outputs[0,-1,""]
    logits,
dim=-1


values, indices = torch.top(

    probablities,
     5
)

print("input :", prompt)

for value,index in zip(values, indices):
    token = tokinzer.decode([index.item()])
    print(repr                                          )
