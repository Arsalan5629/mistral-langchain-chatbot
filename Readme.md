# Mistral LangChain Chatbot

A simple conversational AI chatbot built using **Python, LangChain, and Mistral AI**. The chatbot provides an interactive terminal-based conversation experience and maintains the complete conversation history using LangChain message objects.

## Features

* Mistral AI integration
* Built with LangChain
* Conversational memory through message history
* System, Human, and AI messages
* Interactive terminal-based chatbot
* Environment variable support using `.env`

## Technologies Used

* Python
* LangChain
* Mistral AI
* `langchain-mistralai`
* `python-dotenv`

## Mistral Model

```text
mistral-small-2506
```

## Project Structure

```text
mistral-langchain-chatbot/
│
├── chat.py
├── .env
├── .gitignore
├── requirements.txt
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/mistral-langchain-chatbot.git
cd mistral-langchain-chatbot
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it:

### macOS / Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install langchain langchain-mistralai python-dotenv
```

## Environment Variables

Create a `.env` file:

```env
MISTRAL_API_KEY=your_mistral_api_key
```

Then load the API key in Python:

```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")
```

**Never upload your `.env` file or API key to GitHub.**

## Running the Chatbot

Run:

```bash
python chat.py
```

You will see:

```text
----------Welcome to the Chatbot! Type '0' to exit.-----------
You :
```

Type your message and the Mistral model will respond.

To exit the chatbot:

```text
0
```

## How It Works

The chatbot uses LangChain's message classes:

* `SystemMessage` — defines the chatbot's behavior.
* `HumanMessage` — stores the user's messages.
* `AIMessage` — stores the chatbot's responses.

The conversation history is continuously appended to the `messages` list and sent to the Mistral model with each new request.

## Example

```text
----------Welcome to the Chatbot! Type '0' to exit.-----------

You : What is Python?
Bot : Python is a high-level programming language...

You : What is it used for?
Bot : Python is commonly used for web development, AI, data science...

You : 0
```

## Future Improvements

* Add a graphical user interface
* Add streaming responses
* Add persistent chat history
* Add RAG capabilities
* Add document upload
* Add web search
* Deploy the chatbot as an API
* Build a React frontend

## License

This project is for educational and learning purposes.
