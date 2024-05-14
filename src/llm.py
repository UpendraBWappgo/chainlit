import os 
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI
from src.config import instruction 

load_dotenv()

GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
print(GOOGLE_API_KEY,'lllllllllllll')
os.environ["GOOGLE_API_KEY"] = GOOGLE_API_KEY 
print(GOOGLE_API_KEY,'lllllllllllll')

user_message = "can you tell me about the menu "


def ask_bot(user_message): 
    messages=[{"role": "system", "content": instruction}, 
              {"role": "user", "content": user_message}]
    # message = [{"role": "system", "content": instruction}, 
    #            {"role": "user", "content": user_message}]

    # def ask_bot(messages): 
    llm = ChatGoogleGenerativeAI(model="gemini-pro")

    response = llm.invoke(messages)

    # print(response.content)
    return response.content


# if __name__ == "__main__": 
#     print("welcome to the chat bot")
#     message = ask_bot(input("I am your gini ask what you want?"))
#     print(message)

    # print(ask_bot("what is the meaning of large models?"))


# def load_model(model_name): 
#     if model_name == "gemini-pro":
#         llm = ChatGoogleGenerationAI(model="gemini-pro")
#     else: 
#         llm = ChatGoogleGenerationAI(model="gemini-pro-vision")
    
#     return llm  