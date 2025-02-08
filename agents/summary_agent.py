from langchain.agents import Tool, initialize_agent
from memory.memory_manager import summary_memory
from langchain.llms import GoogleGenerativeAI
from config import GEMINI_API_KEY

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)

summary_tool = Tool(
    name="Text Summarizer",
    func=lambda text: llm(f"Summarize this text: {text}"),
    description="Summarizes text."
)



summary_agent = initialize_agent(
    [summary_tool],
    llm,
    agent="conversational-react-description",
    memory=summary_memory,
    verbose=True
)