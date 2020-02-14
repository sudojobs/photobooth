import os
import sys
from time import sleep
from omxplayer import OMXPlayer
from gpiozero import MotionSensor
from signal import pause
from picamera import PiCamera

pir = MotionSensor(23)

camera = PiCamera()
vid1 = OMXPlayer('/home/pi/Videos/Vid_Wait_Loop1.mp4',args=['--win', '100 100 640 480','--loop'])
vid2 = OMXPlayer('/home/pi/Videos/Vid_Name_Hammerstein.mp4',args=['--win', '100 100 640 480'])

def main():
    initiate()
    while True:
        print("playing vid1")
        vid1.play()
        if pir.motion_detected:
            motion_detected()
        else:
            no_motion()
    except KeyboardInterrupt:
        print("terminated by user")
        vid1.quit()
        vid2.quit()
        camera.close()
            try:
                sys.exit(0)
            except SystemExit:
                os.exit(0)
    finally:
           vid1.quit()
           vid2.quit()
         camera.close()
     print("bye bye")

def initiate():
    print("CENTRAL AI Startup - Running initial setup")
    sleep(1)
    print("Starting Central AI visual front end")
    sleep(1)
    print("Motion detection activated")
    sleep(1)
    print("Security system activated")

def no_motion():
    print("All quiet")
    vid1.play()

def motion_detected():
    print("Intruder Detected")
    sleep(2)
    print("Pausing loop")
    vid1.pause()
    print("Playing Vid_Name_Hammerstein")
    vid2.play()
    sleep(10)
    vid2.pause()
