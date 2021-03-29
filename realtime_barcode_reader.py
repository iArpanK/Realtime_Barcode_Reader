#!/usr/bin/env python
# coding: utf-8

# In[1]:


# importing required libraries

from pyzbar import pyzbar
import argparse
import datetime
import cv2


# In[2]:


# defining the scan barcode function

def scanBarcodes(snap, barcodeList, log):
    
    # resizing the frame from the video stream
    snap = cv2.resize(snap, (640, 480))
    
    # finding & decoding barcodes in the frame
    barcodes = pyzbar.decode(snap)
    
    # iterating over the barcodes
    for b in barcodes:
        
        # storing barcode data & type
        # converting barcode data to string as it is a bytes object
        barcode_data = b.data.decode('utf-8')
        barcode_type = b.type
        
        # finding the rectangle locations bounding the barcode
        # and drawing the rectangle on the frame
        x, y, w, h = b.rect
        cv2.rectangle(snap, (x, y),(x + w, y + h), (0, 255, 0), 3)
        
        # setting the font & text, location, size, color, etc.
        # to be displayed on output frame
        font = cv2.FONT_HERSHEY_SIMPLEX
        text1 = "Type: {}".format(barcode_type)
        text2 = barcode_data
        cv2.putText(snap, text1, (x, y - 20), font, 0.6, (255, 0, 0), 2)
        cv2.putText(snap, text2, (x, y + h + 30), font, 0.6, (0, 0, 255), 2)
        
        # writing the unique barcodes in the log file & printing it
        if barcode_data not in barcodeList:
            status = "[Alert] New Barcode detected : {} ({})".format(barcode_data, barcode_type)
            log.write(status+'\n')
            print(status)
            barcodeList.add(barcode_data)
            
    return snap


# In[3]:


# defining the main function

def main():
    
    # argument parser to parse command line arguments
    ap = argparse.ArgumentParser()
    ap.add_argument("-v", "--video", required = True, help = "URL of your IP Camera (0/1 in case of primary/secondary webcam)")
    args = vars(ap.parse_args())
    
    # converting to int for primary & secondary camera src
    if args["video"] == '0' or args["video"] == '1':
        args["video"] = int(args["video"])
        
    
    # creating a set to contain unique barcodes
    barcodeList = set()
    
    # creating an object of VideoCapture with
    # source as the IP camera url
    print("[Alert] Starting Video...")
    cap = cv2.VideoCapture(args["video"])
    
    # creating a text file for storing session log
    log = open("log.txt", mode ='w')
    log.write("Log created : {}\n\n".format(datetime.datetime.now()))
    
    # frame gets the next frame from video stream
    # ret obtains the boolean return value from getting the frame
    ret, frame = cap.read()
    
    # while loop keeps running the scan barcode function
    # till the Esc key is pressed
    while ret:
        ret, frame = cap.read()
        frame = scanBarcodes(frame, barcodeList, log)
        cv2.imshow('Real-time Barcode Reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            log.close()
            break
            
    # releasing the object & closing the application window
    cap.release()
    cv2.destroyAllWindows()
    
# calling the main function to start the program
if __name__ == '__main__':
    main()

