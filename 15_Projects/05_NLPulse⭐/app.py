# ================================================
# ⚡ NLPulse - Advanced NLP Analytics & Visualization
# Capture the pulse of language with intelligent NLP
# By Mubasshir Ahmed 🚀
# ================================================

from flask import Flask, request, jsonify, render_template, send_from_directory
import nltk
from nltk.tokenize import (
    word_tokenize, sent_tokenize,
    WhitespaceTokenizer, BlanklineTokenizer
)
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk.util import ngrams
from nltk.corpus import stopwords
from nltk import pos_tag, ne_chunk, RegexpParser
from collections import Counter
import os

# ---------------------------
# Summarization (Gensim fallback)
# ---------------------------
try:
    from gensim.summarization import summarize
except ImportError:
    def summarize(text, word_count=50):
        """Simple fallback summarizer"""
        sentences = text.split('.')
        return '. '.join(sentences[:3]) + '.' if len(sentences) > 3 else text

# ---------------------------
# Ensure NLTK resources are available
# ---------------------------
import nltk.data
nltk_packages = {
    "tokenizers/punkt": "punkt",
    "corpora/wordnet": "wordnet",
    "corpora/stopwords": "stopwords",
    "taggers/averaged_perceptron_tagger": "averaged_perceptron_tagger",
    "chunkers/maxent_ne_chunker": "maxent_ne_chunker",
    "corpora/words": "words",
}

for path, pkg in nltk_packages.items():
    try:
        nltk.data.find(path)
    except LookupError:
        nltk.download(pkg, quiet=True)

# ---------------------------
# Flask App
# ---------------------------
app = Flask(__name__)

@app.route("/")
def index():
    """Serve the NLPulse homepage"""
    return render_template("index.html")

@app.route("/static/<path:filename>")
def static_files(filename):
    """Serve static files like CSS/JS"""
    return send_from_directory("static", filename)

@app.route("/process", methods=["POST"])
def process_text():
    """Main NLP pipeline endpoint"""
    try:
        data = request.json
        text = data.get("text", "")
        token_type = data.get("token_type", "word")
        stemmer_choice = data.get("stemmer", "None")
        lemmatize = data.get("lemmatize", False)
        ngram_n = data.get("ngram_n", 2)
        remove_stopwords = data.get("remove_stopwords", False)
        summarize_text = data.get("summarize", False)

        if not text.strip():
            return jsonify({"error": "Please provide text to analyze"}), 400

        # ----------------- Tokenization -----------------
        try:
            if token_type == "word":
                tokens = word_tokenize(text)
            elif token_type == "sentence":
                tokens = sent_tokenize(text)
            elif token_type == "whitespace":
                tokens = WhitespaceTokenizer().tokenize(text)
            else:
                tokens = BlanklineTokenizer().tokenize(text)
        except Exception:
            tokens = text.split()

        # ----------------- Stemming -----------------
        stemmed = []
        try:
            if stemmer_choice != "None":
                if stemmer_choice == "Porter":
                    stemmed = [PorterStemmer().stem(w) for w in word_tokenize(text)]
                elif stemmer_choice == "Lancaster":
                    stemmed = [LancasterStemmer().stem(w) for w in word_tokenize(text)]
                elif stemmer_choice == "Snowball":
                    stemmed = [SnowballStemmer("english").stem(w) for w in word_tokenize(text)]
        except Exception:
            stemmed = []

        # ----------------- Lemmatization -----------------
        lemmatized = []
        try:
            if lemmatize:
                lemmatizer = WordNetLemmatizer()
                lemmatized = [lemmatizer.lemmatize(w) for w in word_tokenize(text)]
        except Exception:
            lemmatized = []

        # ----------------- Stopword Removal -----------------
        filtered = []
        try:
            if remove_stopwords:
                stop_words = set(stopwords.words('english'))
                filtered = [w for w in word_tokenize(text) if w.lower() not in stop_words]
        except Exception:
            filtered = []

        # ----------------- N-Grams -----------------
        ngrams_list = []
        try:
            if ngram_n > 1:
                ngrams_list = [" ".join(gram) for gram in ngrams(word_tokenize(text), ngram_n)]
        except Exception:
            ngrams_list = []

        # ----------------- POS & NER -----------------
        pos_tags, ner = [], []
        try:
            pos_tags = pos_tag(word_tokenize(text))
            ner_tree = ne_chunk(pos_tags)
            ner = [(subtree.label(), " ".join(c[0] for c in subtree)) 
                   for subtree in ner_tree if hasattr(subtree, "label")]
        except Exception:
            pos_tags, ner = [], []

        # ----------------- Chunking -----------------
        chunks = []
        try:
            grammar = "NP: {<DT>?<JJ>*<NN.*>+}"
            cp = RegexpParser(grammar)
            tree = cp.parse(pos_tags)
            chunks = [" ".join([token for token, pos in subtree.leaves()]) 
                      for subtree in tree.subtrees() if subtree.label() == "NP"]
        except Exception:
            chunks = []

        # ----------------- Word Frequency -----------------
        try:
            freq = dict(Counter(word_tokenize(text)))
        except Exception:
            freq = {}

        # ----------------- Summarization -----------------
        summary = ""
        try:
            if summarize_text:
                summary = summarize(text, word_count=50)
        except Exception:
            summary = "Text too short for summarization or summarization failed."

        return jsonify({
            "tokens": tokens,
            "stemmed": stemmed,
            "lemmatized": lemmatized,
            "filtered": filtered,
            "ngrams": ngrams_list,
            "pos_tags": pos_tags,
            "ner": ner,
            "chunks": chunks,
            "frequency": freq,
            "summary": summary,
        })

    except Exception as e:
        return jsonify({"error": f"Processing error: {str(e)}"}), 500


if __name__ == "__main__":
    print("⚡ NLPulse is running at http://127.0.0.1:5000 🚀")
    app.run(debug=True)
