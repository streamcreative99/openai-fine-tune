import streamlit as st
import openai

# App title
st.title('Wise Old Owl Advice Bot')

# Check for OpenAI API Key in Streamlit's secrets
if 'OPENAI_API_KEY' in st.secrets:
    st.sidebar.success('API key successfully loaded from secrets!')
    openai_api_key = st.secrets['OPENAI_API_KEY']
else:
    openai_api_key = st.sidebar.text_input('Enter OpenAI API Key:', type='password')
    if not openai_api_key.startswith('sk-'):
        st.sidebar.warning('Please enter your OpenAI API key!')

# Using the fine-tuned model to generate responses
def generate_response(input_text, model_name):
    openai.api_key = openai_api_key
    response = openai.Completion.create(
        model=model_name,
        prompt=f"You are a wise old owl giving sage advice.\n{input_text}"
    )
    st.info(response.choices[0].text)

with st.form('my_form'):
    text = st.text_area('Seek advice:', 'How can I find inner peace?')
    submitted = st.form_submit_button('Ask the Wise Old Owl')
    if submitted and openai_api_key.startswith('sk-'):
        # Replace 'your-fine-tuned-model-id' with the ID of your fine-tuned model
        generate_response(text, 'your-fine-tuned-model-id')
