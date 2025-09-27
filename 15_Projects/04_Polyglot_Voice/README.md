# 🌍 Polyglot Voice: Translate, Read & Visualize  

> 🔎 *"Your multilingual assistant — detect, translate, speak, and visualize text."*  

---

## 📌 Project Overview
**Polyglot Voice** is an interactive **Natural Language Understanding (NLU) app** built with **Streamlit**.  
It allows you to:  
- Detect the language of input text  
- Translate into multiple languages  
- Read aloud using **Text-to-Speech (TTS)**  
- Visualize important words with a **Word Cloud**  

This project demonstrates the integration of **translation, speech synthesis, and visualization** in one multilingual assistant.  

---

## 🎯 Features
✅ Automatic **language detection**  
✅ Translate into multiple target languages  
✅ Read aloud with **gTTS (Text-to-Speech)**  
✅ Generate **Word Cloud** for visualization  
✅ Interactive user interface with **Streamlit**  

---

## 📂 Project Structure
```
04_Polyglot_Voice/
├─ output/
│  ├─ Polyglot Voice.pdf       # Demo output (saved from app)
│  └─ temp.mp3                 # Temporary TTS audio file
├─ app.py                      # Main Streamlit application
└─ requirements.txt            # Project dependencies
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/mubasshirahmed-3712/AI-FSDS-progress-journal.git
cd Natural_Language_Processing/15_Projects/04_Polyglot_Voice
```

### 2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 3️⃣ Install FFmpeg (Required for Audio Processing)
- **Windows**
  1. Download [FFmpeg Essentials Build](https://ffmpeg.org/download.html)  
  2. Extract → Example path: `C:\ffmpeg-7.1.1-essentials_build\bin`  
  3. Add this path to **System Environment Variables → PATH**  
  4. Verify in terminal:
     ```bash
     ffmpeg -version
     ffprobe -version
     ```
- **Linux (Debian/Ubuntu)**
  ```bash
  sudo apt-get install ffmpeg
  ```
- **MacOS**
  ```bash
  brew install ffmpeg
  ```

### 4️⃣ Run the App
```bash
streamlit run app.py
```

Then open your browser → `http://localhost:8501`  

---

## 📊 Demo
An example output is available:  
📄 [View Demo (PDF)](./output/Polyglot%20Voice.pdf)  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **Streamlit** → Web app framework  
- **googletrans** → Translation API  
- **langdetect** → Automatic language detection  
- **gTTS** → Google Text-to-Speech  
- **pycountry** → Language code mapping  
- **nltk** → Tokenization  
- **wordcloud + matplotlib** → Visualization  

---

## ✨ Tagline
> *"Polyglot Voice helps you understand, translate, speak, and visualize languages effortlessly."*  

---

## 📌 Author
👤 **Mubasshir Ahmed**  
📧 [https://www.linkedin.com/in/mubasshir3712/]  
🔗 GitHub: [mubasshirahmed-3712](https://github.com/mubasshirahmed-3712)  

---