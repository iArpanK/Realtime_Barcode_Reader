# Realtime Barcode Reader
---
Scans one-dimensional barcodes and QR codes in real-time from your phone's camera or computer's webcam. Can be run directly from your command-line or terminal. This application is built using Python 3.7 and uses the following libraries:

- OpenCV
- Pyzbar

### Dependencies
---
Install OpenCV
```sh
$-> pip install opencv-python
```
Install Pyzbar
```sh
$-> pip install pyzbar
```

### Running the Program
---
After all the required libraries have been installed, the program can be run as
```sh
$-> python realtime_barcode_reader.py --video <source>
```
In place of source, enter the URL of your IP Camera application. Format for this is ``` http://<IP_address>:<PORT>/video```. 
For example, I'm using an Android application called [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam) which shows these two instances.

![1616989007121](https://user-images.githubusercontent.com/80940234/112825314-3bad0680-90a9-11eb-8389-75bc66169550.jpg) ![1617037915127](https://user-images.githubusercontent.com/80940234/112928918-182f9d80-9135-11eb-86a0-a4bb33c35d63.jpg)
1. First instance : I connected my computer to my phone's personal hotspot
2. Second instance : I connected my computer & phone to a WiFi

So in the first instance, my source URL would be ```http://192.168.43.1:4747/video```. And the complete command would be
```sh
$-> python realtime_barcode_reader.py --video http://192.168.43.1:4747/video
```
And in the second instance, my source URL would be ```http://192.168.43.39:4747/video```. And the complete command would be
```sh
$-> python realtime_barcode_reader.py --video http://192.168.43.39:4747/video
```
> **NOTE** : In both these instances, note that your computer needs to be connected to the same network as your smartphone. Also, keep the IP Camera application running in your phone.

If you want to use your computer’s primary or secondary webcam as the video source, use source as 0 or 1 respectively, in the command above. For example, the below command starts your computer’s primary webcam as the video source.
```sh
$-> python realtime_barcode_reader.py --video 0
```
On punching either of these commands as per your choice, the **realtime_barcode_reader.py** program will start executing displaying a startup message on the command line, and your phone/computer will start streaming video feed. At the same time, a new window will open up on your computer screen displaying the barcode reader’s output stream (as shown below).

**Now we are ready to scan different barcodes!**

![Screenshot (171)](https://user-images.githubusercontent.com/80940234/112930070-444c1e00-9137-11eb-95df-a7448370d5db.png)

### Sample Runs
---
Attached below are some sample shots of the barcode reader.

![Untitled collage](https://user-images.githubusercontent.com/80940234/112828520-6bf6a400-90ad-11eb-9630-59833f24a1df.jpg)

### Log
---
On every run, this program generates a log file (log.txt) which contains the exact last session timestamp and details of the unique barcodes scanned.

![Screenshot (169)](https://user-images.githubusercontent.com/80940234/112828876-ed4e3680-90ad-11eb-8651-5d19a8f29fee.png)

### Notes
---
For IP Camera application, you can download either of these apps:

[DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam)

[IP Webcam](https://play.google.com/store/apps/details?id=com.pas.webcam)

[Google Drive download link (ipynb file included) ⤓](https://drive.google.com/drive/folders/1PxKK17r4U2jFhb8HkbiN57yTIwbqJ7qy?usp=sharing)

Thanks!
