import os
import json
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()



# Function to split JSON by each key
def split_json_by_keys(json_data):
    split_data = []
    for key, value in json_data.items():
        # Convert each key-value pair into a Document object with metadata
        split_data.append(Document(page_content=key + '\n'+ value['content'], metadata={**value['metadata'], "key": key}))
    return split_data

def split_json_by_keys_title(json_data):
    split_data = []
    for key, value in json_data.items():
        # Convert each key-value pair into a Document object with metadata
        split_data.append(Document(page_content=key, metadata={"key": key}))
    return split_data

def build_chroma_db(file_path, persistent_directory, action):
    # Check if the Chroma vector store already exists
    if not os.path.exists(persistent_directory):
        print("Persistent directory does not exist. Initializing vector store...")

        # Ensure the JSON file exists
        if not os.path.exists(file_path):
            raise FileNotFoundError(
                f"The file {file_path} does not exist. Please check the path."
            )

        # Load the JSON content from the file
        with open(file_path, 'r') as f:
            docs = json.load(f)

        # Split the JSON data by top-level keys
        documents = action(docs)

        # Display information about the split documents
        print("\n--- Document Chunks Information ---")
        print(f"Number of document chunks: {len(documents)}")
        print(f"Sample chunk:\n{documents[0].page_content}\n")

        # Create embeddings
        print("\n--- Creating embeddings ---")
        embeddings = OpenAIEmbeddings(
            model="text-embedding-3-small"
        )  # Update to a valid embedding model if needed
        print("\n--- Finished creating embeddings ---")

        # Create the vector store and persist it automatically
        print("\n--- Creating vector store ---")
        db = Chroma.from_documents(
            documents, embeddings, persist_directory=persistent_directory)
        print("\n--- Finished creating vector store ---")

    else:
        print("Vector store already exists. No need to initialize.")


if __name__ == '__main__':
    # Define the directory containing the text file and the persistent directory
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, "data", "sitesData.json")
    persistent_directory = os.path.join(current_dir, "db", "site_content_db")
    build_chroma_db(file_path, persistent_directory,  split_json_by_keys)

    # persistent_directory = os.path.join(current_dir, "db", "site_title_db")
    # build_chroma_db(file_path, persistent_directory, split_json_by_keys_title)


