import sounddevice as sd
fs = 44100
sd.default.samplerate = fs
sd.default.channels = 2
duration = 5

myrecording = sd.rec(int(duration*fs))
sd.wait()
#print(myrecording)
#myrec = sd.playrec(myrecording)
#from scipy.io.wavefile import write
#write('recording.wav',44100,myrecording)
#from numpy import savetxt

#savetxt('recordingtxt.txt',myrecording)

'''from wavefile import WaveWriter, Format
import numpy as np
BUFFERSIZE = 512
NCHANNELS = 2
TITLE = "Some Noise"
ARTIST = "The Artists"

with WaveWriter('synthaaaa.wav',channels=NCHANNELS,format=Format.OGG|Format.VORBIS,) as w :
    w.metadata.title = TITLE
    w.write(myrecording)'''

import wavio as wv
wv.write('rec0001.wav',myrecording,rate = fs,sampwidth = 3)

import pythonSpeech
import googleSpanQueryFile
#import googleJSON
