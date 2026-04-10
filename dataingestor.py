import config
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_pinecone import PineconeVectorStore

def buildMarketIndex():
    print(f"Loading: {config.pdfpath}")
    loader = PyPDFLoader(config.pdfpath)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_documents(pages)

    print(f"Split into {len(chunks)} chunks.")

    Embeddings = HuggingFaceEmbeddings(model_name=config.embeddingModel)

    print("Uploading to Pinecone this might take a minute.")

    vectorDB = PineconeVectorStore.from_documents(
        documents=chunks,
        embedding=Embeddings,
        index_name=config.indexName,           
        pinecone_api_key=config.pineconeAPIKey
    )

if __name__ == "__main__":
    buildMarketIndex()