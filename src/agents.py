from crewai import Agent
from langchain.chat_models import ChatOpenAI
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

# Define Agents
topic_agent = Agent(
    role="Topic Researcher",
    goal="Find high-impact, trending LinkedIn post topics related to AI for mid-market companies",
    backstory="You are a marketing strategist who studies what's trending on social media and in industry blogs.",
    llm=llm
)

writer_agent = Agent(
    role="Content Writer",
    goal="Write multiple variations of a LinkedIn post based on a given topic",
    backstory="You are a creative marketer skilled in writing engaging LinkedIn content in different styles.",
    llm=llm
)

seo_agent = Agent(
    role="SEO Enhancer",
    goal="Improve the LinkedIn post by adding keywords, hashtags, and relevant links",
    backstory="You are a LinkedIn growth hacker specializing in post optimization and discoverability.",
    llm=llm
)