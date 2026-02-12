import ollama

response = ollama.chat(
    model='llama3:8b',
    messages=[
        {'role': 'system', 'content': 'Respond only in JSON format.'},
        {'role': 'user', 'content': 'Make a paragrph in the style of shakspeare.'}
    ]
)

print(response['message']['content'])
