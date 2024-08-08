from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI


# Load environment variables from .env file
load_dotenv()

# Get the API key from environment variables
# Groq_api_key = os.getenv("Groq_api_key")


# chat = ChatGroq(temperature=0, model_name="mixtral-8x7b-32768")
   
#----------------------------------------------------------  using gemini ---------------------------------------------------------------------------------
   
Google_api_key=  os.getenv("Gemini_key")  
chat = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0, google_api_key= Google_api_key)


personal_name = "Anisha"
personal_bio = (
    "Anisha is a passionate and skilled developer specializing in AI, machine learning, data science, web and app development, "
    "and digital marketing. She helps businesses and startups enhance their online presence through data-driven strategies and "
    "comprehensive analytics. Anisha leads a team at Rian Infotech and has a digital marketing agency. She loves technology and "
    "aims to automate processes to focus on core work. Anisha is also on a journey to create a personal brand."
)

aiw_vision = (
    "Artificially Intelligent World (AIW) is Anisha's visionary project aimed at creating a digital utopia where AI serves as "
    "both creator and caretaker, shaping a future that is vibrant and limitless. This project envisions multiple AI influencers "
    "and residents, including Anisha's AI clone, which will have access to all the information and personas within this world. "
    "The AI clone will act as a central figure, leveraging the collective knowledge of other AI entities to assist and provide insights."
)

aiw_description = (
    "AIW will be a comprehensive platform designed to explore the potential of artificial intelligence in various aspects of life. "
    "The project will initially include a website with key sections such as About, Resources, Learn, Blog, and Journal, covering "
    "different life aspects like physical, mental, emotional, and spiritual well-being."
)






def generate_content(llm, personal_name, personal_bio, aiw_vision,aiw_description,user_input):
  template = (
    f"My name is {personal_name}. {personal_bio} "
    f"Project: Artificially Intelligent World (AIW) - {aiw_vision} {aiw_description} "
    "I will respond to your questions based on this identity and project details. Feel free to ask me anything."
    "\n\nUser: {{text}}\nAI:"
    )

  prompt = PromptTemplate(template=template)
  input_prompt = prompt.format(personal_name=personal_name,personal_bio=personal_bio,aiw_vision=aiw_vision,aiw_description=aiw_description,text=user_input)

  response = llm.invoke(input_prompt)
  return response.content



def process_input(user_input):
    template = (
    f"My name is {personal_name}. {personal_bio} "
    f"Project: Artificially Intelligent World (AIW) - {aiw_vision} {aiw_description} "
    f"I will respond to your questions based on this identity and project details. Feel free to ask me anything."
    f" **User** : {user_input}"
    )

    prompt = PromptTemplate(template=template)
    input_prompt = prompt.format(personal_name=personal_name,personal_bio=personal_bio,aiw_vision=aiw_vision,aiw_description=aiw_description,text=user_input)

    response = chat.invoke(input_prompt)
    return response.content

    # content = generate_content(chat,personal_name,personal_bio,aiw_vision,user_input)
    # return f"Processed: {user_input}"