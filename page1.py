# page1.py
import streamlit as st
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.


import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


def app():
    st.title('Image-Chatter')
    
    os.getenv("google")
    genai.configure(api_key=os.getenv("google"))

    ## Function to load OpenAI model and get respones

    def get_gemini_response(input,image):
        model = genai.GenerativeModel('gemini-pro-vision')
        if input!="":
            response = model.generate_content([input,image])
        else:
            response = model.generate_content(image)
        return response.text

    ##initialize our streamlit app

    

    
    
    uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
    image=""   
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image.", use_column_width=True)

    input=st.text_input("How can you help you",key="input")

    submit=st.button("Answer")

    ## If ask button is clicked

    if submit:
        
        response=get_gemini_response(input,image)
        st.subheader("The Response is")
        st.write(response)
