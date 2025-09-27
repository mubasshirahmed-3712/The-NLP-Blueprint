# ===========================================
# 🌍 Polyglot Voice: Translate, Read & Visualize
# Your multilingual assistant — detect, translate, speak, and visualize text
# By Mubasshir Ahmed 🚀
# ===========================================

import streamlit as st
import os
import nltk
from gtts import gTTS
from gtts.lang import tts_langs
from langdetect import detect, LangDetectException
from googletrans import Translator
import pycountry
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize

# ---------------------------
# NLTK Downloads
# ---------------------------
nltk.download('punkt')

# ---------------------------
# Streamlit App Config
# ---------------------------
st.set_page_config(page_title="Polyglot Voice", layout="wide")
st.title("🌍 Polyglot Voice: Translate, Read & Visualize")
st.write("Your multilingual assistant — detect, translate, speak, and visualize text.")

# Sidebar branding
st.sidebar.header("⚙️ App Info")
st.sidebar.markdown("👨‍💻 **By Mubasshir Ahmed** 🚀")
st.sidebar.markdown("🔎 *Detect → Translate → Read Aloud → Visualize*")

# ---------------------------
# Utility Functions
# ---------------------------
gtts_languages = tts_langs()
translator = Translator()

def read_aloud(text, language='en'):
    """Convert text to speech and play it."""
    tts = gTTS(text=text, lang=language)
    tts.save("temp.mp3")
    st.audio("temp.mp3", format="audio/mp3")

def get_gtts_lang_code(pycountry_code):
    """Map pycountry code to gTTS supported code."""
    if pycountry_code in gtts_languages:
        return pycountry_code
    mapping = {
        'he': 'iw',       # Hebrew
        'zh-cn': 'zh-CN', # Chinese Simplified
        'zh-tw': 'zh-TW', # Chinese Traditional
    }
    return mapping.get(pycountry_code, 'en')

def generate_wordcloud(text):
    """Generate a word cloud from the given text."""
    if not text.strip():
        return None
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)
    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    plt.tight_layout()
    return fig

def translate_text(text, dest='en'):
    """Translate text to a target language."""
    result = translator.translate(text, dest=dest)
    return result.text

# ---------------------------
# Input Section
# ---------------------------
col1, col2 = st.columns(2)

with col1:
    paragraph = st.text_area("✍️ Enter your paragraph:")

with col2:
    all_languages = [lang.name for lang in pycountry.languages if hasattr(lang, 'name')]
    target_languages_input = st.multiselect("🌐 Select target languages:", all_languages)

# ---------------------------
# Language Detection
# ---------------------------
paragraph_language = None
if paragraph.strip():
    try:
        paragraph_language = detect(paragraph)
        language_name = pycountry.languages.get(alpha_2=paragraph_language).name
        st.info(f"🔍 Detected Language: **{language_name}**")
    except LangDetectException:
        st.warning("⚠️ Language detection failed. Defaulting to English.")
        paragraph_language, language_name = 'en', 'English'
    except Exception:
        st.error("⚠️ Error during language detection. Defaulting to English.")
        paragraph_language, language_name = 'en', 'English'

# ---------------------------
# Translate to English (Universal Language)
# ---------------------------
translated_paragraph = paragraph
if paragraph_language and paragraph_language != 'en':
    try:
        translated_paragraph = translate_text(paragraph, dest='en')
        st.success(f"🌎 Translated to English: {translated_paragraph}")
    except Exception as e:
        st.error(f"⚠️ Translation to English failed: {e}")

# ---------------------------
# Word Cloud Visualization
# ---------------------------
if translated_paragraph.strip():
    try:
        wordcloud_fig = generate_wordcloud(translated_paragraph)
        if wordcloud_fig:
            st.sidebar.subheader("☁️ Word Cloud")
            st.sidebar.pyplot(wordcloud_fig)
    except Exception as e:
        st.error(f"⚠️ Error generating word cloud: {e}")

# ---------------------------
# Buttons
# ---------------------------
if st.button("🔊 Read Original Paragraph"):
    if paragraph.strip():
        read_aloud(paragraph)

if st.button("🌐 Translate & Read Aloud"):
    for lang_name in target_languages_input:
        try:
            lang_code = pycountry.languages.lookup(lang_name).alpha_2
            translated_text = translate_text(paragraph, dest=lang_code)
            st.write(f"✅ **{lang_name} Translation:** {translated_text}")

            # Read aloud in target language
            tts_lang = get_gtts_lang_code(lang_code)
            read_aloud(translated_text, language=tts_lang)
        except Exception as e:
            st.error(f"⚠️ Translation to {lang_name} failed: {e}")

# ---------------------------
# Footer
# ---------------------------
st.markdown(
    """
    ---
    🌍 **Polyglot Voice v1.0**  
    👨‍💻 Built with ❤️ by *Mubasshir Ahmed* 🚀  
    """
)
