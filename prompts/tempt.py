import ollama 

response = ollama.chat(
    model='llama3:8b',
    messages=[{'role': 'user', 'content': 'Explain transformers simply'}],
    options={
        'temperature': 0.2   # more deterministic
    }
)


print(response)