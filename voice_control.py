import speech_recognition as sr
import pyautogui
import pywhatkit
import webbrowser

class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()

    def listen(self):
        """Capture voice command from microphone"""
        with self.microphone as source:
            print("🎤 Listening...")
            self.recognizer.adjust_for_ambient_noise(source)
            audio = self.recognizer.listen(source)

        try:
            command = self.recognizer.recognize_google(audio).lower()
            print(f"✅ Recognized: {command}")
            return command
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return ""
        except sr.RequestError:
            print("⚠️ Speech Recognition service error")
            return ""

    def handle_command(self, command):
        """Process recognized voice command"""

        # Mouse actions
        if "click" in command:
            pyautogui.click()
        elif "double click" in command:
            pyautogui.doubleClick()
        elif "right click" in command:
            pyautogui.rightClick()

        # Scrolling
        elif "scroll up" in command:
            pyautogui.scroll(500)
        elif "scroll down" in command:
            pyautogui.scroll(-500)

        # Volume control
        elif "volume up" in command:
            pyautogui.press("volumeup")
        elif "volume down" in command:
            pyautogui.press("volumedown")
        elif "mute" in command:
            pyautogui.press("volumemute")

        # 🎵 Media control
        elif "pause" in command or "play" in command:
            pyautogui.press("playpause")
        elif "next" in command:
            pyautogui.press("nexttrack")
        elif "previous" in command or "back" in command:
            pyautogui.press("prevtrack")

        # YouTube search
        elif "youtube" in command:
            query = command.replace("youtube", "").strip()
            if query:
                pywhatkit.playonyt(query)
            else:
                webbrowser.open("https://www.youtube.com")

        # Open Google
        elif "open google" in command:
            webbrowser.open("https://www.google.com")

        # Exit program
        elif "quit" in command or "exit" in command:
            print("👋 Exiting...")
            exit()
