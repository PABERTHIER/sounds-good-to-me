# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 16:12:13 2017

@author: Pierre-Antoine
"""

# Playing the "file.wav" file using the Windows sound-playing capabilities provided by winsound.
import winsound
winsound.PlaySound('file.wav',winsound.SND_FILENAME)
