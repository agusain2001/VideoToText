from youtube_transcript_api import YouTubeTranscriptApi

def get_youtube_transcript(video_url: str) -> str:
    """
    Fetches the transcript of a YouTube video.
    """
    try:
        video_id = video_url.split("v=")[1].split("&")[0]  # Extract video ID from URL
        transcript = YouTubeTranscriptApi.get_transcript(video_id)
        transcript_text = " ".join([entry['text'] for entry in transcript])
        return transcript_text
    except Exception as e:
        return f"Error fetching transcript: {str(e)}"