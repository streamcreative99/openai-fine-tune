import streamlit as st
from langchain.llms import OpenAI

# App title
st.title('SC Starter Kit App')

# Check for OpenAI API Key in Streamlit's secrets
if 'OPENAI_API_KEY' in st.secrets:
    st.sidebar.success('API key successfully loaded from secrets!', icon='✅')
    openai_api_key = st.secrets['OPENAI_API_KEY']
else:
    openai_api_key = st.sidebar.text_input('Enter OpenAI API Key:', type='password')
    if not openai_api_key.startswith('sk-'):
        st.sidebar.warning('Please enter your OpenAI API key!', icon='⚠')

def generate_response(input_text):
    llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
    st.info(llm(input_text))

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
