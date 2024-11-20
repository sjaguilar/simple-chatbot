import ollama
import pyttsx3
import speech_recognition as sr

# Initialize TTS engine
tts_engine = pyttsx3.init()

# Initialize Speech Recognizer
recognizer = sr.Recognizer()

def speak(text):
    """Convert text to speech."""
    tts_engine.say(text)
    tts_engine.runAndWait()

def listen():
    """Capture speech input from the user."""
    with sr.Microphone() as source:
        print("Listening...")
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand that. Please try again.")
            return None
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
            return None

# Configure TTS settings (optional)
def configure_tts():
    """Configure TTS voice settings."""
    tts_engine.setProperty('rate', 150)  # Speed
    tts_engine.setProperty('volume', 0.9)  # Volume
    voices = tts_engine.getProperty('voices')
    tts_engine.setProperty('voice', voices[0].id)  # Choose voice (0: default, 1: alternate)

configure_tts()

# Chat loop
print("Chatbot: Hello! You can speak or type. Say 'exit' to quit.")
speak("Hello! You can speak or type. Say 'exit' to quit.")

while True:
    # Get user input via voice or fallback to typing
    user_input = listen() or input("You: ")
    if user_input and user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        speak("Goodbye!")
        break

    if user_input:
        # Generate response using the Ollama model
        response = ollama.chat(
            model='dolphin-llama3:8beix',
            messages=[
                {'role': 'user', 'content': user_input}
            ]
        )
        response_text = response['message']['content']
        print(f"Chatbot: {response_text}")
        speak(response_text)
    else:
        print("Chatbot: Please say something or type your input.")
        speak("Please say something or type your input.")
