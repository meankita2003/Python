
from ollama import chat

# Select the local LLM
model = "llama3.2"

# Define prompts
prompts = [
    "What is Python?",
    "Explain Machine Learning",
    "What is Artificial Intelligence?"
]

# Display all prompts
for index, prompt in enumerate(prompts, start=1):
    print(index, prompt)

# Execute every prompt
for index, prompt in enumerate(prompts, start=1):
    print("_" * 30)
    print("Prompt number:", index)
    print("Input prompt:", prompt)

    response = chat(
        model=model,
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    print("AI Response:")
    print(response["message"]["content"])
