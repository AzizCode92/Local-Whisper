import os
import streamlit as st
import ffmpeg
from pydub import AudioSegment
from tempfile import NamedTemporaryFile
from whisper_local import Whisper
from constants import *


st.set_page_config(
    page_title="Whisper.cpp",
    page_icon="musical_note",
    layout="wide",
    initial_sidebar_state="auto",
)

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def to_wav(input_file):
    try:
        y, _ = (
            ffmpeg.input(input_file, threads=0)
            .output("-", format="s16le", acodec="pcm_s16le", ac=1, ar=16000)
            .run(
                cmd=["ffmpeg", "-nostdin"], capture_stdout=True, capture_stderr=True
            )
        )
    except ffmpeg.Error as e:
        raise RuntimeError(f"Failed to load audio: {e.stderr.decode()}") from e
    return y

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def convert_to_wav(audio_file):
    # Convert to WAV format using ffmpeg and pydub
    audio = AudioSegment.from_file(audio_file)
    audio = audio.set_frame_rate(16000)
    with NamedTemporaryFile(delete=False, suffix=".wav") as temp_wav_file:
        temp_wav_file_path = temp_wav_file.name
        audio.export(temp_wav_file_path, format="wav")
    return temp_wav_file_path

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def download_model(model_type):
    model_path = os.path.join(MODEL_PATH, f"ggml-{model_type}.bin")
    if not os.path.exists(model_path):
        Whisper._run_command(f"./whisper-cpp/models/download-ggml-model.sh {model_type}")
    else:
        st.success(f"Model {model_type} already exists")
    return model_path

@st.cache(persist=True,allow_output_mutation=False,show_spinner=True,suppress_st_warning=True)
def display_transcript(temp_wav_file_path):
    with open(f"{temp_wav_file_path}.txt", 'r') as text_file:
        transcript_text = text_file.read()
        st.subheader("Transcript Text")
        st.code(transcript_text, language="text")



st.title("Local Whisper")
st.info('✨ Supports all popular audio formats - WAV, MP3, MP4, OGG, WMA, AAC, FLAC, FLV 😉')
st.text("First upload your audio file and then select the model type. \nThen click on the button to transcribe the text in the audio.")
uploaded_file = st.file_uploader("Upload audio file", type=["wav","mp3","ogg","wma","aac","flac","mp4","flv"])

if uploaded_file is not None:
    # Convert to WAV format using ffmpeg and pydub
    temp_wav_file_path = convert_to_wav(uploaded_file)
    st.success("Converted to WAV format!")
    st.markdown("---")
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("Feel free to play your uploaded audio file 🎼")
        # Play the converted WAV file
        st.audio(temp_wav_file_path, format="audio/*")
    
    with col2:
        whisper_model_type = st.radio("Please choose your model type", AVAILABLE_MODELS)
        if not os.path.exists(os.path.join(MODEL_PATH, f"ggml-{whisper_model_type}.bin")):
            whisper_model_path = download_model(whisper_model_type)
        else:
            st.success(f"Model {whisper_model_type} already exists")
    

    if st.button("Generate Transcript"):
        with st.spinner(f"Generating Transcript... 💫"):
            if not os.path.exists(f"{temp_wav_file_path}.txt"):
                Whisper._run_command("make -C whisper-cpp main")
                Whisper._run_command(f"./whisper-cpp/main --language auto --output-txt true -m whisper-cpp/models/ggml-{whisper_model_type}.bin -f {temp_wav_file_path}")
            else:
                with open(f"{temp_wav_file_path}.txt", 'r') as text_file:
                    transcript_text = text_file.read()
                    st.text_area("Transcript Text", transcript_text, height=300)

else:
    st.warning('Please upload your audio file')