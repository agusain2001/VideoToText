from langchain.agents import initialize_agent
from memory.memory_manager import qa_memory
from langchain.llms import GoogleGenerativeAI
from config import GEMINI_API_KEY

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)



qa_agent = initialize_agent(
    [],
    llm,
    agent="conversational-react-description",
    memory=qa_memory,
    verbose=True
)