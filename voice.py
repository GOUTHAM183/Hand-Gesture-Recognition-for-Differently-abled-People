from gtts import gTTS
import os
from playsound import playsound
from io import BytesIO
import pyttsx3
'''
mytext = 'Hello world, Welcome'
language = 'en'
  

myobj = gTTS(text=mytext, lang=language, slow=False)
  

myobj.save("hello.mp3")
playsound("hello.mp3")
'''

engine = pyttsx3.init()
text = "Python is a great programming language"
engine.say(text)
# play the speech
engine.runAndWait()