def handle_conversation(intent, user_input):
    if intent == 'weather':
        return "I'll check the weather for you."
    elif intent == 'web_search':
        return "I'll search the web for that information."
    elif intent == 'help':
        return "I can assist you with checking the weather, searching the web, and answering basic queries. How can I help?"
    elif intent == 'greeting':
        return "Hello! How can I assist you today?"
    elif intent == 'goodbye':
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to help with that. Can you be more specific?"
