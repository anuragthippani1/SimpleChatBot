import re
import random 
from collections import defaultdict

class SimpleChatbot:
    def __init__(self):

        self.patterns = {
            r'hi|hello|hey': [
                "Hello! How are you today?",
                "Hi there! Nice to meet you!",
                "Hey! How can I help you?"
            ],
            r'how are you': [
                "I'm doing well, thank you for asking!",
                "I'm great! How about you?",
                "All good here! What's on your mind?"
            ],
            r'what is your name': [
                "I'm ChatBot, nice to meet you!",
                "You can call me ChatBot!",
                "My name is ChatBot."
            ],
            r'bye|goodbye': [
                "Goodbye! Have a great day!",
                "See you later!",
                "Bye! Come back soon!"
            ],
            r'weather': [
                "I can't check the weather, but I hope it's nice where you are!",
                "Are you planning any outdoor activities?",
                "I wish I could tell you about the weather!"
            ],
            r'joke': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "What did one ocean say to the other? Nothing, they just waved!",
                "Why did the math book look sad? Because it had too many problems."
            ],
            r'what can you do': [
                "I can chat with you, answer questions, and tell jokes!",
                "I can help with information or even entertain you with a joke!",
                "I can respond to various questions. What do you want to know?"
            ],
            r'what is your favorite': [
                "I don't have preferences, but I do enjoy chatting with you!",
                "I like helping people like you, that's my favorite thing to do!"
            ],
            r'tell me a fact': [
                "Did you know? Honey never spoils! Archaeologists have found pots of honey in ancient tombs that are over 3,000 years old.",
                "Here's a fun fact: Octopuses have three hearts!",
                "Did you know that a day on Venus is longer than a year on Venus?"
            ],
            r'tell me about yourself': [
                "I'm ChatBot, created to assist with your queries and have fun conversations!",
                "I don't have a story, but I'm here to talk and help you out as best I can."
            ]
        }
        

        self.context = defaultdict(str)
        self.user_name = None
        
    def get_name(self, user_input):
        """Ask for the user's name if it's not already provided."""
        if self.user_name:
            return f"Nice to see you again, {self.user_name}!"
        else:
            return "What's your name?"

    def remember_name(self, user_input):
        """Store the user's name."""
        if not self.user_name:
            self.user_name = user_input
            return f"Nice to meet you, {self.user_name}!"
        return None

    def respond(self, user_input):

        user_input = user_input.lower()


        if "my name is" in user_input or "i am" in user_input:
            name = re.sub(r"my name is|i am", "", user_input).strip()
            return self.remember_name(name)


        if "what is your name" in user_input:
            return self.get_name(user_input)
        

        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input):
                return random.choice(responses)
        

        return random.choice([
            "I'm not sure I understand. Could you rephrase that?",
            "Interesting! Tell me more about that.",
            "I'm still learning. Could you elaborate?",
            "That's a good question! I'm not quite sure how to answer."
        ])

def main():
    chatbot = SimpleChatbot()
    print("ChatBot: Hi! I'm a simple chatbot. Type 'bye' to exit.")
    
    while True:
        user_input = input("You: ").strip()
        
        if user_input.lower() in ['bye', 'goodbye', 'exit']:
            print("ChatBot:", chatbot.respond(user_input))
            break
            
        response = chatbot.respond(user_input)
        print("ChatBot:", response)

if __name__ == "__main__":
    main()
