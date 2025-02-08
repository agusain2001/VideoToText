from flask import Flask, request, jsonify
from agents.transcript_agent import transcript_agent
from agents.summary_agent import summary_agent
from agents.qa_agent import qa_agent
from agents.general_agent import general_agent

app = Flask(__name__)

@app.route('/fetch_transcript', methods=['POST'])
def fetch_transcript():
    data = request.json
    video_url = data.get('video_url')
    if not video_url:
        return jsonify({"error": "Please provide a YouTube video URL."}), 400
    transcript = transcript_agent.run(f"Fetch the transcript for this video: {video_url}")
    return jsonify({"transcript": transcript})

@app.route('/summarize_transcript', methods=['POST'])
def summarize_transcript():
    data = request.json
    video_url = data.get('video_url')
    if not video_url:
        return jsonify({"error": "Please provide a YouTube video URL."}), 400
    summary = summary_agent.run(f"Summarize this video: {video_url}")
    return jsonify({"summary": summary})

@app.route('/ask_question', methods=['POST'])
def ask_question():
    data = request.json
    video_url = data.get('video_url')
    question = data.get('question')
    if not video_url or not question:
        return jsonify({"error": "Please provide a YouTube video URL and a question."}), 400
    response = qa_agent.run(f"Answer this question: {question}\n\nVideo: {video_url}")
    return jsonify({"response": response})

@app.route('/general_chat', methods=['POST'])
def general_chat():
    data = request.json
    user_input = data.get('user_input')
    if not user_input:
        return jsonify({"error": "Please provide user input."}), 400
    response = general_agent.run(user_input)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)