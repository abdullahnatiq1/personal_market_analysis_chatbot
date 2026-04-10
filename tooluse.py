import config
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_core.tools import create_retriever_tool
from langchain_pinecone import PineconeVectorStore

def getRetriverTool():
    Embeddings = HuggingFaceEmbeddings(model_name=config.embeddingModel)

    vectorDB = PineconeVectorStore(
        index_name=config.indexName, 
        embedding=Embeddings,
        pinecone_api_key=config.pineconeAPIKey, 
        text_key="text"
    )
    
    retriever = vectorDB.as_retriever(search_kwargs={"k": 3})

    return create_retriever_tool(
        retriever,
        "MarketSearch",
        "Use this tool to find information about competitors and market trends from the PDF."
    )