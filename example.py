#!/usr/bin/env python3
import p2pcam as Camera
import cv2
import numpy as np

def saveFile(cam, jpeg):
    RGBImageNext = cv2.imdecode(np.fromstring(jpeg, dtype=np.uint8), cv2.IMREAD_COLOR)
    cv2.imwrite('image.jpg', RGBImageNext)


camera = Camera.P2PCam("192.168.178.28", "192.168.178.9")
camera.NB_FRAGMENTS_TO_ACCUMULATE = 20
# camera.SOCKET_TIMEOUT = 20
# camera.debug = True

# Loop in scripts loop. Not recommended since you are lacking control.

# camera.onJpegReceived = saveFile
# camera.start()

# Synchronously fetch image from camera (asynchronous is not in the package yet.)
#
# Initialisation is not needed since it initialises in the retrieveImage function as well
# camera.initialize()
# saveFile(camera, camera.retrieveImage())

# A loop to keep retrieving pictures. initialisation is needed since otherwise socket_error will not be set.

camera.initialize()
while camera.socket_error == False:
    try:
        jpeg = camera.retrieveImage()
        print('got an image!')
        saveFile(camera, jpeg)
    except KeyboardInterrupt:
        raise
    except Exception as e:
        print(("[ERROR] " + str(e)))
        pass
