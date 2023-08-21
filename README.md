# transcribe_podcast

Transcribe-podcast Streamlit Application

# Introduction
Transcribe-podcast is a Minimal Viable Product (MVP) built as a Streamlit application that leverages the capabilities of the Whisper technology to accurately transcribe audio content. Through this web app, users can easily upload audio files, select a Whisper model, and get a transcribed text. This open-source project aims to provide a user-friendly interface for Whisper-CPP, which is a submodule of our Git repository. Please do keep in mind that, being an MVP, the product's primary focus is to demonstrate the core functionality, thus it may be less than perfect. We welcome feedback and contributions for improvement.

## Features

* User-friendly web interface for audio file upload
* Supports transcription in different languages through Whisper models
* Transcribes the audio content and presents the text directly on the interface
* Integrated Whisper-CPP as a submodule
* Full respect for data privacy as everything runs locally; no data is sent to OpenAI



## Prerequisites

Python 3.6 or higher
Streamlit
Whisper-CPP

## Installation

Clone the repository into your local system:
```
git clone --recursive https://github.com/AzizCode92/transcribe_podcast.git
```
The --recursive flag is used to clone the whisper-cpp submodule as well.
Navigate to the project directory and install Python dependencies:
pip install -r requirements.txt
Usage
To run the Streamlit app, use the following command:
```
streamlit run transcribe.py
```
This will start the app in your default browser. Simply select your audio file, select your desired Whisper model, click transcribe, and get your transcribed text.

## Contribution
Your contributions to enrich the functionalities are always welcome. Feel free to propose the changes if they are substantial by opening an issue and discussing it first.

## License
This project is licensed under the MIT license.

## Support
If you encounter issues or have suggestions, please create an issue on GitHub.
