from agent import agentSetup

def runChatbot():
    ChatAgent = agentSetup()
    print("Market Analysis Chatbot")
    print("Type 'quit' to exit.")
    
    while True:
        UserInput = input("\nYou: ")
        if UserInput.lower() in ["quit", "exit"]:
            break
            
        Response = ChatAgent.invoke({"input": UserInput})
        print(f"\nAgent: {Response['output']}")

if __name__ == "__main__":
    runChatbot()