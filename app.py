import speech_recognition as sr
import pyautogui
import difflib
import time

DEBUG = False

# Initialize recognizer and microphone
recognizer = sr.Recognizer()
microphone = sr.Microphone(device_index=2)  # use your own mic index

# Commands with keywords
commands = {
    "video speichern": ["video", "speichern"],
    "aufnahme starten": ["aufnahme", "starten"],
    "aufnahme stoppen": ["aufnahme", "stoppen"],
    "foto machen": ["foto", "machen"]
}

# Actions for each command
command_actions = {
    "video speichern": lambda: pyautogui.hotkey('alt', 'f10'),
    "aufnahme starten": lambda: pyautogui.hotkey('alt', 'f9'),
    "aufnahme stoppen": lambda: pyautogui.hotkey('alt', 'f9'),
    "foto machen": lambda: pyautogui.hotkey('win', 'prtsc')
}

# Fuzzy match helper
def fuzzy_match(text, options, threshold=0.6):
    text = text.lower()
    for option in options:
        if difflib.SequenceMatcher(None, text, option).ratio() > threshold:
            return option
    return None

def match_command_keywords(text):
    text_words = text.lower().split()
    matched_commands = []
    for cmd, keywords in commands.items():
        if all(any(difflib.SequenceMatcher(None, kw, w).ratio() > 0.6 for w in text_words) for kw in keywords):
            matched_commands.append(cmd)
    return matched_commands

def listen_for_commands():
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        if DEBUG:
            print("Listening for commands...")

        while True:
            try:
                audio = recognizer.listen(source, phrase_time_limit=4)
                try:
                    chunk = recognizer.recognize_google(audio, language="de-DE").lower()
                    if DEBUG:
                        print(f"Recognized chunk: {chunk}")

                    # Match all commands in this chunk
                    matched = match_command_keywords(chunk)
                    for cmd in matched:
                        if DEBUG:
                            print(f"Executing action for: {cmd}")
                        command_actions[cmd]()

                except sr.UnknownValueError:
                    if DEBUG:
                        print("Could not understand chunk, continuing...")
                except sr.RequestError as e:
                    if DEBUG:
                        print(f"Request error: {e}")

            except Exception as e:
                if DEBUG:
                    print(f"Listening error: {e}")

if __name__ == "__main__":
    listen_for_commands()
