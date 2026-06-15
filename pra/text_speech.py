"""import pyttsx3
from gtts import gTTS
import os
import platform


def speak_text(
    text: str,
    voice_index: int = 0,
    rate: int = 140,
    volume: float = 0.95,
    use_gtts: bool = False,
) -> None:
    if not isinstance(text, str) or not text.strip():
        raise ValueError("Text must be a non-empty string.")

    if use_gtts:
        try:
            tts = gTTS(text=text, lang="en", slow=False)
            tts.save("temp_audio.mp3")
            os.system(
                "mpg123 temp_audio.mp3"
            )  # Requires mpg123 (install: sudo apt install mpg123)
            os.remove("temp_audio.mp3")
            return
        except Exception as e:
            print(f"gTTS failed: {e}. Falling back to pyttsx3.")

    try:
        # Use the correct Linux driver and fall back safely if unavailable
        if platform.system() == "Linux":
            try:
                engine = pyttsx3.init(driverName="espeak")
            except Exception:
                engine = pyttsx3.init()
        else:
            engine = pyttsx3.init()

        voices = engine.getProperty("voices")
        if voices:
            voice_index = max(0, min(voice_index, len(voices) - 1))
            engine.setProperty("voice", voices[voice_index].id)

        # Optimized for clarity
        engine.setProperty("rate", rate)
        engine.setProperty("volume", volume)

        engine.say(text)
        engine.runAndWait()
    except Exception as e:
        print(f"pyttsx3 failed: {e}")


if __name__ == "__main__":
    # Example usage
    speak_text("Hello, how are you? its nice to meet you")  # Use pyttsx3 (offline)
    # speak_text("Hello, how are you?", use_gtts=True)  # Use gTTS (online, clearer)
"""
import requests

url = "http://10.52.117.119:8080/message"

respond = requests.post(url)
respond.