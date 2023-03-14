from pytube import YouTube

# Ask user for the YouTube video URL
url = input("Enter the YouTube video URL: ")

# Create a YouTube object with the URL
yt = YouTube(url)

# Get the first stream with the highest resolution
stream = yt.streams.filter(progressive=True).order_by('resolution').desc().first()

# Download the video
stream.download()
print("Video downloaded successfully!")


