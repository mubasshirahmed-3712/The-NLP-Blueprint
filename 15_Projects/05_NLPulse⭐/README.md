# ⚡ NLPulse - Advanced NLP Analytics & Visualization  

<div align="center">

![NLPulse Logo](https://img.shields.io/badge/NLPulse-Interactive%20NLP-blueviolet?style=for-the-badge&logo=python&logoColor=white)

**Capture the pulse of language with intelligent NLP processing, interactive visualizations, and automatic summarization**  

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://python.org)  
[![Flask](https://img.shields.io/badge/Flask-2.3.3-teal.svg)](https://flask.palletsprojects.com/)  
[![NLTK](https://img.shields.io/badge/NLTK-3.8.1-orange.svg)](https://nltk.org)  
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)  

[Demo](#demo) • [Features](#features) • [Installation](#installation) • [Usage](#usage) • [Tech Stack](#tech-stack) • [Contributing](#contributing)

</div>  

---

## 🌟 Features  

### 📝 **Text Processing**
- Tokenization: Word, sentence, whitespace, and blankline tokenization  
- Stemming: Porter, Lancaster, and Snowball stemmers  
- Lemmatization: WordNet-based root word extraction  
- Stopwords Removal: Filter out common English stopwords  
- N-Grams: Configurable n-gram generation (1–5)  

### 🔍 **Linguistic Analysis**
- POS Tagging for grammatical structure  
- Named Entity Recognition (NER): Detect people, organizations, locations  
- Noun Phrase Chunking for syntactic insights  
- Word Frequency Analysis with statistical counts  

### 📊 **Visualizations**
- Custom **Canvas-based Word Clouds**  
- Interactive **Chart.js frequency graphs**  
- Real-time result updates  
- Mobile-friendly responsive UI  

### 🎯 **Advanced**
- Automatic **Text Summarization** (Gensim-based)  
- **Modern UI** with branded theme (NLPulse)  
- Error handling and performance optimization  

---

## 🚀 Quick Start  

### Prerequisites
- Python 3.7+  
- pip package manager  

### Installation  

1. Clone the repository:
```bash
git clone https://github.com/mubasshirahmed-3712/nlpulse.git
cd nlpulse
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
python app.py
```

4. Open in browser:
```
http://localhost:5000
```

---

## 💻 Usage  

### Basic Flow
1. Paste or type text in the input area  
2. Configure tokenization, stemming, etc.  
3. Click **🚀 Analyze with NLPulse**  
4. Explore results across tabs  

### Tabs & Insights
- **🔤 Tokens** → Tokenization output  
- **⚙️ Processing** → Stemming, lemmatization, stopword filtering, n-grams  
- **🔍 Linguistics** → POS tags, NER entities, noun phrase chunks  
- **📈 Insights** → Word cloud & frequency chart  
- **📋 Summary** → Auto text summarization  

---

## 🛠️ Tech Stack  

### Backend  
- Flask – Lightweight API framework  
- NLTK – Core NLP toolkit  
- Gensim – Summarization & topic modeling  
- NumPy / SciPy – Math & processing  

### Frontend  
- HTML5, CSS3 (custom branded theme with your palette)  
- JavaScript – Interactive UX  
- Chart.js – Data visualizations  
- Canvas API – Word cloud rendering  

---

## 📁 Project Structure  

```
NLPulse/
├── app.py             # Flask backend
├── requirements.txt   # Dependencies
├── README.md          # Documentation
├── templates/
│   └── index.html     # UI template
├── static/
│   ├── style.css      # Custom theme
│   └── script.js      # Frontend logic
└── .vscode/
    └── launch.json    # Dev config
```

---

## 🔧 Development  

### Run in Dev Mode  
```bash
export FLASK_ENV=development
export FLASK_DEBUG=1
python app.py
```

### VS Code Setup  
- Open folder in VS Code  
- Install Python extension  
- Run with `F5` or terminal:  
```bash
python app.py
```

---

## 📋 Requirements  

```
Flask==2.3.3
nltk==3.8.1
gensim==4.3.2
numpy==1.24.3
scipy==1.10.1
```

---

## 🎯 Use Cases  

- **Research** → Analyze papers, datasets  
- **Content Analysis** → Blogs, articles, social media  
- **Text Mining** → Extract trends from large corpora  
- **Education** → Learn NLP concepts interactively  
- **Business Intelligence** → Customer feedback & reviews  

---

## 🤝 Contributing  

We welcome contributions 🚀  

1. Fork this repo  
2. Create a branch → `git checkout -b feature/awesome-feature`  
3. Commit → `git commit -m "Added awesome feature"`  
4. Push → `git push origin feature/awesome-feature`  
5. Open a Pull Request  

---

<div align="center">

👨‍💻 **Built with ❤️ by [Mubasshir Ahmed](https://github.com/mubasshirahmed-3712)**  

⭐ Star this repo if you find it helpful ⭐  

</div>  
