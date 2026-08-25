# Mistral LangChain Chatbot

A simple conversational AI chatbot built with **Python, LangChain, and Mistral AI**. The chatbot maintains conversation history using LangChain message objects and provides an interactive terminal-based chat experience.

## Technologies

* Python
* LangChain
* Mistral AI
* `langchain-mistralai`
* Python-dotenv

## Features

* Mistral AI chat model integration
* Conversational message history
* System, user, and AI messages
* Interactive terminal chatbot
* Environment variable support with `.env`

## Model

`mistral-small-2506`

## How It Works

The application sends the complete conversation history to the Mistral model whenever the user enters a new message. This allows the chatbot to maintain context throughout the conversation.

**Note:** Never upload your actual Mistral API key to GitHub. Store it in a `.env` file and add `.env` to `.gitignore`.
