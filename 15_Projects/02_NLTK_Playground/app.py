# ===========================================
# 📊 NLTK-Playground: Interactive NLP Explorer
# By Mubasshir Ahmed 🚀
# ===========================================

import streamlit as st
import nltk
import re
from nltk.tokenize import (
    word_tokenize, sent_tokenize, blankline_tokenize,
    WhitespaceTokenizer, wordpunct_tokenize
)
from nltk.util import bigrams, trigrams, ngrams
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.corpus import stopwords

# ---------------------------
# Setup (download NLTK data only once)
# ---------------------------
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')

# ---------------------------
# Streamlit App Config
# ---------------------------
st.set_page_config(page_title="NLTK-Playground", layout="wide")
st.title("🧠 NLTK-Playground: Interactive NLP Explorer")
st.write("Learn and explore NLP fundamentals interactively with **NLTK + Streamlit**.")

# ---------------------------
# Input Text
# ---------------------------
st.subheader("📌 Enter Your Text")
text_input = st.text_area(
    "Type or paste your text below:",
    "Natural Language Processing with NLTK is really interesting and fun."
)

# ---------------------------
# Sidebar Options
# ---------------------------
st.sidebar.header("⚙️ NLP Options")

do_tokenize = st.sidebar.checkbox("Tokenization", value=True)
do_stopwords = st.sidebar.checkbox("Remove Stopwords", value=True)
do_pos = st.sidebar.checkbox("Part-of-Speech Tagging", value=True)
do_ngrams = st.sidebar.checkbox("N-Grams", value=True)
do_stemming = st.sidebar.checkbox("Stemming", value=True)
do_lemmatize = st.sidebar.checkbox("Lemmatization", value=True)

st.sidebar.markdown("---")
st.sidebar.markdown("👨‍💻 **By Mubasshir Ahmed** 🚀")

# ---------------------------
# Tokenization
# ---------------------------
if do_tokenize:
    st.subheader("🔤 Tokenization")
    st.write("**Word Tokens:**", word_tokenize(text_input))
    st.write("**Sentence Tokens:**", sent_tokenize(text_input))
    st.write("**Blankline Tokens:**", blankline_tokenize(text_input))
    st.write("**Whitespace Tokens:**", WhitespaceTokenizer().tokenize(text_input))
    st.write("**WordPunct Tokens:**", wordpunct_tokenize(text_input))

# ---------------------------
# Stopword Removal
# ---------------------------
if do_stopwords:
    st.subheader("🚫 Stopword Removal")
    tokens = word_tokenize(text_input)
    stop_words = set(stopwords.words('english'))
    filtered = [w for w in tokens if w.lower() not in stop_words]
    st.write("**Filtered Tokens:**", filtered)

# ---------------------------
# POS Tagging
# ---------------------------
if do_pos:
    st.subheader("🔎 Part-of-Speech (POS) Tagging")
    tokens = word_tokenize(text_input)
    pos_tags = nltk.pos_tag(tokens)
    st.write("**POS Tags:**", pos_tags)

# ---------------------------
# N-Grams
# ---------------------------
if do_ngrams:
    st.subheader("🔗 N-Grams")
    tokens = word_tokenize(text_input)
    st.write("**Bigrams:**", list(bigrams(tokens)))
    st.write("**Trigrams:**", list(trigrams(tokens)))

    n = st.slider("Select N for N-Grams", 2, 10, 4)
    st.write(f"**{n}-Grams:**", list(ngrams(tokens, n)))

# ---------------------------
# Stemming
# ---------------------------
if do_stemming:
    st.subheader("🌱 Stemming")
    words = word_tokenize(text_input)
    pst = PorterStemmer()
    lst = LancasterStemmer()
    sbst = SnowballStemmer("english")

    st.write("**Porter Stemmer:**", [pst.stem(w) for w in words])
    st.write("**Lancaster Stemmer:**", [lst.stem(w) for w in words])
    st.write("**Snowball Stemmer:**", [sbst.stem(w) for w in words])

# ---------------------------
# Lemmatization
# ---------------------------
if do_lemmatize:
    st.subheader("🍃 Lemmatization")
    words = word_tokenize(text_input)
    wordnet_lemmatizer = WordNetLemmatizer()
    lemmatized = [wordnet_lemmatizer.lemmatize(w) for w in words]
    st.write("**WordNet Lemmatizer:**", lemmatized)

# ---------------------------
# Footer
# ---------------------------
st.success("✅ NLP Processing Completed!")
st.markdown(
    """
    ---
    🔥 **NLTK-Playground v1.0**  
    👨‍💻 Built with ❤️ by *Mubasshir Ahmed*  
    """
)
