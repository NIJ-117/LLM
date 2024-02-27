# home.py
import streamlit as st

def app():
    import streamlit as st

    # Title of the project
    st.header('GEN-LLM')

    # Section for project contributors
    st.subheader('Project Contributor:')
    contributors = ['Kapil Univara', 'Srikanth Prabhu']
    for contributor in contributors:
        st.write(f"- {contributor}")

    # Section for project capabilities
    st.subheader('The Project we have created has the following Capabilities:')
    capabilities = [
        'Capability to chat with the pdf',
        'Capability to chat with structured data like csv',
        'Capability to chat with the image',
        'Generate the images on the basis of text prompt'
        # Add other capabilities if needed
    ]
    for capability in capabilities:
        st.write(f"- {capability}")

    # Section for customized model
    st.subheader('Make the Customized Model on -')
    models = ['Medical Bot', 'Law Bot', 'Code Bot', 'Invoice Extraction']
    for model in models:
        st.write(f"- {model}")

    # To run the Streamlit app, save this script as `app.py` and
    # in your terminal run: streamlit run app.py
