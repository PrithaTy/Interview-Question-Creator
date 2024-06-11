from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import TokenTextSplitter
from langchain.docstore.document import Document
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from src.prompt import *

import os
from dotenv import load_dotenv

load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY

def file_processing(file_path):
    loader = PyPDFLoader(file_path)
    data = loader.load()

    question_gen = ""
    for page in data:
        question_gen += page.page_content

    splitter_ques_gen = TokenTextSplitter(
    model_name = "gpt-3.5-turbo",
    chunk_size = 10000,
    chunk_overlap = 200
    )

    chunk_ques_gen = splitter_ques_gen.split_text(question_gen)

    document_ques_gen = [Document(page_content = t) for t in chunk_ques_gen ]

    splitter_ans_gen = TokenTextSplitter(
    model_name = "gpt-3.5-turbo",
    chunk_size = 1000,
    chunk_overlap = 100
    )

    document_answer_gen = splitter_ans_gen.split_documents(
    document_ques_gen
    )

    return document_ques_gen, document_answer_gen


def llm_pipeline(file_path):

    document_ques_gen, document_answer_gen = file_processing(file_path)

    llm_ques_gen_pipeline = ChatOpenAI(
    model = "gpt-3.5-turbo",
    temperature = 0.3 #creativity of model; stick more to doc
    )


    PROMPT_QUESTIONS = PromptTemplate(template = promt_template,
               input_variables= ['text'])
    


    REFINE_PROMPT_QUESTIONS = PromptTemplate(
    input_variables = ["existing_answer","text"],
    template = refine_template
    )
