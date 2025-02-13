from llama_index.core import SimpleDirectoryReader
from llama_index.core import VectorStoreIndex, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.llms.gemini import Gemini
from dotenv import load_dotenv
import os 

# Loading the data
document = SimpleDirectoryReader("data").load_data()

# Setting the embedding model
Settings.embed_model = HuggingFaceEmbedding(
    model_name="BAAI/bge-small-en-v1.5"
)

# Setting the text splitter
text_splitter = SentenceSplitter(chunk_size=1000)
Settings.text_splitter = text_splitter

# Creating a vector index
index = VectorStoreIndex.from_documents(document, transformations=[text_splitter], embed_model=Settings.embed_model)

# Saving the index
index.storage_context.persist(persist_dir="storage")

# Creating a Gemini model
load_dotenv()
api_key = os.getenv('api_key')
model = 'models/gemini-2.0-flash'

llm = Gemini(model=model, api_key=api_key)
Settings.llm = llm


# Retrieving Context and Generating response
def ask_question(question):
    query_engine = index.as_query_engine()
    response = query_engine.query(question)
    answer = response.response
    return answer