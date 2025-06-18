import random
import time
import pyttsx3
import locale
engine = pyttsx3.init()
locale.setlocale(locale.LC_TIME, 'en_US.UTF-8')
current_time = time.strftime("%I:%M %p")
engine.say("bonjour mohamad "+ current_time )
engine.runAndWait()