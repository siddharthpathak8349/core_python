from translate import Translator
import pyttsx3

# Initialize the translator
translator = Translator(from_lang="english", to_lang="hindi")
# Translate the text
translation = translator.translate("Hello world")

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Set speech rate to normal (around 150-180 is considered natural)
engine.setProperty('rate', 150)

# Set the voice to a female voice
voices = engine.getProperty('voices')
for voice in voices:
    if "female" in voice.name.lower():  # Look for a female voice
        engine.setProperty('voice', voice.id)
        break

# Speak the translated text
engine.say(translation)
engine.runAndWait()
