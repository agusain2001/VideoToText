from langchain.agents import initialize_agent
from memory.memory_manager import general_memory
from langchain.llms import GoogleGenerativeAI
from config import GEMINI_API_KEY

llm = GoogleGenerativeAI(model="gemini-pro", google_api_key=GEMINI_API_KEY)



general_agent = initialize_agent(
    [],
    llm,
    agent="conversational-react-description",
    memory=general_memory,
    verbose=True
)