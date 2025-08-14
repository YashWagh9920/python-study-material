import speech_recognition as sr
from datetime import datetime
from langdetect import detect, DetectorFactory

# Fix randomness in langdetect
DetectorFactory.seed = 0

# Create recognizer
r = sr.Recognizer()

def listen_and_detect_language():
    with sr.Microphone() as source:
        print("Adjusting for ambient noise... please wait")
        r.adjust_for_ambient_noise(source, duration=1)

        print("Listening for speech... (Press Ctrl+C to stop)")
        while True:
            try:
                audio_data = r.listen(source)
                print("Processing...")

                # Recognize speech (Google auto detects language if not specified)
                text_spoken = r.recognize_google(audio_data)  

                # Detect language
                lang_code = detect(text_spoken)

                # Map common language codes to full names
                lang_map = {
                    "en": "English",
                    "hi": "Hindi",
                    "mr": "Marathi",
                    "gu": "Gujarati",
                    "bn": "Bengali",
                    "ta": "Tamil",
                    "te": "Telugu"
                }
                lang_name = lang_map.get(lang_code, lang_code)

                # Output
                timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                print(f"[{timestamp}] Language spoken: {lang_name} | What spoken: {text_spoken}")

            except sr.UnknownValueError:
                print("Could not understand audio")
            except sr.RequestError as e:
                print(f"API Error: {e}")

if __name__ == "__main__":
    try:
        listen_and_detect_language()
    except KeyboardInterrupt:
        print("\nStopped listening.")
