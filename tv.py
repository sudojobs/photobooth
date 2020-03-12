#-------------------------------
#imports
#-------------------------------
import os
import glob
import time
import datetime
import subprocess

from os import stat
from time import sleep
from os import listdir
from subprocess import check_output
from time import gmtime,strftime
from random import shuffle
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

if(len(vid_files)>0): 
   latest_file = max(vid_files, key=os.path.getctime)

if not (len(video_files) > 0):
   print ("No mp4 files found!")

#-------------------------------
# Main Loop
#-------------------------------
while True:
       #check the video files if new file is there update the video_files(array list)
       vid_files=glob.glob('./videos/*.mp4')
       #by default the process has been started and video playing
       if(len(vid_files)>0): 
          if(latest_file!= max(vid_files, key=os.path.getctime)):
             latest_file=max(vid_files,key=os.path.getctime)
             sorted_list=sorted(vid_files, key=lambda x: stat(x).st_mtime)
             hundred_list=reverse(sorted_list[-100:]) 
             print(hundred_list)
             extra_list=sorted_list[0:-99] 
             if (os.path.exists('playlist.txt')):
                 os.remove('playlist.txt')  
             with open('playlist.txt', 'w') as f: # Create the playlist file for ffpmpeg capt
                     for item in hundred_list:
                         f.write("%s\n" % item)
             for i in range (len(extra_list)):  # Rremove the extra files
                     os.remove(extra_list[i])
             subprocess.call(['ffmpeg','-f','concat','-i','playlist.txt','-c','copy','output.mp4'])
             subprocess.call(['killall','omxplayer.bin']) 

       subprocess.call(['omxplayer','--no-osd','--no-keys','--win', '1,1,500,400','-p','-o','hdmi', 'output.mp4'])
       #sleep(0); 
