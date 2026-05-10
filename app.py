import streamlit as st
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

import os
from dotenv import load_dotenv
load_dotenv()


# langsmith tracking
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_PROJECT"] = "Q&A Chatbot with Gemini"

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user's question to the best of your ability."),
        ("user", "Question: {question}")
    ]
)


def generate_response(question, api_key, llm, temperature, max_tokens):
    llm = ChatGoogleGenerativeAI(model=llm, google_api_key=api_key, temperature=temperature, max_tokens=max_tokens)
    output_parser = StrOutputParser()
    chain = prompt | llm | output_parser
    answer = chain.invoke({'question': question})
    return answer


st.title("Q&A Chatbot with Gemini")
st.sidebar.title("Settings")
api_key = text_input = st.sidebar.text_input("Google API Key", type="password")

llm = st.sidebar.selectbox(
    "Select LLM", ["gemini-3.1-flash-lite", "gemini-2.5-flash-lite", "gemini-2.5-flash", "gemini-3.1-flash-lite-preview", "gemini-2.5-pro"])
temperature = st.sidebar.slider("Temperature", 0.0, 1.0, 0.7)
max_tokens = st.sidebar.slider("Max Tokens", 50, 100000, 200)

question = st.text_input("Enter your question:")
if st.button("Get Answer"):
    if not api_key:
        st.error("Please enter your Google API Key in the sidebar.")
    else:
        with st.spinner("Generating answer..."):
            answer = generate_response(
                question, api_key, llm, temperature, max_tokens)
            st.write("Answer:", answer)

# st.markdown("---")
# st.markdown(
#     "Made with ❤️ using [Langchain](https://python.langchain.com/) and [Streamlit](https://streamlit.io/).")
