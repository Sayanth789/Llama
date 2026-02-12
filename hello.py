import time
import ollama 

print('Loading..')

start = time.time()

response = ollama.chat(
    model='llama3:8b',
    messages=[{'role': 'user', 'content': 'Say Hello'}],
    stream=False
)
end = time.time()

print("Time taken:", end - start)
print(response['message']['content'])