import streamlit as st
import openai

# App title
st.title('SC Starter Kit App with Fine-Tuning')

# Check for OpenAI API Key in Streamlit's secrets
if 'OPENAI_API_KEY' in st.secrets:
    st.sidebar.success('API key successfully loaded from secrets!')
    openai_api_key = st.secrets['OPENAI_API_KEY']
else:
    openai_api_key = st.sidebar.text_input('Enter OpenAI API Key:', type='password')
    if not openai_api_key.startswith('sk-'):
        st.sidebar.warning('Please enter your OpenAI API key!')

# File Uploader for Fine-Tuning
uploaded_file = st.sidebar.file_uploader("Upload your training dataset (in .jsonl format)", type="jsonl")

# Fine-Tuning Button
if st.sidebar.button('Start Fine-Tuning'):
    if uploaded_file and openai_api_key.startswith('sk-'):
        # Upload the Dataset to OpenAI
        uploaded = openai.File.create(file=uploaded_file, purpose='fine-tune')
        
        # Start the Fine-Tuning Job
        openai.api_key = openai_api_key
        response = openai.FineTuningJob.create(training_file=uploaded.id, model="gpt-3.5-turbo")
        
        if response:
            st.sidebar.write("Fine-tuning started successfully!")
        else:
            st.sidebar.write("Error starting fine-tuning. Please check your dataset and API key.")
    else:
        st.sidebar.warning("Ensure you've uploaded a dataset and provided a valid API key!")

def generate_response(input_text):
    # Assuming OpenAI() works similar to openai.Completion.create
    response = openai.Completion.create(model="fine-tuned-model-id-if-any", prompt=input_text)
    st.info(response.choices[0].text)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted and openai_api_key.startswith('sk-'):
        generate_response(text)
