#pip install gTTS
#pip install playsound

from gtts import gTTS
from playsound import playsound
text = "your text"
var = gTTS(text = text, lang='en', slow=True)
var.save('your path to save the file\text.mp3')
playsound('your path to save the file\text.mp3')
