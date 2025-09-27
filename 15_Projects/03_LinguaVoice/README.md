# 🌍 LinguaVoice: Translate & Speak  

> 🔎 *"Break language barriers with instant translation and natural voice output."*  

---

## 📌 Project Overview
**LinguaVoice** is an interactive **Language Translator + Text-to-Speech (TTS)** app built with **Streamlit**.  
It allows you to:  
- Translate text into **100+ languages**  
- Listen to translations in **natural voice (male/female)**  
- Control **speech speed** (normal, slow, fast)  
- Download both **translated text** and **audio files**  

This project demonstrates the power of combining **NLP + Speech Processing** for real-world multilingual communication.  

---

## 🎯 Features
✅ Translate text into multiple languages  
✅ Text-to-Speech with **male/female voice** options  
✅ Speed control (**Normal / Slow / Fast**)  
✅ Downloadable **translated text** and **audio**  
✅ Interactive UI powered by **Streamlit**  

---

## 📂 Project Structure
```
03_LinguaVoice/
├─ data/
│  └─ language.csv                 # Language codes (ISO + names)
├─ output/                          # Sample outputs
│  ├─ final_lang.mp3                # Final processed audio
│  ├─ lang.mp3                      # Raw gTTS audio
│  ├─ LinguaVoice_Translate&Speak.pdf # Demo output
│  └─ translated.txt                # Example text output
└─ app.py                           # Streamlit application
```

---

## ⚙️ Installation & Setup

### 1️⃣ Clone Repository
```bash
git clone https://github.com/mubasshirahmed-3712/AI-FSDS-progress-journal.git
cd Natural_Language_Processing/15_Projects/03_LinguaVoice
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

Then open in browser → `http://localhost:8501`  

---

## 📊 Demo
An example output is available:  
📄 [View Demo (PDF)](./output/LinguaVoice_Translate%20&%20Speak.pdf)  

---

## 🛠️ Tech Stack
- **Python** 🐍  
- **Streamlit** → Web app framework  
- **mtranslate** → Language translation  
- **gTTS** → Google Text-to-Speech  
- **pydub** → Audio processing (pitch, speed)  
- **Pandas** → Language dataset handling  

---

## ✨ Tagline
> *"LinguaVoice helps you translate and speak across languages effortlessly."*  

---

## 📌 Author
👤 **Mubasshir Ahmed**  
📧 [https://www.linkedin.com/in/mubasshir3712/]  
🔗 GitHub: [mubasshirahmed-3712](https://github.com/mubasshirahmed-3712)  

---
