from ollama import chat

#select the local LLM
model = "llama3.2:lb"

# define prompts
prompt = [
    "Explain recursion",
    "Explain recursion in python in 3 simple points",
    """ you are experienced gython teacher
    Explain recursion forbeginner
    Give one simple example."""
    """Convert programming language to uppercase.
    Example  1:
    Input: python
    output: PYTHON

    Example 2:
    Input: java
    Output: JAVA
     
    Input: javascript
    output: """
]

# Execute every prompt 
for index, prompt in enumerate(prompts, start=1):
    print("_"*30)
    print("prompt number : ", index)
    print("input prompt :",prompt)

    response = chat(
        model = model,
        message = [
            {
                "role": "user"
            }

        ]
        
    )
