import sounddevice as sd
import wavio
import speech_recognition as sr
import pyttsx3
import datetime
import wikipedia
import webbrowser
import os
import time
import requests

def get_news():
    api_key = "81f8bf38f875426386915079940d6971"
    url = f"https://newsapi.org/v2/top-headlines?country=in&apiKey={api_key}"
    try:
        response = requests.get(url)
        data = response.json()
        if "articles" in data:
            articles = data["articles"][:5]
            news_list = [article["title"] for article in articles if article["title"]]
            return news_list
        else:
            return ["No news articles found."]
    except Exception as e:
        return [f"Error fetching news: {e}"]



# Text-to-speech setup
engine = pyttsx3.init()
engine.setProperty('rate', 175)

def speak(text):
    print("Jarvis:", text)
    engine.say(text)
    engine.runAndWait()

# Save memory
def save_memory(text):
    with open("temp_memory.txt", "w") as f:
        f.write(text)

# Recall memory
def recall_memory():
    try:
        with open("temp_memory.txt", "r") as f:
            return f.read()
    except FileNotFoundError:
        return "I don't remember anything."

# Shutdown system
def shutdown_system(seconds=30):
    speak(f"Shutting down the system in {seconds} seconds.")
    os.system(f"shutdown /s /t {seconds}")

# Cancel shutdown
def cancel_shutdown():
    speak("Shutdown canceled.")
    os.system("shutdown /a")

# Record audio using sounddevice
def record_audio(filename="temp.wav", duration=5, rate=44100):
    print("Listening...")
    recording = sd.rec(int(duration * rate), samplerate=rate, channels=1)
    sd.wait()
    wavio.write(filename, recording, rate, sampwidth=2)

# Recognize voice
def listen_command():
    record_audio()
    recognizer = sr.Recognizer()
    try:
        with sr.AudioFile("temp.wav") as source:
            audio = recognizer.record(source)
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)
            return command
    except:
        return ""

# Knowledge base for GK and Physics
knowledge_base = {
    # GK Questions
    "what is the smallest continent": "The smallest continent is Australia.",
    "who is the prime minister of india": "The Prime Minister of India is Narendra Modi.",
    "capital of france": "The capital of France is Paris.",
    "how many continents are there": "There are seven continents.",
    "largest ocean in the world": "The Pacific Ocean is the largest ocean.",
    "national animal of india": "The national animal of India is the Bengal Tiger.",
    "national bird of india": "The national bird of India is the Peacock.",
    "national flower of india": "The national flower of India is the Lotus.",
    "fastest land animal": "The fastest land animal is the cheetah.",
    "highest mountain peak": "Mount Everest is the highest mountain peak.",
    "currency of japan": "The currency of Japan is Yen.",
    "largest desert in the world": "The Sahara Desert is the largest hot desert.",
    "longest river in the world": "The Nile is the longest river in the world.",
    "how many states in india": "There are 28 states in India.",
    "who was mahatma gandhi": "Mahatma Gandhi was the leader of India's independence movement.",
    "capital of china": "The capital of China is Beijing.",
    "which planet is known as the red planet": "Mars is known as the red planet.",
    "largest country by area": "Russia is the largest country by area.",
    "national anthem of india": "The national anthem of India is Jana Gana Mana.",
    "who wrote the national anthem": "Rabindranath Tagore wrote the national anthem of India.",
    "who invented the telephone": "Alexander Graham Bell invented the telephone.",
    "first man to walk on the moon": "Neil Armstrong was the first man to walk on the moon.",
    "how many bones in human body": "There are 206 bones in the human body.",
    "who invented computer": "Charles Babbage is known as the father of the computer.",
    "largest mammal": "The blue whale is the largest mammal.",
    "who discovered america": "Christopher Columbus is credited with discovering America.",
    "which is the coldest place on earth": "Antarctica is the coldest place on Earth.",
    "how many players in cricket team": "There are 11 players in a cricket team.",
    "national sport of india": "The national sport of India is Hockey.",
    "which is the tallest building in the world": "Burj Khalifa is the tallest building in the world.",

    # Physics Questions
    "what is newton's first law": "An object at rest stays at rest, and an object in motion stays in motion unless acted upon by an external force.",
    "what is newton's second law": "Force equals mass times acceleration.",
    "what is newton's third law": "For every action, there is an equal and opposite reaction.",
    "what is gravity": "Gravity is the force that attracts objects toward the center of the Earth.",
    "who discovered gravity": "Gravity was discovered by Isaac Newton.",
    "what is speed": "Speed is the distance traveled per unit of time.",
    "what is velocity": "Velocity is speed with direction.",
    "what is acceleration": "Acceleration is the rate of change of velocity.",
    "unit of force": "The unit of force is Newton.",
    "unit of energy": "The unit of energy is Joule.",
    "unit of power": "The unit of power is Watt.",
    "what is work": "Work is done when a force is applied to an object and it moves in the direction of the force.",
    "law of conservation of energy": "Energy cannot be created or destroyed, only transformed from one form to another.",
    "what is potential energy": "Potential energy is stored energy due to position.",
    "what is kinetic energy": "Kinetic energy is energy due to motion.",
    "what is friction": "Friction is the force that resists motion between two surfaces.",
    "what is pressure": "Pressure is force per unit area.",
    "unit of pressure": "The unit of pressure is Pascal.",
    "what is mass": "Mass is the amount of matter in an object.",
    "what is weight": "Weight is the force exerted by gravity on an object.",
    "unit of current": "The unit of electric current is Ampere.",
    "unit of resistance": "The unit of resistance is Ohm.",
    "unit of charge": "The unit of electric charge is Coulomb.",
    "what is conductor": "A conductor allows electricity to pass through it easily.",
    "what is insulator": "An insulator does not allow electricity to pass through it easily.",
    "example of conductor": "Copper is a good conductor of electricity.",
    "example of insulator": "Rubber is a good insulator.",
    "what is refraction": "Refraction is the bending of light as it passes from one medium to another.",
    "what is reflection": "Reflection is the bouncing of light from a surface.",
    "what is lens": "A lens is a transparent material that bends light to form images."
}

def get_knowledge_answer(command):
    for key in knowledge_base:
        if key in command:
            return knowledge_base[key]
    return None

# Main Jarvis function
def run_jarvis():
    speak("Yes sir. Say 'Jarvis' to wake me.")

    while True:
        print("Waiting for wake word 'Jarvis' or cancel word 'Arise'...")
        command = listen_command()

        if "arise" in command:
            cancel_shutdown()
            continue

        if "jarvis" not in command:
            continue

        # Wake word detected
        speak("Yes? What can I do for you?")

        while True:
            command = listen_command()

            if "sleep" in command:
                speak("Okay, going to sleep.")
                break

            answer = get_knowledge_answer(command)
            if answer:
                speak(answer)
            elif "wikipedia" in command:
                try:
                    result = wikipedia.summary(command.replace("wikipedia", ""), sentences=2)
                    speak(result)
                except:
                    speak("Sorry, I couldn't find anything relevant.")
            elif "time" in command:
                time_now = datetime.datetime.now().strftime("%I:%M %p")
                speak(f"The time is {time_now}")
            elif "open notepad" in command:
                os.system("notepad")
            elif "open chrome" in command:
                os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            elif "open youtube" in command:
                webbrowser.open("https://www.youtube.com")
            elif "open gmail" in command:
                webbrowser.open("https://mail.google.com")
            elif "news" in command or "headlines" in command:
                speak("Here are the top headlines.")
                headlines = get_news()
                for headline in headlines:
                    print("Headline:", headline)  # Debug print
                    speak(headline)
                continue

            elif "open spotify" in command:
                webbrowser.open("https://open.spotify.com")
            elif "open facebook" in command:
                webbrowser.open("https://www.facebook.com")
            elif "open chat gpt" in command:
                webbrowser.open("https://chatgpt.com/")
            elif "open notepad plus plus" in command or "open notepad++" in command:
                os.startfile("C:\\Program Files\\Notepad++\\notepad++.exe")
            elif "open vlc" in command:
                os.startfile("C:\\Program Files\\VideoLAN\\VLC\\vlc.exe")
            elif "open bluetooth" in command or "bluetooth settings" in command:
                os.system("start ms-settings:bluetooth")
                speak("Opening Bluetooth settings.")

            elif "remember" in command:
                speak("What should I remember?")
                memory = listen_command()
                save_memory(memory)
                speak("Got it. I’ll remember that.")
            elif "do you remember" in command:
                memory = recall_memory()
                speak(f"You told me to remember: {memory}")
            elif "shutdown" in command:
                speak("After how many seconds should I shut down?")
                delay_cmd = listen_command()
                try:
                    delay = int("".join(filter(str.isdigit, delay_cmd)))
                except:
                    delay = 30
                shutdown_system(delay)
                break
            elif "exit" in command or "bye" in command:
                speak("Goodbye!")
                return
            elif command != "":
                speak("Sorry, I didn't understand that.")

# Start the assistant
run_jarvis()
