   The followings are the problems I've met and the corresponding solutions:

1. The Atom problem: How to install the package "Pymakr" in your Atom editor? (Windows)
   
   For the instructions in "www.pycom.io" are for Mac, you may find it hard to follow the exact instructions. Don't worry, just finish it in your software! In Atom of Windows, choose "Packages" after you log in for the first time. Then search "Pymakr" and select "Install". Because the network may not be stable, you need to be patient.
   Certainly, if you use other Pymakr softwares, you won't meet this problem.

2. How to connect your WiPy board via serial port?
   
   1. Choose "More" on the REPL and choose "Get serial ports". Then it'll show you the name of the serial port you are using. (For me, it's COM3. In Mac it could be a totally different shape.)
   2. Choose "Settings", then select "Global settings". In this page, you need to change the information in "Device address" (Default: 192.168.4.1)to the name of serial port. (For me, it's COM3.)
   
   Try again. If it still doesn't work, access the storage and you'll find the file "pymakr.conf". Open it and change the information "address": "192.168.4.1" to "address": "COM3".
   
   If it still doesn't work, check if your FTDI driver works correctly. If necessary, use a serial assistant(For example: PuTTY). You can see the details in https://micropython.org/resources/docs/en/latest/wipy/wipy/tutorial/repl.html
   
   
3. There are problems when I run "main.py"?
   
   If you got your "main.py" from the other side, you may face this problem. Cause sometimes your editor doesn't support the command "from mqtt import MQTTClient". And the solution is easy, just "import mqtt".
   
4. The light in "io.adafruit.com" doesn't change color? For the code already works in my editor.
   
   You know, there may be delays. You could refresh for some times. Besides, in your adafruit account, you could also have a look at your "Monitor". You could find the real-time information there.
   
#These are the problems I've met. If you have any other problems, please tell me and let's work it out.
#If I invade the athority, please tell me.
