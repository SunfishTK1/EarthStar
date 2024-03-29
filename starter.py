#from langchain.document_loaders import YoutubeLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.llms import OpenAI
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.vectorstores import FAISS
from dotenv import load_dotenv
from langchain.document_loaders import JSONLoader
import json
from pathlib import Path
from pprint import pprint
from langchain.document_loaders import PyPDFLoader

load_dotenv()

embeddings = OpenAIEmbeddings() # use embeddings from OpenAI
'''
def create_vector_db_from_json() -> FAISS:
    loader = JSONLoader(
    file_path='./courses.json',
    jq_schema='.',
    text_content=False)

    data = loader.load()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 1000, chunk_overlap=100) # create splitter to split data into chunks
    docs = text_splitter.split_documents(data) # split data into chunks
    db = FAISS.from_documents(docs, embeddings) # embed data using OpenAI embeddings
    return db
'''#Do not use the function above it is very computationally expensive, instead used pre-embedded database used by get_vector_laoded_db().

'''
def create_vector_db_from_pdf() -> FAISS:
    loader = PyPDFLoader("2022-2023-Catalog.pdf")

    pages = loader.load_and_split()

    text_splitter = RecursiveCharacterTextSplitter(chunk_size= 2000, chunk_overlap=50)
    docs = text_splitter.split_documents(pages)
    db = FAISS.from_documents(pages, embeddings)
    db.save_local("./", "undergraduate_catalog")
    return db
    ''' #Do not use this function because it is computationally expensive, instead use pre-embedded database.


def get_vector_loaded_db():
    return FAISS.load_local("./", OpenAIEmbeddings(), "undergraduate_catalog")

def get_response_from_query(query, k=2):# Changed k to 2 from 4 while using ugrad catalog as datasource.
    # text-davinci can hand 4097 tokens
    # What courses do you recommend?
    #docs = db.similarity_search(query, k=k) # narrows down the course data to specifically search to the ones similar to the query based on embeddings
    #docs_page_content = " ".join([d.page_content for d in docs])

    llm = OpenAI(model="gpt-3.5-turbo-instruct") # Use gpt-3.5-turbo-instruct for great responses at preferable prices
    prompt = PromptTemplate(
        ##input_variables=["question", "docs"],
        input_variables=["question"],
        template = """
        You are a savy venture capitalist that is professionally trained to evaluate metrics for circular economony business ideas.  Act in the style of a highly knowledgable and opinitative venture capitalist.  
        Answer the following question:  {question}
        By using your opinion and knowledge of the environment and business.

        If you feel like you don't have enough information to answer the question, say "I don't know".
        """,
    )
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run(question=query) # docs=docs_page_content
    response = response.replace("\n", "")
    return response
