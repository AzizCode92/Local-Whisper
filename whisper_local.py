import streamlit as st
import subprocess

class Whisper:
    
    _dir_changed = False

    
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