#fuction
def chatbot():
    #function
    print(" ChatBot: Hello! I am a simple chatbot.")
    print("Type 'bye' to exit.\n")

#loop
    while True:
        user = input("You: ").lower()

        if user == "hello" or user == "hi":
            print(" ChatBot: Hi! How can I help you?")

        elif user == "how are you":
            print(" ChatBot: I am fine. Thanks for asking!")

        elif user == "what is your name":
            print(" ChatBot: My name is Python Bot.")

        elif user == "Tell me about yourself":
            print(" ChatBot: My name is Python Bot.I am create by my boss Antim Yadav")
        elif user == "about":
            print(" ChatBot: My name is Python Bot.I am created by my boss Mr antim")

        elif user == "bye":
            print(" ChatBot: Goodbye!")
            break

        else:
            print(" ChatBot: Sorry, I don't understand that.")

# Function Call
chatbot()


