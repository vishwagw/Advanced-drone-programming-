#This file is for the openMV camer modules

#importing libraires
import cv2
import numpy as np
import sys, serial, struct,time # must install the serial lib

#we are creating  the opencamera class.
class openMVCamera() :

    def __init__(self, name, com) :
        self.name = name
        self.picture = None
        self.time = time.time()
        self.frame = 0

        self.display = True
        self.fps = None
        self.size = None

        self.serial = serial.Serial(com, baudrate=115200, bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE,
                                    xonxoff=False, rtscts=False, stopbits=serial.STOPBITS_ONE, timeout=None,
                                    dsrdtr=True) 
        
        self.serial.setDTR(True)  # dsrdtr is ignored on Windows.
        self.serial.write(b'wledd')
        self.contrast = round(4/7,2)
        self.brightness= round(4/7,2)
        self.saturation= round(4/7,2)
    
    #for photos
    def photos(self):
        

    #for videos
    def videos(self):
        while True:
            self.photo()
            keyCode = cv2.waitKey(1) & 0xff
            # Stop the program on the ESC key
            if keyCode == 27:
                break

        cv2.waitKey(0)
        cv2.destroyAllWindows()






