# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:17:47 2017

@author: Pierre-Antoine
"""

# Creating a stereo WAV file with sine wave audio on each channel,
# allowing the user to specify the frequencies and levels of the waves, as well as the duration of the audio.
import wave
import math
import binascii

print("Creating an audio file in WAV format (PCM 8-bit stereo 44100 Hz)")
print("Sine-shaped sound on each channel\n")

file_name = 'sound.wav'
sound = wave.open(file_name, 'w')

channels_number = 2    # Stereo
bytes_number = 1    # Sample size: 1 byte = 8 bits
sampling_frequency = 44100   # Sampling frequency

left_channel_frequency = float(input('Left channel sound frequency (Hz) ? '))
right_channel_frequency = float(input('Right channel sound frequency (Hz) ? '))
left_channel_level = float(input('Left channel sound level (0 to 1) ? '))
right_channel_level = float(input('Right channel sound level (0 to 1) ? '))

duration = float(input('Duration (in seconds) ? '))

samples_number = int(duration * sampling_frequency)
print("Number of samples :", samples_number)

parameters = (channels_number, bytes_number, sampling_frequency, samples_number, 'NONE', 'not compressed')
sound.setparams(parameters)    # Creation of the header (44 bytes)

# Max level in the positive wave: +1 -> 255 (0xFF)
# Max level in the negative wave: -1 -> 0 (0x00)
# Zero sound level: 0 -> 127.5 (0x80 in rounded value)

left_amplitude = 127.5 * left_channel_level
right_amplitude = 127.5 * right_channel_level

print('Please wait...')
for i in range(0, samples_number):
    # Left channel
    # 127.5 + 0.5 to round to the nearest integer
    left_channel_sample = wave.struct.pack('B', int(128.0 + left_amplitude * math.sin(2.0 * math.pi * left_channel_frequency * i / sampling_frequency)))
    # Right channel
    right_channel_sample = wave.struct.pack('B', int(128.0 + right_amplitude * math.sin(2.0 * math.pi * right_channel_frequency * i / sampling_frequency)))
    sound.writeframes(left_channel_sample + right_channel_sample)

sound.close()

file = open(file_name, 'rb')
data = file.read()
file_size = len(data)
print('\nFile Size', file_name, ':', file_size, 'bytes')
print("Reading the header content (44 bytes) :")
print(binascii.hexlify(data[0:44]))
print("Number of data bytes :", file_size - 44)
file.close()
