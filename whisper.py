import os
import streamlit as st
import subprocess
from constants import MODEL_PATH, AUDIO_PATH

class Whisper:
    def __init__(self, model_name, audio_file):
        self.model_name = model_name
        self.audio_file = audio_file
        self.model_path = os.path.join(MODEL_PATH, model_name)
        self.audio_path = os.path.join(AUDIO_PATH, audio_file)
    
    @classmethod
    def _run_command(cls, args):
        """Run command, transfer stdout/stderr back into Streamlit and manage error"""
        st.info(f"Running '{' '.join(args)} '")
        result = subprocess.run(args, capture_output=True, shell=True)
        try:
            result.check_returncode()
            st.info(result.stdout)
        except subprocess.CalledProcessError as e:
            st.error(result.stderr)
            raise e