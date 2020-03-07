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
       #check the video files if new file is there update the video_files(array list)
       #by default the process has been started and video playing
       subprocess.call(['omxplayer','--no-osd','--no-keys','-p','-o','hdmi', video_files[stateindex]])
    
       #after 1st mp4 file played we have increase the index size by 1 
       stateindex += 1
     
       #loop if all the files are played if number is less than  99
       if stateindex >= len(video_files):
          stateindex = 0
       elis stateindex >=99:
          stateindex = 0
       
       sleep(0); 
