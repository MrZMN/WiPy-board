# WiPy-board
It's about WiPy boards 

What I did in the whole peroid:
1. Get a WiPy board. (You can gain the detailed instructions of using it from www.pycom.io)
2. Follow the instructions. Initialize the board and you could start some interesting Python instructions on it!
3. Create an adafruit account. And establish your "Feed" and "Dashboard". You can see the detailed instructions in https://www.hackster.io/bucknalla/mqtt-micropython-044e77?ref=channel&ref_id=13739_trending___&offset=1
4. You need a software to connect the WiPy board and run the micropython code. I used Atom editor as the media. (With a package "Pymakr" installed.) Absolutely you could also just use a Pymakr software, and it also worked.
5. Try to connect the WiPy board with your computer! You can either use WiFi or just use serial port. If you choose the serial port, make sure that you have installed the FTDI driver. If you have any problems, please see the file "troubleshooting".
6. Access the file storage(In Atom, just "download".) and you'll see some files including "main.py". Remember to change the detials of it! (The method can be seen in the "main.py" in this repository.)
7. Don't forget to insert the "mqtt.py" in your "lib" folder! 
8. If you have finished the former steps, you are able to run your code in Atom! (Or other Pymakr software.) Run "mqtt.py" first. Then run "main.py". Wait for a few seconds.
9. It will run the method of MQTT library first, and after the WiPy board connects to the WiFi, it will send "Lights ON" and "Lights OFF" instructions to your adafruit account! And by simulation you can see the really light on and off in your dashboard!
