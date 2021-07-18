import googletrans
import speech_recognition as sr
import gtts
import playsound

recognizer = sr.Recognizer()
translator = googletrans.Translator()
input_lang = 'Language Code 1' #replace with respective language code form Language list-Shortcuts file
output_lang = 'language Code 2'#replace with respective language code form Language list-Shortcuts file
try:
    with sr.Microphone() as source:
        print('Speak Now')
        voice = recognizer.listen(source)
        text = recognizer.recognize_google(voice, language=input_lang)
        print(text)
except:
    pass

translated = translator.translate(text, dest=output_lang)
print(translated.text)
converted_audio = gtts.gTTS(translated.text, lang=output_lang)
converted_audio.save('t.mp3')
playsound.playsound('t.mp3')
print(googletrans.LANGUAGES)
