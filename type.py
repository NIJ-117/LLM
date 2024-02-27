import streamlit as st

# Assuming your page functions are defined or imported above
from home import app as home_app
from page1 import app as page1_app
from page2 import app as page2_app
from page5 import app as page5_app
# ... import other pages ...

# Define categories and their pages
CATEGORIES = {
    "Basic Features": {
        "Home": home_app,
        "ImageChatter": page1_app,
        "Chatter": page2_app,
    },
    "Advanced Features": {
        "Chatpdf GEN LLM": page5_app,
        # Add other advanced feature pages here
    }
}

st.sidebar.title('Navigation')

# Let the user select a category
category = st.sidebar.selectbox("Select a category", list(CATEGORIES.keys()))

# Based on the category, let the user select a page
page = st.sidebar.radio("Select a page", list(CATEGORIES[category].keys()))

# Display the selected page
CATEGORIES[category][page]()

# Adding links to the sidebar
st.sidebar.markdown("---")  # Optional: add a visual divider
st.sidebar.markdown("### Useful Links")
st.sidebar.markdown("[OpenAI](https://www.openai.com/)", unsafe_allow_html=True)
st.sidebar.markdown("[Streamlit Documentation](https://docs.streamlit.io/)", unsafe_allow_html=True)
st.sidebar.markdown("[GitHub](https://github.com/)", unsafe_allow_html=True)
