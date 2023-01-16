# 🤖 Django Chatbot Server 📡

This is a Django-based chatbot server that _takes user queries_ and routes them to the appropriate `NLP Model` for handling and _generating response_.

## Features

- Takes user queries and routes them to the appropriate model
- Simple `GET` and `POST` request API
- Saves user queries and answer in the `sqlite` database for further analysis

## Getting Started

### Prerequisites

- Python 3.x
- Django

### Installation

1. Clone the repository using SSH : `git@github.com:HeadlessTech/mujib-jiggyasa-bot-server.git`
2. Install the dependencies: `pip install -r requirements.txt`

### Running the Server

1. Run migrations: `python manage.py migrate`
2. Start the server: `python manage.py runserver`
3. The server will be running at http://localhost:8000
4. Goto http://localhost:8000/ask_question/ with
    i. `GET `request to get all the queries and answers
    ii. `POST` request ( with qeustion) to get the answer of the question
