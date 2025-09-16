import threading
from gaze_control import GazeController
from voice_control import VoiceController

def run_gaze():
    gaze = GazeController()
    gaze.run()

def run_voice():
    voice = VoiceController()
    while True:
        command = voice.listen()
        if command:
            voice.handle_command(command)

def main():
    print("""
🎯 AI Voice + Gaze Control System Ready!

👉 Available voice commands:
   - 'click' / 'double click' / 'right click'
   - 'scroll up' / 'scroll down'
   - 'volume up' / 'volume down'
   - 'youtube <song name>' (e.g., youtube kesariya)
   - 'pause' / 'play' (YouTube)
   - 'skip' (skip forward on YouTube)
   - 'open google'
   - 'quit' / 'exit'
    """)

    # Run gaze and voice control in parallel
    threading.Thread(target=run_gaze, daemon=True).start()
    run_voice()

if __name__ == "__main__":
    main()
