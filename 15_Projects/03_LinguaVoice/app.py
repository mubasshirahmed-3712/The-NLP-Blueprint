# ===========================================
# 🌍 LinguaVoice: Translate & Speak
# Break language barriers with instant translation and natural voice output
# By Mubasshir Ahmed 🚀
# ===========================================

import streamlit as st
import pandas as pd
import os
import base64
from mtranslate import translate
from gtts import gTTS
from pydub import AudioSegment

# ---------------------------
# App Config
# ---------------------------
st.set_page_config(page_title="LinguaVoice: Translate & Speak", layout="wide")
st.title("🌍 LinguaVoice: Translate & Speak")
st.write("Break language barriers with instant translation and natural voice output.")

# ---------------------------
# Load Language Dataset
# ---------------------------
try:
    df = pd.read_csv("data/language.csv")
    df.dropna(inplace=True)
    lang = df["name"].to_list()
    langlist = tuple(lang)
    langcode = df["iso"].to_list()
    lang_array = {lang[i]: langcode[i] for i in range(len(langcode))}
except Exception as e:
    st.error("⚠️ Language dataset not found. Please check `data/language.csv`.")
    st.stop()

# ---------------------------
# Input Section
# ---------------------------
st.subheader("📌 Enter Your Text")
inputtext = st.text_area("Type or paste text to translate:", height=100)

# ---------------------------
# Sidebar Options
# ---------------------------
st.sidebar.header("⚙️ Translation Settings")
choice = st.sidebar.radio("🎯 Select Output Language", langlist)
voice_choice = st.sidebar.radio("🗣️ Choose Voice", ("Female", "Male"))
speed_choice = st.sidebar.radio("⚡ Select Speed", ("Normal", "Slow", "Fast"))

st.sidebar.markdown("---")
st.sidebar.markdown("👨‍💻 **By Mubasshir Ahmed** 🚀")

# ---------------------------
# Utility: File Download
# ---------------------------
def get_binary_file_download_html(bin_file, file_label="File"):
    with open(bin_file, "rb") as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">📥 Download {file_label}</a>'
    return href

# ---------------------------
# Processing
# ---------------------------
if len(inputtext) > 0:
    try:
        # Translate
        output = translate(inputtext, lang_array[choice])

        c1, c2 = st.columns([3, 3])

        with c1:
            st.subheader("✅ Translated Text")
            st.text_area("Translation Result:", output, height=200)

            # Save translated text
            with open("translated.txt", "w", encoding="utf-8") as f:
                f.write(output)
            st.markdown(get_binary_file_download_html("translated.txt", "Translated Text"), unsafe_allow_html=True)

        with c2:
            st.subheader("🔊 Voice Output")

            # Convert text to speech
            tts = gTTS(text=output, lang=lang_array[choice], slow=(speed_choice == "Slow"))
            tts.save("lang.mp3")

            # Load audio
            sound = AudioSegment.from_file("lang.mp3", format="mp3")

            # Male voice (lower pitch)
            if voice_choice == "Male":
                sound = sound._spawn(sound.raw_data, overrides={
                    "frame_rate": int(sound.frame_rate * 0.8)
                }).set_frame_rate(sound.frame_rate)

            # Speed adjustments
            if speed_choice == "Fast":
                sound = sound.speedup(playback_speed=1.25)
            elif speed_choice == "Slow":
                sound = sound.speedup(playback_speed=0.85)

            # Export final audio
            sound.export("final_lang.mp3", format="mp3")

            # Play in Streamlit
            with open("final_lang.mp3", "rb") as f:
                st.audio(f.read(), format="audio/mp3")

            # Download option
            st.markdown(get_binary_file_download_html("final_lang.mp3", "Audio File"), unsafe_allow_html=True)

    except Exception as e:
        st.error(f"⚠️ Error: {e}")

# ---------------------------
# Footer
# ---------------------------
st.success("✅ Processing Completed!")
st.markdown(
    """
    ---
    🌍 **LinguaVoice v1.0**  
    👨‍💻 Built with ❤️ by *Mubasshir Ahmed* 🚀  
    """
)
