# home.py
import streamlit as st
from ctransformers import AutoModelForCausalLM




def app():
    st.title('Code-Helper')
    def load_llm():
        # Load your model here
        # This example uses placeholders; replace with your actual model loading code
        llm = AutoModelForCausalLM.from_pretrained("codelamagguf.gguf",
                                                model_type='llama',
                                                max_new_tokens=512,
                                                repetition_penalty=1.13,
                                                temperature=0.1)
        return llm
    llm = load_llm()

    def llm_function(message):
        # Directly generate a response from the model
        response = llm(message)  # This should be adjusted based on how your actual model expects to be called
        output_texts = response  # # Input text box for user
        return output_texts

    user_input = st.text_area("Enter your message:", " what is your query related to coding")

    if st.button('Submit'):
        response = llm_function(user_input)
        # Assuming 'response' is already in a displayable format; adjust if it's not directly displayable
        st.text_area("Response:", response, height=300)
        
        