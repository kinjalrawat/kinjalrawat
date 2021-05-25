# -*- coding: utf-8 -*-
"""
Created on Sat Dec 12 12:54:27 2020

@author: BlackLotus57
"""
import speech_recognition as sr
recognizer = sr.Recognizer()

with sr.Microphone() as inputs:
    print("Please speak now")
    listening = recognizer.listen(inputs)
    print("Analysing...")


try:
        print("Did you say: "+recognizer.recognize_google(listening))
except:
        print("please speak again")
