#-------------------------------
#imports
#-------------------------------
import os
import time
import datetime
import subprocess

from time import sleep
from os import listdir
from subprocess import check_output
from time import gmtime,strftime
#from omxplayer import OMXPlayer
from omxplayer.player import OMXPlayer
#-------------------------------
#initialization
#-------------------------------
stateindex  = 0

#-------------------------------
# video files in directory
#-------------------------------

video_files = [ f for f in listdir('./videos') if f[-4:] == '.mp4' ]
 
if not (len(video_files) > 0):
    print ("No mp4 files found!")

#-------------------------------
#function for video skip
#-------------------------------

def videoskip(channel):
    subprocess.call(['killall', 'omxplayer.bin'])

#-------------------------------
# Main Loop
#-------------------------------
while True:
       #by default the process has been started and video playing
       subprocess.call(['omxplayer','-quit', video_files[stateindex]])
    
       #after 1st mp3 file played we have increase the index size by 1 
       stateindex += 1
     
       #loop if all the files are played
       if stateindex >= len(video_files):
          stateindex = 0

       #logic for time check and On/Off night lamp
       sleep(0); 
