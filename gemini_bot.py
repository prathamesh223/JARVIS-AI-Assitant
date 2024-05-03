import streamlit as st
import os
import google.generativeai as genai

# Set page title and favicon
st.set_page_config(page_title="JARVIS", page_icon=":robot:")

# Custom CSS for chat messages
st.markdown("""
    <style>
        .chat-container {
            max-width: 800px;
            margin: auto;
            padding: 20px;
            background-color: #f9f9f9;
            border-radius: 10px;
            box-shadow: 0 2px 5px rgba(0, 0, 0, 0.1);
        }
        .chat-message {
            padding: 10px;
            margin: 10px;
            border-radius: 10px;
            box-shadow: 2px 2px 5px rgba(0, 0, 0, 0.1);
            max-width: 70%;
        }
        .assistant-message {
            background-color: #f0f0f0;
            color: #333333;
            align-self: flex-start;
        }
        .user-message {
            background-color: #cceeff;
            color: #333333;
            align-self: flex-end;
        }
    </style>
""", unsafe_allow_html=True)

st.title("JARVIS: The AI Assistant")

os.environ['GOOGLE_API_KEY'] = "AIzaSyAJhZZg0fiBqNCZpRX3zHwKroIEGXXBElY"
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# Select the model
model = genai.GenerativeModel('gemini-pro')

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Ask me Anything"
        }
    ]

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.empty():
        if message["role"] == "assistant":
            st.markdown(f'<div class="chat-message assistant-message">{message["content"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<div class="chat-message user-message">{message["content"]}</div>', unsafe_allow_html=True)

# Process and store Query and Response
def llm_function(query):
    response = model.generate_content(query)

    # Displaying the Assistant Message
    with st.empty():
        st.markdown(f'<div class="chat-message assistant-message">{response.text}</div>', unsafe_allow_html=True)

    # Storing the User Message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": query
        }
    )

    # Storing the Assistant Message
    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response.text
        }
    )

# Accept user input
query = st.text_input("You:", "What's up?")

# Calling the Function when Input is Provided
if st.button("Send"):
    # Displaying the User Message
    with st.empty():
        st.markdown(f'<div class="chat-message user-message">{query}</div>', unsafe_allow_html=True)

    llm_function(query)
