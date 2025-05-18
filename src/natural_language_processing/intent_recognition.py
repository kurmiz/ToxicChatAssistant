def recognize_intent(user_input):
    user_input = user_input.lower()
    if any(word in user_input for word in ['weather', 'temperature', 'forecast']):
        return 'weather'
    elif any(word in user_input for word in ['time', 'clock', 'hour']):
        return 'time'
    elif any(word in user_input for word in ['date', 'day', 'month', 'year']):
        return 'date'
    elif any(phrase in user_input for phrase in ['your name', "what's your name", 'who are you']):
        return 'name'
    elif any(phrase in user_input for phrase in ['My name', "what's my name", 'xyz']):
        return 'created'    
    else:
        return 'general'