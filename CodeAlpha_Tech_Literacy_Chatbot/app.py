import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 1. THE DATASET (You can add more rows here!)

# --- UPDATED STEP 1: LOAD FROM CSV ---
#try:
#    # This reads the csv file from the same folder as your app.py
#    df = pd.read_csv(r"Tech_Literacy_Chatbot\Tech_Literacy.csv")

#except FileNotFoundError:
#    st.error("Error: 'tech_data.csv' not found. Please make sure the file is in the same folder.")
#    st.stop()

#df = pd.read_csv(r"Tech_Literacy_Chatbot\Tech_Literacy.csv")

# 1. THE DATASET (You can add more rows here!)
data = {
    "question": [
        "What is a computer?",
        "What is Artificial Intelligence (AI)?",
        "How does the internet work?",
        "What is Hardware?",
        "What is Software?",
        "What is the Cloud?",
        "What is a CPU?",
        "What is RAM?",
        "What is an IP address?",
        "What is a Firewall?",
        "What is a computer?",
        "What is Artificial Intelligence (AI)?",
        "How does the internet work?",
        "What is Hardware?",
        "What is the Cloud?",
        "What is a CPU?",
        "What is RAM?",
        "What is a motherboard?",
        "What is the difference between HDD and SSD?",
        "What is a GPU?",
        "What is BIOS?",
        "What is an Operating System?",
        "What is the difference between System and Application software?",
        "What is Open Source software?",
        "What is a Driver?",
        "What is Virtualization?",
        "What is an IP address?",
        "How does DNS work?",
        "What is a Router?",
        "What is the difference between HTTP and HTTPS?",
        "What is a Firewall?",
        "What is a VPN?",
        "What is Machine Learning?",
        "What is a Neural Network?",
        "What is a Large Language Model (LLM)?",
        "What is the Cloud?",
        "What is Blockchain?",
        "What is an API?",
        "What is Malware?",
        "What is Phishing?",
        "What is 2FA (Two-Factor Authentication)?",
        "What is Encryption?",
        "What is DL?",
        "What is CV?"],



   "answer": [ 
       "An electronic device that manipulates data according to a set of instructions.",
        "Technology that allows computers to mimic human intelligence and learn from data.",
        "A global network of billions of computers connected to share information.",
        "The physical parts of a computer you can touch, like the keyboard or CPU.",
        "The programs and instructions that tell a computer what to do.",
        "Servers accessed over the internet for storing data instead of your local drive.",
        "The Central Processing Unit, which acts as the 'brain' of the computer.",
        "Short-term memory used to store data for active tasks quickly.",
        "A unique digital address that identifies a device on a network.",
        "A security system that monitors and controls network traffic to block threats.",
        
        "An electronic device that manipulates information or data, following a set of instructions called software.",
        "Technology that allows computers to mimic human intelligence, such as learning from data and solving problems.",
        "It is a global network of billions of computers connected by cables and wireless signals to share information.",
        "The physical parts of a computer you can touch, like the keyboard, monitor, and internal circuits.",
        "It refers to servers accessed over the internet, allowing you to store and access data without using your local hard drive.",
        "The Central Processing Unit acts as the "brain" of the computer, executing instructions and processing data.",
        "Random Access Memory is short-term storage that allows computers to access data quickly for active tasks.",
        "The main circuit board that connects all computer components like the CPU, memory, and hard drives together.",
        "HDDs use spinning disks to store data, while SSDs use flash memory, making them significantly faster and more durable.",
        "A Graphics Processing Unit is a specialized processor designed to handle images, videos, and complex 3D rendering.",
        "The Basic Input/Output System is software that initializes your hardware and starts the operating system during boot-up.",
        "Software like Windows or macOS that manages computer hardware and allows you to run applications.",
        "System software runs the hardware, while Application software helps users perform specific tasks like browsing or typing.",
        "Software with source code that anyone can inspect, modify, and enhance (e.g., Linux or VLC).",
        "A small piece of software that tells your operating system how to communicate with hardware like printers or cameras.",
        "Technology that allows you to run multiple virtual computers or operating systems on a single physical machine.",
        "A unique string of numbers that identifies a device on a network or the internet, acting like a digital home address.",
        "The Domain Name System acts as the "phonebook" of the internet, converting names like https://www.google.com/search?q=google.com into IP addresses.",
        "A device that directs data traffic between different networks, such as connecting your home devices to the internet.",
        "HTTP is the standard protocol for web data, while HTTPS adds a layer of encryption to keep your data secure.",
        "A security system that monitors and controls incoming and outgoing network traffic based on specific safety rules.",
        "A Virtual Private Network creates a secure, encrypted tunnel for your internet traffic to protect your privacy.",
        "A branch of AI where computers learn from data and improve their performance without being explicitly programmed.",
        "An AI model inspired by the human brain that uses layers of interconnected nodes to recognize complex patterns.",
        "An AI trained on massive amounts of text to understand and generate human-like language (e.g., ChatGPT or Gemini).",
        "On-demand delivery of computing services like storage and processing over the internet instead of a local drive.",
        "A decentralized digital ledger that records transactions across many computers so the record cannot be altered.",
        "An Application Programming Interface is a set of rules that allows two different software programs to talk to each other.",
        "Malicious software (like viruses or spyware) designed to damage, disrupt, or gain unauthorized access to a computer.",
        "A cyber-attack where scammers send fake emails or messages to trick you into revealing sensitive information.",
        "A security process requiring two different forms of identification to access an account for extra protection.",
        "The process of scrambling data into a code so that only people with a "key" can read it.",
        "Deep learning is the subject which deals with the artificial neural netwrok caled neurons.",
        "CV stands for computer vision which deals with the study realed to the analysing the image components".
        ]


}

df = pd.DataFrame(data)

# 2. THE NLP BRAIN
def get_bot_response(user_query):
    # Vectorize the questions using TF-IDF
    vectorizer = TfidfVectorizer(stop_words='english')
    
    # Combine user query with our dataset questions for comparison
    all_questions = df['question'].tolist() + [user_query]
    tfidf_matrix = vectorizer.fit_transform(all_questions)
    
    # Calculate similarity between the user's question (last in matrix) and dataset
    # We compare matrix[-1] (user) against matrix[:-1] (all data questions)
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    
    # Find the index of the highest score
    index = similarity_scores.argmax()
    score = similarity_scores[0][index]
    
    # Threshold: Only answer if similarity is high enough
    if score > 0.3:
        return df.iloc[index]['answer']
    else:
        return "I'm not sure about that technical term. Could you try asking something else like 'What is AI'?"

# 3. THE USER INTERFACE (STREAMLIT)
st.set_page_config(page_title="TechLex Chatbot", page_icon="🤖")
st.title("🤖 TechLex: 1-Line Tech Guide")
st.markdown("Ask simple technical questions and get 1-line answers!")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history from session state
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
if prompt := st.chat_input("Type your question here (e.g., What is RAM?)"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get Response
    response = get_bot_response(prompt)

    # Display bot response
    with st.chat_message("assistant"):
        st.markdown(response)
    st.session_state.messages.append({"role": "assistant", "content": response})