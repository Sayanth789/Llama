import ollama

for chunk in ollama.chat(
    model='llama3:8b',
    messages=[{'role': 'user', 'content': 'Explain transformers'}],
    stream=True
):
    print(chunk['message']['content'], end='', flush=True)
