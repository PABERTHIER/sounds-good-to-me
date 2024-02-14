# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 15:38:44 2017

@author: Pierre-Antoine
"""

# Recording audio from the default input device for the specified duration, saves it to a WAV file named "output.wav", and then terminates.
import pyaudio
import wave
 
chunk = 1024
format = pyaudio.paInt16
channels_number = 2     # Stereo
sampling_frequency = 44100   # Sampling frequency
output_file_name = "output.wav"
 
p = pyaudio.PyAudio()

duration = float(input('Duration (in seconds) ? '))
 
stream = p.open(format=format, channels=channels_number, rate=sampling_frequency, input=True, frames_per_buffer=chunk)
 
print("Start recording")
 
frames = []
 
for i in range(0, int(sampling_frequency / chunk * duration)):
    data = stream.read(chunk)
    frames.append(data)
 
print("End recording")
 
stream.stop_stream()
stream.close()
p.terminate()

wf = wave.open(output_file_name, 'wb')
wf.setnchannels(channels_number)
wf.setsampwidth(p.get_sample_size(format))
wf.setframerate(sampling_frequency)
wf.writeframes(b''.join(frames))
wf.close()

# Playing the "output.wav" file and waits until it's done playing before the program exits.
import pygame

pygame.mixer.init()
pygame.mixer.Sound("output.wav").play()
while pygame.mixer.get_busy():
    # Reading...
    pass
