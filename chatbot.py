import random
import spacy
from nltk.tokenize import word_tokenize

# Load spaCy English model
nlp = spacy.load("en_core_web_sm")

# Predefined responses
responses = {
    "greeting": ["Hello! How can I assist you today?", "Hi there! What can I do for you?"],
    "farewell": ["Goodbye! Have a great day!", "See you soon! Take care!"],
    "thanks": ["You're welcome!", "No problem! Always here to help!"],
    "default": ["I'm sorry, I don't understand. Could you rephrase?", "Can you clarify your question?"]
}

# Function to categorize user input
def get_intent(text):
    text = text.lower()
    tokens = word_tokenize(text)
    
    if any(word in tokens for word in ["hi", "hello", "hey"]):
        return "greeting"
    elif any(word in tokens for word in ["bye", "goodbye", "see you"]):
        return "farewell"
    elif any(word in tokens for word in ["thank", "thanks"]):
        return "thanks"
    else:
        return "default"

# Chatbot function
def chatbot():
    print("Chatbot: Hello! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye!")
            break
        intent = get_intent(user_input)
        response = random.choice(responses[intent])
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    chatbot()