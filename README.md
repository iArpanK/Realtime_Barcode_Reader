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
For example, I'm using an Android application called [DroidCam](https://play.google.com/store/apps/details?id=com.dev47apps.droidcam) which at an instance shows this page.

![1616989007121](https://user-images.githubusercontent.com/80940234/112825314-3bad0680-90a9-11eb-8389-75bc66169550.jpg)

So, in this instance my source URL would be ```http://100.83.0.70:4747/video```. And the complete command would be
```sh
$-> python realtime_barcode_reader.py --video http://100.83.0.70:4747/video
```
If you want to use your computer’s primary or secondary webcam as the video source, use source as 0 or 1 respectively, in the command above. For example, the below command starts your computer’s primary webcam as the video source.
```sh
$-> python realtime_barcode_reader.py --video 0
```
On punching either of these commands as per your choice, the **realtime_barcode_reader.py** program will start executing displaying a startup message on the command line, and your phone/computer will start streaming video feed. At the same time, a new window will open up on your computer screen displaying the barcode reader’s output stream.
**Now we are ready to scan different barcodes!**

![Screenshot (133)](https://user-images.githubusercontent.com/80940234/112826604-d823d880-90aa-11eb-9dd4-973ea31aae55.png)

### Sample Runs
---
Attached below are some sample shots.

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
