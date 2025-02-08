# YouTube AI Agent

## 📌 Project Overview
This project is a **Flask-based REST API** that leverages **multiple AI agents** to interact with YouTube videos. The agents use **LangChain**, **Google Gemini AI**, and **YouTube Transcript API** to fetch transcripts, summarize content, answer questions, and enable general conversations.

## 🚀 Features
- **Fetch YouTube Video Transcripts**
- **Summarize Transcripts**
- **Answer Questions Based on Transcripts**
- **General AI Conversations**
- **Memory Management for Contextual Responses**

## 📂 Project Structure
```
youtube_ai_agent/
│
├── agents/                  # AI Agents for different tasks
│   ├── __init__.py          
│   ├── transcript_agent.py  # Fetch YouTube transcripts
│   ├── summary_agent.py     # Summarize transcripts
│   ├── qa_agent.py          # Answer questions based on transcript
│   └── general_agent.py     # General chatbot agent
│
├── tools/                   # Utility functions
│   ├── __init__.py          
│   └── youtube_tools.py     # Fetch transcript from YouTube
│
├── memory/                  # Memory management for agents
│   ├── __init__.py          
│   └── memory_manager.py    # Handles memory for all agents
│
├── api/                     # API implementation using Flask
│   ├── __init__.py          
│   └── app.py               # API endpoints
│
├── config/                  # Configuration files
│   ├── __init__.py          
│   └── settings.py          # API keys and settings
│
├── tests/                   # Unit tests for agents
│   ├── __init__.py          
│   ├── test_transcript_agent.py
│   ├── test_summary_agent.py
│   ├── test_qa_agent.py
│   └── test_general_agent.py
│
├── requirements.txt         # Dependencies
└── README.md                # Project documentation
```

## 🔍 How It Works
### 1️⃣ Fetching a YouTube Transcript
- The **Transcript Agent** extracts the transcript from a YouTube video.
- Uses **YouTube Transcript API** to fetch text from the video.

### 2️⃣ Summarizing the Transcript
- The **Summary Agent** takes the transcript and provides a concise summary.
- Uses **Google Gemini AI** to process and summarize the content.

### 3️⃣ Answering Questions
- The **QA Agent** allows users to ask questions related to the transcript.
- Uses **LangChain memory** to keep context.

### 4️⃣ General AI Chat
- The **General Agent** handles non-video-related conversations.
- Works like a general chatbot using Google Gemini AI.

## 🛠 Installation & Setup
1️⃣ **Clone the repository:**
```bash
git clone https://github.com/agusain2001/VideoToText.git

```

2️⃣ **Install dependencies:**
```bash
pip install -r requirements.txt
```

3️⃣ **Run the API:**
```bash
python api/app.py
```

4️⃣ **Test API using curl or Postman**

## 📡 API Endpoints
### 📍 1. Fetch YouTube Transcript
**Endpoint:**
```http
POST /fetch_transcript
```
**Request Body:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=example"
}
```
**Response:**
```json
{
  "transcript": "Full transcript of the video..."
}
```

### 📍 2. Summarize Transcript
**Endpoint:**
```http
POST /summarize_transcript
```
**Request Body:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=example"
}
```
**Response:**
```json
{
  "summary": "This video is about..."
}
```

### 📍 3. Ask a Question
**Endpoint:**
```http
POST /ask_question
```
**Request Body:**
```json
{
  "video_url": "https://www.youtube.com/watch?v=example",
  "question": "What is the main topic of the video?"
}
```
**Response:**
```json
{
  "response": "The main topic of the video is..."
}
```

### 📍 4. General AI Chat
**Endpoint:**
```http
POST /general_chat
```
**Request Body:**
```json
{
  "user_input": "Tell me a joke!"
}
```
**Response:**
```json
{
  "response": "Why don’t scientists trust atoms? Because they make up everything!"
}
```

