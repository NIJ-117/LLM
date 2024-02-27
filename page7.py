import streamlit as st

from langchain.llms import CTransformers
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
import os

def app():
    st.title('Local-LLM-Chatter')
    

    # Initialize the language model outside the main function to avoid reloading it on each interaction
    llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q8_0.bin", model_type="llama",
                        config={'max_new_tokens': 128, 'temperature': 0.01})

    template = """
    [INST] <<SYS>>
    You are a helpful, respectful and honest assistant. Your answers are always brief.
    <</SYS>>
    {text}[/INST]
    """

    prompt = PromptTemplate(template=template, input_variables=["text"])

    def get_response(query):
        llm_chain = LLMChain(prompt=prompt, llm=llm)
        response = llm_chain.run(query)
        return response
    
    

    user_input = st.text_input("Ask a question:", "")

    if st.button("Submit"):
        if user_input:
            response = get_response(user_input)
            st.write(response)
        else:
            st.write("Please enter a question.")
