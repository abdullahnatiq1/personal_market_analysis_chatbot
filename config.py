import os 
from dotenv import load_dotenv

load_dotenv()

groqAPIKey = os.getenv("GROQ_API_KEY")
pineconeAPIKey = os.getenv("PINECONE_API_KEY")
indexName = os.getenv("indexName") 
modelName = "llama-3.3-70b-versatile"
embeddingModel = "all-MiniLM-L6-v2"

pdfpath = os.path.join("data", "market_analysis.pdf")

print("working")