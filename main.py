from dotenv import load_dotenv
import os
from langchain_core.prompts import PromptTemplate
from langchain import chat_models
from langchain_openai import ChatOpenAI
from langchain_openai import AzureChatOpenAI

load_dotenv()

def main():
    print("Hello from langchain-course!")


    information = """
        The Prophet Muhammad (peace be upon him) stands as one of the most transformative and influential figures in human  history. Revered as the final messenger of God in Islam, he not only founded a global religion but also established a just and ethical society through visionary leadership. His influence spans across spiritual, social, political, and cultural spheres and continues to shape the lives of over two billion people worldwide.
    """

    # Create a prompt template
    summary_template = """
            Given the information {information} about a person:
            1. summarize their life and impact briefly
            2. list three key contributions they made to society 
        """ 
    summary_prompt_template = PromptTemplate( input_variables=["information"], template=summary_template ) 


    chat = ChatOpenAI(model="gpt-5", temperature=0) 
    chain = summary_prompt_template | chat 
    response = chain.invoke(input={"information": information}) 
    print("Summary and Contributions:") 
    print(response.content)


if __name__ == "__main__":
    main()
