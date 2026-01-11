import streamlit as st
import pandas as pd
import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# --- 1. MANDATORY FIRST COMMAND ---
st.set_page_config(page_title="TechLex Chatbot", page_icon="🤖")

# --- 2. DATA LOADING ---
@st.cache_data
def load_data():
    file_path = "Tech_Literacy.csv" 
    if os.path.exists(file_path):
        data = pd.read_csv(file_path)
        data.columns = data.columns.str.strip().str.lower()
        return data.dropna(subset=['question', 'answer'])
    else:
        # Fallback data so the app doesn't crash if CSV is missing
        return pd.DataFrame({
            "question": ["what is ai"], 
            "answer": ["AI is the simulation of human intelligence by machines."]
        })

df = load_data()

# --- 3. BOT LOGIC ---
def get_bot_response(user_query):
    if df.empty:
        return "I'm sorry, my knowledge base is empty."
    
    vectorizer = TfidfVectorizer(stop_words='english')
    questions_list = df['question'].astype(str).tolist()
    all_texts = questions_list + [user_query]
    
    tfidf_matrix = vectorizer.fit_transform(all_texts)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    index = similarity_scores.argmax()
    score = similarity_scores[0][index]
    
    if score > 0.25:
        return df.iloc[index]['answer']
    return "I'm not sure about that. Try asking something else!"

# --- 4. USER INTERFACE ---
st.title("🤖 TechLex: 1-Line Tech Guide")

if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Type your question here..."):
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    response = get_bot_response(prompt)
    
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})