import ollama


response = ollama.chat(
    model='llama3:8b',
    messages=[
        {'role': 'system', 'content': 'You are a strict AI professor.'},
        {'role': 'user', 'content': 'Explain transformer simply'}
    ]
)

print(response)