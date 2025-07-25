def chatbot():
    print("🤖 Chatbot: Hello! I’m your friendly chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").lower().strip()

        if user_input in ["hi", "hello", "hey"]:
            print("🤖 Chatbot: Hello! How can I assist you today?")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I'm ChatBot, your virtual assistant!")

        elif "how are you" in user_input:
            print("🤖 Chatbot: I'm just code, but I'm functioning perfectly. Thanks for asking!")

        elif "what can you do" in user_input:
            print("🤖 Chatbot: I can chat with you, answer simple questions, and show how rule-based bots work.")

        elif "bye" in user_input or "exit" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day.")
            break
        
        elif "help" in user_input:
            print("🤖 Chatbot: Sure! Ask me anything about weather, my name, or just say hi!")

        elif "weather" in user_input:
            print("🤖 Chatbot: I'm not connected to live data, but it’s always a good day to learn!")

        else:
            print("🤖 Chatbot: I’m sorry, I didn’t understand that. Try asking something else.")

chatbot()
