# Importing TextBlob to help the chatbot understand language nuances.
from textblob import TextBlob

# Define intents
intents = {
    "hours": {
        "keywords": ["hours", "open", "timing", "time"],
        "response" : "We are open from 9-6 AM"
    },
    "return" : {
        "keywords": ["close", "refund", "problem"],
        "response": "Id be happy to help and we are now connecting you to a live agent"
    }
}

def get_response(message:str):
    msg = message.lower()
    for _, data in intents.items():
        for keyword in data["keywords"]:
            if keyword in msg:
                return data["response"]
    else:
        sentiment = TextBlob(message).sentiment.polarity
        if sentiment > 0:
            return ("That's so great to hear !!")
        elif sentiment < 0: 
            return ("I am so sorry")
        else:
            return (" Can you please repeat it !!")

def chat():
    print("Hi !! How can I help you today ?")
    while (user_msg := input("You: ")):
        if any(keyword in user_msg.strip().lower() for keyword in ["quit", "bye"]):
            break
        print(f"\n ChatBot: {get_response(user_msg)}")
    
    print("Thank you for chatting and have a great day !!")
          


if __name__ == "__main__":
    # Creating the chatbot and starting the chat loop.
    chatbot = chat()
