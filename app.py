import streamlit as st
import pandas as pd
import vertexai
from vertexai.generative_models import GenerativeModel, Part, ChatSession, GenerationConfig

def get_chat_response(chat: ChatSession, prompt: str, context) -> str:
    response = chat.send_message([context, prompt], generation_config=GenerationConfig(
                temperature=0.1,
                top_p=0.95,
                # top_k=20,
                candidate_count=1,
                # max_output_tokens=100,
                stop_sequences=["STOP!"],
            ))
    return response.text

PROJECT_ID = "pacific-legend-435014-q7"

st.title("Document QnA")
st.write("Uses Vertex AI Gemini LLM for document QnA | Deployed as a Streamlit application hosted on Google Cloud Platform.")


vertexai.init(project=PROJECT_ID, location="europe-west3")

model = GenerativeModel("gemini-1.5-pro") 
st.session_state['context'] = None


## File Uploader and Summarizer
file = st.file_uploader("Upload File", type=['xlsx']) #'txt','csv','xlsx'

if file is not None:
    with st.spinner('Loading and creating context'):
        
        df = pd.read_excel(file)
        st.write(df.head())
        context = df.to_string()
        st.session_state['context'] = context




### Initialize a Chat session
chat = model.start_chat()

response = ""
# prompts = []
# responses = []

### Chat session
if st.session_state['context'] is not None:
    with st.form(key="Chat_form"):

        prompt = st.text_input("Enter a prompt:")
        # prompts.append(prompt)

        submit_button = st.form_submit_button(label="Generate")

        if submit_button:
            
            with st.spinner('Generating response, Please Wait'):

                # response = model.generate_content( [st.session_state['context'], prompt])
                response = get_chat_response(chat, prompt, context)
                #response = response.text
                # responses.append(response)

            if 'results' not in st.session_state:
                st.session_state.results = {}

            st.session_state.results.update({prompt:response})

if 'results' in st.session_state: 
    for query,result in st.session_state.results.items():
        st.write("User Prompt:")
        st.text(query)
        st.write("Response:")
        st.text(result)

###
