import config
from langchain_groq import ChatGroq
from langchain_classic.agents import AgentExecutor, create_react_agent
from langchain_core.prompts import PromptTemplate 
from tooluse import getRetriverTool

def agentSetup():
    llm = ChatGroq(
        groq_api_key = config.groqAPIKey, 
        model_name = config.modelName,
        temperature = 0.4
    )
    
    Tools = [getRetriverTool()]
    template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought: {agent_scratchpad}"""

    prompt = PromptTemplate.from_template(template)
    marketAgent = create_react_agent(llm, Tools, prompt)

    return AgentExecutor(
        agent = marketAgent,
        tools = Tools,
        verbose = True,
        handle_parsing_errors = True
    )