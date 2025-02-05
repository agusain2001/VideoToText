import streamlit as st
import whisper
import tempfile
import os
import yt_dlp
from google.generativeai import configure, generate_content

# Configure Gemini API (Replace with your API Key)
configure(api_key="AIzaSyC03o_q72iVBFOvVktBIRRri67fBv_OrQ4")

# Load Whisper model
model = whisper.load_model("base")

def download_youtube_audio(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': 'temp_audio.%(ext)s',
    }
    
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
        for file in os.listdir():
            if file.startswith("temp_audio"):
                return file
    return None

def transcribe_audio(audio_path):
    result = model.transcribe(audio_path)
    return result['text']

def transcribe_with_gemini(text):
    response = generate_content(model="gemini-pro", prompt=f"Transcribe the following speech: {text}")
    return response.text

st.title("🎙️ Video to Text Transcriber")
option = st.radio("Choose Input Type:", ("YouTube URL", "Upload Video"))

if option == "YouTube URL":
    url = st.text_input("Enter YouTube Video URL:")
    if st.button("Transcribe") and url:
        with st.spinner("Downloading audio..."):
            audio_file = download_youtube_audio(url)
            if audio_file:
                with st.spinner("Transcribing..."):
                    text = transcribe_audio(audio_file)
                    final_text = transcribe_with_gemini(text)
                    st.text_area("Transcript:", final_text, height=300)
                    os.remove(audio_file)
            else:
                st.error("Failed to download audio.")

elif option == "Upload Video":
    uploaded_file = st.file_uploader("Upload a video file", type=["mp4", "avi", "mov"])
    if uploaded_file and st.button("Transcribe"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp4") as temp_file:
            temp_file.write(uploaded_file.read())
            temp_path = temp_file.name
        
        with st.spinner("Transcribing..."):
            text = transcribe_audio(temp_path)
            final_text = transcribe_with_gemini(text)
            st.text_area("Transcript:", final_text, height=300)
        
        os.remove(temp_path)
