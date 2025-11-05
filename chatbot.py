def chatbot(): 
    print("Chatbot: Hello! I'm your friendly chatbot. Type 'bye' to exit.\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi there!")
        elif user_input == "how are you":
            print("Chatbot: I'm doing great, thank you! How about you?")
        elif user_input == "i am fine":
            print("Chatbot: That's nice to hear!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a nice day 😊")
            break
        else:
            print("Chatbot: Sorry, I didn’t understand that.")

# Run the chatbot
chatbot()
