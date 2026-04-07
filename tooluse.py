import config
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma
from langchain.tools.retriever import create_retriever_tool

def getRetriverTool():
    Embeddings = HuggingFaceEmbeddings(model_name = config.embeddingModel)
    vectorDB = Chroma(
        persist_directory = config.chromaDIR,
        embedding_function = Embeddings
    )

    retriever = vectorDB.as_retriever(search_kwargs = {"k": 3})

    return create_retriever_tool(
        retriever,
        "MArketsearch",
        "Use this tool to find information about  competitors and market trends for the pdf"
    )