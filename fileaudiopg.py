from gtts import gTTS
import  os
text=open("hel.txt","r",encoding='utf-8').read()
lan='ml'
output=gTTS(text=text,lang=lan,slow=False)
output.save("out.mp3")
os.system("start out.mp3")