from flask import Flask, request, jsonify
from langchain.agents import Tool, initialize_agent
from langchain.memory import ConversationBufferMemory
from langchain.llms import GoogleGenerativeAI
from transcriptAPI import  get_youtube_transcript

# Initialize Flask app
app = Flask(__name__)

# Initialize Gemini LLM
GEMINI_API_KEY = "AIzaSyC03o_q72iVBFOvVktBIRRri67fBv_OrQ4"
llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

# Define the YouTube transcript tool
youtube_tool = Tool(
    name="YouTube Transcript Fetcher",
    func=get_youtube_transcript,
    description="Useful for fetching the transcript of a YouTube video. Input should be a YouTube video URL."
)

# Initialize memory for the conversation
memory = ConversationBufferMemory()

# Initialize the agent with tools and memory
tools = [youtube_tool]
agent = initialize_agent(
    tools,
    llm,
    agent="conversational-react-description",
    memory=memory,
    verbose=True
)

# Endpoint to fetch and store YouTube transcript
@app.route('/fetch_transcript', methods=['POST'])
def fetch_transcript():
    data = request.json
    video_url = data.get('video_url')
    if not video_url:
        return jsonify({"error": "Please provide a YouTube video URL."}), 400
    
    # Fetch the transcript
    transcript = get_youtube_transcript(video_url)
    
    # Store the transcript in memory
    memory.chat_memory.add_user_message(f"YouTube video: {video_url}")
    memory.chat_memory.add_ai_message(f"Transcript: {transcript}")
    
    return jsonify({"message": "Transcript fetched and stored in memory.", "transcript": transcript})

# Endpoint to chat with the AI agent
@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_input = data.get('user_input')
    if not user_input:
        return jsonify({"error": "Please provide user input."}), 400
    
    # Get the AI's response
    response = agent.run(user_input)
    
    return jsonify({"response": response})

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)