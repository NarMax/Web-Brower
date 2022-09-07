import pyttsx3
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)
from termcolor import colored
def add_tab():
  audio="Hey this is your father..."
  print(colored(audio,'red',attrs=['bold']))
  print(audio)
  engine.say(audio)
  engine.runAndWait()
