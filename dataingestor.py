import config
from langchain_community.document_loaders import PyPDFLoader
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma

def buildMarketIndex():
    print(f"Loading: {config.pdfpath}")
    loader = PyPDFLoader(config.pdfpath)
    pages = loader.load()

    splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 50)
    chunks = splitter.split_documents(pages)

    Embeddings = HuggingFaceEmbeddings(model_name = config.embeddingModel)

    Chroma.from_documents(
        documents = chunks,
        embedding = Embeddings,
        persist_directory = config.chromaDIR
    )
    print("Success: Vector database created in" + config.chromaDIR)

if __name__ == "__main__":
    buildMarketIndex()


# this file is being used to write pdf to translate and to store that into chromadb
