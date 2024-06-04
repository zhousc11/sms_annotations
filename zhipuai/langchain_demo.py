from langchain import hub
from langchain.agents import AgentExecutor, create_react_agent
from langchain_community.tools.tavily_search import TavilySearchResults
import os
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory

llm = ChatOpenAI(
    temperature=0.95,
    model="glm-4",
    openai_api_key="SECRET",
    openai_api_base="https://open.bigmodel.cn/api/paas/v4/"
)

os.environ["TAVILY_API_KEY"] = "SECRET"
tools = [TavilySearchResults(max_results=2)]
prompt = hub.pull("hwchase17/react")

# Choose the LLM to use
agent = create_react_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
agent_executor.invoke({"input": "what is LangChain?"})