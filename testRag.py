from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

def load_and_split(sample2):
    loader = PyPDFLoader(sample2)
    documents = loader.load()
    print(f'Number of doument pages:{len(documents)}')