import sys
import os
import pyaudio
import wave
from random import random as rnd
from time import sleep

chunk = 1024
sfl = []

p = pyaudio.PyAudio()
#print("{}".format(p.get_default_output_device_info()))

soundfiles = "sounds"

# load files
for sf in os.listdir(soundfiles):
    if sf.endswith(".wav"):
        sfl.append(sf)
            
timeout = 60
for i in range(timeout):
    ri = int(rnd() * len(sfl))
    sfh = wave.open(os.path.join(soundfiles, sfl[ri]), 'rb')
    #print("sample nr. {}".format(ri))
    stream = p.open(format=p.get_format_from_width(sfh.getsampwidth()),
                channels = sfh.getnchannels(),
                rate = sfh.getframerate(),
                output = True)
    data = sfh.readframes(chunk)
    while data:
        stream.write(data)
        data = sfh.readframes(chunk)
    stream.stop_stream()
    stream.close()
    sfh.close()
    
p.terminate()
    
