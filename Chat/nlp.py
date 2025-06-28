import random

def get_bot_response(user_input):
    # Sample logic (you can integrate spaCy or transformers here)
    responses = {
        "hello": "Hi! How can I assist you today?",
        "help": "Sure, I’m here to help. Ask me anything!",
        "bye": "Goodbye! Have a nice day!",
    }

    for key in responses:
        if key in user_input.lower():
            return responses[key]

    return "I'm not sure how to respond to that. Can you rephrase?"
