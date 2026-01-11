🤖 TechLex: 1-Line Tech Guide

TechLex is a lightweight, AI-powered chatbot designed to provide instant, one-line definitions for technical terms. It uses Natural Language Processing (NLP) to match user queries with a knowledge base stored in a CSV file.

🚀 Features
*Simple UI:* Built with Streamlit for a clean, chat-like experience.
*NLP Matching:* Uses TF-IDF Vectorization and Cosine Similarity to find the best answer, even if the user doesn't type the question exactly as stored.
*Persistent Chat:* Maintains session history during your visit.
*Easy to Update:* Simply add new rows to the `Tech_Literacy.csv` file to expand the bot's knowledge.

 🛠️ Tech Stack
*Frontend:* Streamlit
*Data Handling:* Pandas
*NLP Machine Learning:* Scikit-learn (TfidfVectorizer & Cosine Similarity)

 📂 Project Structure
text
├── app.py                
├── Tech_Literacy.csv     
├── requirements.txt      
└── README.md         

📊 How it Works
The bot doesn't just look for keywords; it converts text into numerical vectors.

When you ask a question:

It calculates the TF-IDF (Term Frequency-Inverse Document Frequency) of your input.

It compares that "vector" against all questions in the CSV using Cosine Similarity.

If the similarity score is above 0.25, it returns the corresponding answer.