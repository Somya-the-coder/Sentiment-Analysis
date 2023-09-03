import streamlit as st
from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

# Streamlit UI
st.title("Sentiment Analysis App")
text = st.text_area("Enter text for sentiment analysis:")
if st.button("Analyze"):
    if text:
        results = sentiment_analyzer(text)
        sentiment = results[0]['label']
        score = results[0]['score']
        st.write(f"Sentiment: {sentiment}")
