# 🎙️ YouTube AI Agent API

This project provides a Flask-based REST API that integrates with Google Gemini AI and YouTube Transcript API. The API allows users to fetch and store YouTube video transcripts and chat with an AI agent, which uses the stored transcript as context.

## Features
- Fetch transcripts of YouTube videos
- Store transcripts in memory for context
- Chat with an AI agent using stored transcripts
- RESTful API design

## Prerequisites
Before running the project, ensure you have:

- A Google Gemini API Key
- Python 3.x installed
- Required Python libraries

### Install dependencies
Run the following command to install the necessary dependencies:
```bash
pip install google-generativeai langchain youtube-transcript-api flask
```

## Project Structure
```
.
├── main.py             # Main Flask application
├── transcriptAPI
├── README.md           # Project documentation
└── requirements.txt   # List of dependencies

```

## API Endpoints

### 1. Fetch YouTube Transcript
**Endpoint:** `POST /fetch_transcript`

**Request Body:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=example"
}
```

**Response:**
```json
{
  "message": "Transcript fetched and stored in memory.",
  "transcript": "Full transcript of the video..."
}
```

### 2. Chat with AI Agent
**Endpoint:** `POST /chat`

**Request Body:**
```json
{
  "user_input": "What is the main topic of the video?"
}
```

**Response:**
```json
{
  "response": "The main topic of the video is..."
}
```

## How to Run the API

1. Clone this repository:
```bash
git clone https://github.com/your-repo/youtube-ai-agent-api.git
cd youtube-ai-agent-api
```

2. Set up your Google Gemini API key:
```python
GEMINI_API_KEY = "your-gemini-api-key"
```

3. Run the Flask application:
```bash
python app.py
```

4. Use tools like Postman or `curl` to test the endpoints.

### Example Usage with `curl`

**Fetch Transcript:**
```bash
curl -X POST http://127.0.0.1:5000/fetch_transcript \
     -H "Content-Type: application/json" \
     -d '{"video_url": "https://www.youtube.com/watch?v=example"}'
```

**Chat with AI Agent:**
```bash
curl -X POST http://127.0.0.1:5000/chat \
     -H "Content-Type: application/json" \
     -d '{"user_input": "What is the main topic of the video?"}'
```

