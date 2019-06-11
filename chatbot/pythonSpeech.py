import speech_recognition as sr
r = sr.Recognizer()

audiofile = 'rec0001.wav'
#text = ''

aFile = sr.AudioFile(audiofile)
with aFile as source:
    r.adjust_for_ambient_noise(source, duration=0.5)
    audio = r.record(source)
text = r.recognize_google(audio)#,show_all = True)
print(text)

f = open('recognizedtext.txt','w')
f.write(text)
f.close()

'''with harvard as source:
    audio = r.record(source,duration = 1)
print(r.recognize_google(audio))#,show_all=True))
#text = r.recognize_google(audio)'''
    
