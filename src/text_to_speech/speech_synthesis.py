import pyttsx3

def synthesize_speech(text):
    # Initialize the speech engine
    engine = pyttsx3.init()

    # Optionally, set properties (e.g., voice, rate, volume)
    # Uncomment and modify the following lines if needed:
    # voices = engine.getProperty('voices')
    # engine.setProperty('voice', voices[0].id)  # Set voice (0 for male, 1 for female, etc.)
    # engine.setProperty('rate', 150)  # Set speech rate
    # engine.setProperty('volume', 1.0)  # Set volume (0.0 to 1.0)

    # Say the text
    engine.say(text)

    # Wait for the speech to finish
    engine.runAndWait()
