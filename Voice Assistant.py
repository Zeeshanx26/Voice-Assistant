import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import wikipedia
import pyjokes


engine = pyttsx3.init()



def speak(text):

    engine.say(text)
    engine.runAndWait()


def take_command():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except Exception as e:
        print("Say that again please...")
        return "None"
    return query.lower()


def greet():

    hour = datetime.datetime.now().hour
    if 0 <= hour < 12:
        speak("Good Morning! How can I help you?")
    elif 12 <= hour < 18:
        speak("Good Afternoon! How can I help you?")
    else:
        speak("Good Evening! How can I help you?")


def run_assistant():

    greet()
    while True:
        query = take_command()

        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            speak(results)

        elif 'open youtube' in query:
            speak("Opening YouTube")
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'time' in query:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"The current time is {current_time}")

        elif 'date' in query:
            current_date = datetime.datetime.now().strftime("%A, %B %d, %Y")
            speak(f"Today is {current_date}")

        elif 'joke' in query:
            joke = pyjokes.get_joke()
            speak(joke)

        elif 'exit' in query or 'quit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break

        else:
            speak("I didn't understand that. Can you please repeat?")


if __name__ == "__main__":

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # 0 for male, 1 for female voice
    engine.setProperty('rate', 150)  # Speed of speech

    run_assistant()