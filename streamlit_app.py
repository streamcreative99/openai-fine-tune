import streamlit as st
import openai
import os

# Set the OpenAI API key
openai.api_key = os.getenv("OPENAI_API_KEY")

# App title
st.title('SC Starter Kit App with Fine-Tuning')

# Check if API key is set (optional but useful for debugging)
if not openai.api_key:
    st.sidebar.warning("OpenAI API key is not set!")
else:
    st.sidebar.success('API key successfully loaded!')

# File Uploader for Fine-Tuning
uploaded_file = st.sidebar.file_uploader("Upload your training dataset (in .jsonl format)", type="jsonl")

# Fine-Tuning Button
if st.sidebar.button('Start Fine-Tuning'):
    if uploaded_file:
        # Upload the Dataset to OpenAI
        uploaded = openai.File.create(file=uploaded_file, purpose='fine-tune')
        
        # Start the Fine-Tuning Job
        response = openai.FineTuningJob.create(training_file=uploaded.id, model="gpt-3.5-turbo")
        
        if response:
            st.sidebar.write("Fine-tuning started successfully!")
        else:
            st.sidebar.write("Error starting fine-tuning. Please check your dataset.")
    else:
        st.sidebar.warning("Ensure you've uploaded a dataset!")

def generate_response(input_text):
    # Assuming OpenAI() works similar to openai.Completion.create
    response = openai.Completion.create(model="fine-tuned-model-id-if-any", prompt=input_text)
    st.info(response.choices[0].text)

with st.form('my_form'):
    text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
    submitted = st.form_submit_button('Submit')
    if submitted:
        generate_response(text)
