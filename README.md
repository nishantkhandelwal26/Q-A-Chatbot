# Q&A Chatbot with Gemini

A simple and interactive Q&A chatbot built using Streamlit, LangChain, and Google Gemini API.

# Deployed On

[Q&A Chatbot Demo](https://q-a-chatbot-nishant.streamlit.app/)

## Features

- Multiple Gemini model support
- Adjustable LLM parameters
- Streamlit-based UI
- LangChain prompt chaining
- LangSmith tracing integration
- Secure API key input from sidebar

---

## Tech Stack

- Python
- Streamlit
- LangChain
- Google Gemini API
- LangSmith
- dotenv

---

## Project Structure

```bash
├── app.py
├── .env
├── requirements.txt
└── README.md
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nishantkhandelwal26/Q-A-Chatbot.git
```

### 2. Create Virtual Environment

```bash
python -m venv venv
```

Activate the environment:

#### Windows

```bash
venv\Scripts\activate
```

#### Mac/Linux

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file in the root directory:

```env
LANGCHAIN_API_KEY=your_langsmith_api_key
```

You will provide the Gemini API key directly in the Streamlit sidebar while running the app.

---

## Running the Application

```bash
streamlit run app.py
```

---

## Supported Models

- `gemini-3.1-flash-lite`
- `gemini-2.5-flash-lite`
- `gemini-2.5-flash`
- `gemini-3.1-flash-lite-preview`
- `gemini-2.5-pro`

---

## How It Works

1. User enters their Google Gemini API key in the sidebar
2. User selects the desired Gemini model
3. User adjusts temperature and max tokens
4. User asks a question
5. LangChain creates a prompt chain
6. Gemini generates the response
7. Output is displayed in the Streamlit app

---

## Example requirements.txt

```txt
streamlit
langchain
langchain-google-genai
langchain-core
python-dotenv
```

---

## Author

Built by Nishant Khandelwal using LangChain and Gemini AI.