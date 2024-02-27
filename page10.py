# home.py
import streamlit as st

import os
import shutil

from streamlit_chat import message
from langchain.chains import ConversationalRetrievalChain
from langchain.document_loaders import PyPDFLoader, DirectoryLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import CTransformers
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
import os


def app():
    st.title('Talk-To-Pdf')
   


    # Define the target directory where the PDF will be copied
    TARGET_DIR = "llama2pdf"
    def save_uploaded_file(uploaded_file):
        try:
            with open(os.path.join(TARGET_DIR, uploaded_file.name), "wb") as f:
                f.write(uploaded_file.getbuffer())
            return True
        except Exception as e:
            return False

    def delete_file(filename):
        try:
            os.remove(os.path.join(TARGET_DIR, filename))
            return True
        except Exception as e:
            return False

    # Streamlit app layout
    



    
    def conversation_chat(query):
        result = chain({"question": query, "chat_history": st.session_state['history']})
        st.session_state['history'].append((query, result["answer"]))
        return result["answer"]

    def initialize_session_state():
        if 'history' not in st.session_state:
            st.session_state['history'] = []

        if 'generated' not in st.session_state:
            st.session_state['generated'] = ["Hello! Ask me anything about 🤗"]

        if 'past' not in st.session_state:
            st.session_state['past'] = ["Hey! 👋"]

    def display_chat_history():
        reply_container = st.container()
        container = st.container()

        with container:
            with st.form(key='my_form', clear_on_submit=True):
                user_input = st.text_input("Question:", placeholder="ask about the pdf", key='input')
                submit_button = st.form_submit_button(label='Send')

            if submit_button and user_input:
                output = conversation_chat(user_input)

                st.session_state['past'].append(user_input)
                st.session_state['generated'].append(output)

        if st.session_state['generated']:
            with reply_container:
                for i in range(len(st.session_state['generated'])):
                    message(st.session_state["past"][i], is_user=True, key=str(i) + '_user', avatar_style="thumbs")
                    message(st.session_state["generated"][i], key=str(i), avatar_style="fun-emoji")

    currSate=0
    if currSate==0:
        uploaded_file = st.file_uploader("Choose a PDF file", type='pdf')
        if uploaded_file is not None:
            file_details = {"FileName": uploaded_file.name, "FileType": uploaded_file.type, "FileSize": uploaded_file.size}
            st.write(file_details)
            
            # Copy the file to the specified directory
            if st.button('Load the file to database'):
                if save_uploaded_file(uploaded_file):
                    st.success(f"File {uploaded_file.name} successfully loaded.")
                    currSate=1
                    
                else:
                    st.error("File copying failed.")

            # Option to delete the file
            # if st.button('Delete PDF from Target Directory'):
            #     if delete_file(uploaded_file.name):
            #         st.success(f"File {uploaded_file.name} deleted successfully from {TARGET_DIR}.")
            #     else:
            #         st.error("File deletion failed.")

        
    #load the pdf files from the path
    loader = DirectoryLoader('llama2pdf/',glob="*.pdf",loader_cls=PyPDFLoader)
    documents = loader.load()

    #split text into chunks
    text_splitter  = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=50)
    text_chunks = text_splitter.split_documents(documents)

    #create embeddings
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2",
                                    model_kwargs={'device':"cpu"})

    #vectorstore
    vector_store = FAISS.from_documents(text_chunks,embeddings)

    #create llm
    llm = CTransformers(model="llama-2-7b-chat.ggmlv3.q8_0.bin",model_type="llama",
                        config={'max_new_tokens':128,'temperature':0.01})

    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

    chain = ConversationalRetrievalChain.from_llm(llm=llm,chain_type='stuff',
                                                retriever=vector_store.as_retriever(search_kwargs={"k":2}),
                                                memory=memory)


    # Initialize session state
    initialize_session_state()
    # Display chat history
    display_chat_history()

    # Option to delete the file
    if st.button('Delete Vector space '):
        if delete_file(uploaded_file.name):
            st.success(f"File {uploaded_file.name} deleted successfully from {TARGET_DIR}.")
            currSate=0
        else:
            st.error("File deletion failed.")
