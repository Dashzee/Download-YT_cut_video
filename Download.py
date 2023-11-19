from pytube import YouTube

def download_high_resolution_video(url, output_path='.'):
    try:
        # Create a YouTube object
        yt = YouTube(url)

        # Get the highest resolution stream with both audio and video
        video_stream = yt.streams.filter(file_extension='mp4', progressive=True).order_by('resolution').desc().first()

        # Download the video
        print(f'Downloading: {yt.title}')
        video_stream.download(output_path)
        print('Download complete!')

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Example usage:
# Replace 'YOUR_VIDEO_URL' with the actual YouTube video URL
# Specify the output path if you want to save the video in a specific directory
download_high_resolution_video('YOUR_VIDEO_URL', output_path='.')
