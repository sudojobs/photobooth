import os
import sys
from time import sleep
from omxplayer import OMXPlayer
from signal import pause



takevideo ='./videos/takphoto.mp4'

cam0='/dev/video0'
cam1='/dev/video1'

def main():
    while True:
        print("playing vid1")
        #Call Subprocess Video via Myplayer
        if (rfid_detected()==1):
            rfid_process()

def rfid_process():
    #play the webcam feed
    #count down on screen 3, 2, 1
    #click pic from cam0
    #click pic from cam1
    #loop Video MP4 "Processing Video"
    #overlay_water_mark via ImageMagic
    #create wigglegram mp4 video
    #play the video for 30 seconds
    #prints_outthe_photo
    #go back to "take a photo"
    #send output for approval
    #send mp4 to tv in bar

def rfid_detected():
    #take the input from rfid
    #if input is valid then
    #return 1
