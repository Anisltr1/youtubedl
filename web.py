import streamlit as st
from pytube import YouTube
import os
import base64

# Set page title and favicon
st.set_page_config(page_title='YouTube Video Downloader', page_icon=':arrow_down:')

# Set page header
st.title('YouTube Video Downloader')

# Get YouTube video URL from user input
url = st.text_input('Enter the YouTube video URL:', '')

# Create a selectbox for choosing between MP4 and MP3
file_format = st.selectbox('Select the file format:', ['MP4', 'MP3'])

# Download YouTube video when user clicks the 'Download' button
if st.button('Download'):
    # Create a YouTube object with the URL
    yt = YouTube(url)

    # Get the stream with the highest resolution
    stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

    # Set the file extension based on the chosen file format
    file_ext = 'mp4' if file_format == 'MP4' else 'mp3'

    # Download the video or audio
    if file_format == 'MP4':
        # Download the video
        filename = stream.download()
    else:
        # Download the audio directly if it exists
        audio_stream = yt.streams.filter(only_audio=True).first()
        if audio_stream is not None:
            filename = audio_stream.download()
        else:
            st.error('Error: This video does not have an audio stream that can be downloaded in MP3 format.')
            st.stop()

    # Load the file contents
    with open(filename, 'rb') as f:
        file_contents = f.read()

    # Encode the file contents as base64
    encoded_file = base64.b64encode(file_contents).decode()

    # Construct the href link with the base64-encoded file and the suggested filename
    href = f'<a href="data:application/octet-stream;base64,{encoded_file}" download="{yt.title}.{file_ext}">Download {file_format}</a>'

    # Show success message with the download link
    st.success(f'{file_format} downloaded successfully! Click the link below to download.')
    st.markdown(href, unsafe_allow_html=True)

