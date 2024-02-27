import streamlit as st
from home import app as home_app
from page1 import app as page1_app
from page2 import app as page2_app

# Importing other apps
from page5 import app as page5_app
from page6 import app as page6_app
from page7 import app as page7_app
from page8 import app as page8_app
from page9 import app as page9_app
from page10 import app as page10_app
from page11 import app as page11_app
from page12 import app as page12_app
from stable import app as stable
# Define categories and their pages

# Dictionary of pages
PAGES = {
    "Home": home_app,
    "ImageChatter": page1_app,
    "Chatter": page2_app,
    # Divider placeholder (will not be used but serves as a visual marker)
    
    "Chatpdf GEN LLM": page5_app,
    
    "Chat with LLAMA 2": page7_app,
    "Chat with CSV LLAMA 2": page8_app,
    
    
    "CodeLLAMA": page11_app,
    
}

CATEGORIES = {
    "Home": {
        "Home": home_app,
    },
    "Basic Features": {
        "ImageChatter": page1_app,
        "Chatter": page2_app,
        "Image-Gen":stable,
    },
    "Advanced Features": {
        "CSV-Helper": page8_app,
        "Invoice OCRLLM": page6_app,
        "Talk-To-PDF": page10_app,
        "Med-Bot": page9_app,
        "Law-Bot": page12_app,
        "Code-Helper": page11_app,
        # Add other advanced feature pages here
    }  
}

st.sidebar.title('Navigation')

# Let the user select a category
category = st.sidebar.selectbox('Select', list(CATEGORIES.keys()))

if category:
    # Check if the selected category is 'Home' and directly call the home_app function
    if category == "Home":
        home_app()
    else:
        # If a category other than 'Home' is selected, show the radio button for page selection
        page = st.sidebar.radio("Select a page", list(CATEGORIES[category].keys()))
        # Display the selected page
        CATEGORIES[category][page]()

# CSS to create a sticky footer in the sidebar
footer = """
    <style>
    .reportview-container .sidebar-content {
        display: flex;
        flex-direction: column;
        height: calc(100vh - 2rem);
    }
    .sidebar-footer {
        margin-top: auto;
    }
    </style>
    <div class="sidebar-footer">
    <hr style="margin:1rem 0;">
    <p style="margin:0;"><b>Useful Links</b></p>
    <a href="https://huggingface.co/TheBloke/Llama-2-13B-GGML" target="_blank">Quantised LLM</a><br>
    <a href="https://openai.com/research/clip" target="_blank">Clip Open AI</a><br>
    <a href="https://github.com/" target="_blank">GitHub</a>
    </div>
"""

st.sidebar.markdown(footer, unsafe_allow_html=True)
