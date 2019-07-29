# P2PCam
Class to retrieve camera images from cameras using the p2p protocol

First of all i just wrote it to work as a class, the original connection and retrieval process has been made by [Jheyman](https://github.com/jheyman/) in his [videosurveillance script](https://github.com/jheyman/videosurveillance/).
I rewrote it to run as a class instead of an application.

So i had this [chinese camera](https://nl.aliexpress.com/item/Phone-monitor-P2P-Free-DDNS-Ontop-RT8633-HD-1-4-CMOS-1-0MP-Network-IP-Camera/990524792.html) laying around, it had this feature that you could access it from outside your home without the need for port forwarding. However after a couple of years this brand dissappeared and with it their services so i couldn't connect to it outside of my own network using [this app](https://play.google.com/store/apps/details?id=x.p2p.cam).

Which made owning this camera quite useless. But i had since gotten into Home Asssistant and got the idea to get it working in there since my instance ran locally so it should be able to access the camera.

## Usage
```
import p2pcam
import cv2
import numpy as np

def saveFile(cam, jpeg):
    RGBImage = cv2.imdecode(np.fromstring(jpeg, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite('image.jpg', RGBImage)

camera = p2pcam.P2PCam(<own ip>, <camera ip>)
saveFile(camera, camera.retrieveImage())
```
## Methods and Variables
### Methods
Any methods that may be useful.

`camera.initialize()` Set some variables and attempt to connect to the camera for the first time.

`camera.retrieveImage()` Retrieve a jpeg string from the camera.

`camera.start()` Start a while true loop staying connected, this will not do anything if `onJpegReceived` isn't set.

`camera.loop()` Start a while loop doing `retrieveImage()` until a socket error occurs.
### Variables
Some variables you may want to set.

`camera.horizontal_flip` Flip camera horizontally. (if true requires numpy and cv2)

`camera.vertical_flip` Flip camera vertically. (if true requires numpy and cv2)

`camera.addTimeStamp` Add a timestamp to the image. (if true requires numpy and cv2)

`camera.debug` If true prints out some debugging information.


The port information will have to be set before initialisation.

`camera.UDP_PORT_HOST` Host udp port default: 5123

`camera.UDP_PORT_TARGET` Target udp port default: 5000

`camera.SOCKET_TIMEOUT` Sets the socket timeout in seconds.

`camera.NB_FRAGMENTS_TO_ACCUMULATE` How many packets to get a full image. If you put this number high you will get a higher quality image but it will take longer to retrieve. Default: 80

`camera.onJpegReceived` Callback that will be executed if a jpeg image is retrieved. first argument will be the camera class, the second argument will be the jpeg image string.
