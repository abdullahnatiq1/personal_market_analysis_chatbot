import os 
from dotenv import load_dotenv

load_dotenv()

groqAPIKey = os.getenv("GROQ_API_KEY")
modelName = "llama-3.3-70b-versatile"
embeddingModel = "all-MiniLM-L6-v2"
chromaDIR = "chromaDB"

pdfpath = os.path.join("data","market_analysis.pdf")

print("working")