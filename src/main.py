import speech_recognition as sr
from natural_language_processing.intent_recognition import recognize_intent
from task_execution.task_router import route_task
from text_to_speech.speech_synthesis import synthesize_speech

print("Starting the Toxic Assistant...")

def main():
    print("Initializing speech recognizer...")
    recognizer = sr.Recognizer()

    print("Entering main loop...")
    while True:
        print("Listening...")
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source)

            print("Processing your request...")
            user_input = recognizer.recognize_google(audio)
            print(f"You said: {user_input}")

            intent = recognize_intent(user_input)
            print(f"Toxic Assistant: {intent}")

            response = route_task(intent, user_input)

            print(f"Toxic Assistant: {response}")
            synthesize_speech(response)

        except sr.UnknownValueError:
            print("Sorry, I didn't catch that. Could you please repeat?")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

