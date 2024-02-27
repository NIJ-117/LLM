# page2.py
import streamlit as st
from dotenv import load_dotenv
import streamlit as st
import os
import pathlib
import textwrap

import google.generativeai as genai

from IPython.display import display
from IPython.display import Markdown
def app():
    st.title('Hey! How can you help you 😊')
    

    load_dotenv() 

     # take environment variables from .env.

    


    def to_markdown(text):
        text = text.replace('•', '  *')
        return Markdown(textwrap.indent(text, '> ', predicate=lambda _: True))

    os.getenv("google")
    genai.configure(api_key=os.getenv("google"))

    ## Function to load OpenAI model and get respones

    def get_gemini_response(question):
        model = genai.GenerativeModel('gemini-pro')
        response = model.generate_content(question)
        return response.text

    ##initialize our streamlit app

    
    

    input=st.text_input("Input: ",key="input")


    submit=st.button("Can you tell ")

    ## If ask button is clicked

    if submit:
        
        response=get_gemini_response(input)
        st.subheader("The Response to your Query is -")
        st.write(response)

