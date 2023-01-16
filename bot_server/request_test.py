import requests

responses = requests.get('http://127.0.0.1:8000/show_queries/')

question = responses.json()[0]['question']
print(question)
print(type(question))