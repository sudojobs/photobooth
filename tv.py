#-------------------------------
#imports
#-------------------------------
import os
import glob
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

def reverse(lst): 
    lst.reverse() 
    return lst 
#-------------------------------

video_files = [ f for f in listdir('./videos') if f[-4:] == '.mp4' ]
video_files_tmp = [ f for f in listdir('./videos') if f[-4:] == '.mp4' ]
vid_files=glob.glob('./videos/*')
latest_file = max(vid_files, key=os.path.getctime)

if not (len(video_files) > 0):
    print ("No mp4 files found!")

#-------------------------------
#function for video skip
#-------------------------------

def videoskip(channel):
    subprocess.call(['killall', 'omxplayer.bin'])

#-------------------------------
#function for concatenate
#-------------------------------

def concatenate():
	stringa = "ffmpeg -i \"concat:"
	elenco_video = glob.glob("*.mp4")
	elenco_file_temp = []
	for f in elenco_video:
		file = "temp" + str(elenco_video.index(f) + 1) + ".ts"
		os.system("ffmpeg -i " + f + " -c copy -bsf:v h264_mp4toannexb -f mpegts " + file)
		elenco_file_temp.append(file)
	print(elenco_file_temp)
	for f in elenco_file_temp:
		stringa += f
		if elenco_file_temp.index(f) != len(elenco_file_temp)-1:
			stringa += "|"
		else:
			stringa += "\" -c copy  -bsf:a aac_adtstoasc output.mp4"
	print(stringa)
	os.system(stringa)    

#-------------------------------
# Main Loop
#-------------------------------
while True:
       #check the video files if new file is there update the video_files(array list)
       vid_files=glob.glob('./videos/*')
       #by default the process has been started and video playing
       if(latest_file!= max(vid_files, key=os.path.getctime)):
          video_files_tmp = [ f for f in listdir('./videos') if f[-4:] == '.mp4' ]
          video_files=reverse(video_files_tmp)
          latest_file=max(vid_files,key=os.path.getctime)
          stateindex=0
 
 
       subprocess.call(['omxplayer','--no-osd','--no-keys','-p','-o','hdmi', video_files[stateindex]])
 
       #after 1st mp4 file played we have increase the index size by 1 
       stateindex += 1
     
       #loop if all the files are played if number is less than  99
       if stateindex >= len(video_files):
          stateindex = 0
       elif stateindex ==99:
          stateindex = 0
       
       sleep(0); 
