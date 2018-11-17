'''
Created on Nov 4, 2018

@author: CAU VANG
'''
from gtts import gTTS
import time
import os 

mytext = 'Tomorrow, and tomorrow, and tomorrow; creeps in this petty pace from day to day, until the last syllable of recorded time. And all our yesterdays have lighted fools the way to dusty'
#mytext = ' Tui là Trần Ngọc Tuyền. Lớp Khoa học máy tính 2015 '
# language in which you want to convert
language ='en'
#language='vi'

myobj = gTTS( text= mytext,lang = language,slow =False)

# saving the converted audio in mp3 file named
# welcome
myobj.save("welcome1.mp3")

os.System("mpg321 welcome1.mp3")

