from agent import agentSetup

def runChatbot():
    chatAgent = agentSetup()
    print("Market Analysis Chatbot")
    
    while True:
        userInput = input("\nYou: ")
        if userInput.lower() in ["quit", "exit"]:
            break
            
        Response = chatAgent.invoke({"input": userInput})
        print(f"\nAgent: {Response['output']}")

if __name__ == "__main__":
    runChatbot()