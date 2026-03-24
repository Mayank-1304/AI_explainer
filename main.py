# from langchain_google_genai import ChatGoogleGenerativeAI
# from dotenv import load_dotenv
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_core.output_parsers import StrOutputParser

# load_dotenv()

# model = ChatGoogleGenerativeAI(
#     model = "gemini-2.0-flash"
# )

# prompts = ChatPromptTemplate.from_template(
#     "explain {topic} in breif"
# )

# chain =  prompts | model | StrOutputParser()

# result = chain.invoke({"topic": "universe"})

# print(result)