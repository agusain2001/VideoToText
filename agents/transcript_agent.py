from langchain.agents import Tool, initialize_agent
from memory.memory_manager import transcript_memory
from langchain.llms import GoogleGenerativeAI
from tools.youtube_tools import get_youtube_transcript
from config import GEMINI_API_KEY

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

transcript_tool = Tool(
    name="YouTube Transcript Fetcher",
    func=get_youtube_transcript,
    description="Fetches the transcript of a YouTube video."
)



transcript_agent = initialize_agent(
    [transcript_tool],
    llm,
    agent="conversational-react-description",
    memory=transcript_memory,
    verbose=True
)