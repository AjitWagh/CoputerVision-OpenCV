#CoputerVision-OpenCV
This project contains OpenCV Python Exercises
==============================================

###Introduction to OpenCV-Python Tutorials

OpenCV

OpenCV was started at Intel in 1999 by Gary Bradsky and the first release came out in 2000. Vadim Pisarevsky joined Gary Bradsky to manage Intel’s Russian software OpenCV team. In 2005, OpenCV was used on Stanley, the vehicle who won 2005 DARPA Grand Challenge. Later its active development continued under the support of Willow Garage, with Gary Bradsky and Vadim Pisarevsky leading the project. Right now, OpenCV supports a lot of algorithms related to Computer Vision and Machine Learning and it is expanding day-by-day.

Currently OpenCV supports a wide variety of programming languages like C++, Python, Java etc and is available on different platforms including Windows, Linux, OS X, Android, iOS etc. Also, interfaces based on CUDA and OpenCL are also under active development for high-speed GPU operations.

OpenCV-Python is the Python API of OpenCV. It combines the best qualities of OpenCV C++ API and Python language.

###Install OpenCV-Python

sudo apt-get install python-opencv
Open Python IDLE (or IPython) and type following codes in Python terminal.

import cv2 as cv
print(cv.__version__)
If the results are printed out without any errors, congratulations !!! You have installed OpenCV-Python successfully.

###Gui Features in OpenCV
1.Getting Started with Images
Goals : 
	Here, you will learn how to read an image, how to display it and how to save it back
     You will learn these functions : cv2.imread(), cv2.imshow() , cv2.imwrite()
     Optionally, you will learn how to display images with Matplotlib
#Using OpenCV : 
*Read an image :
	Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.

	Second argument is a flag which specifies the way image should be read.

	cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
	cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
	cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel
    See the code below:

	import numpy as np
	import cv2
	# Load an color image in grayscale
	img = cv2.imread('messi5.jpg',0)
*Display an image
	Use the function cv2.imshow() to display an image in a window. The window automatically fits to the image size.

	First argument is a window name which is a string. second argument is our image. You can create as many windows as you wish, but with 		different window names.
	Code :
	cv2.imshow('image',img)
	cv2.waitKey(0)
	cv2.destroyAllWindows()

cv2.waitKey() is a keyboard binding function. Its argument is the time in milliseconds. The function waits for specified milliseconds for any keyboard event. If you press any key in that time, the program continues. If 0 is passed, it waits indefinitely for a key stroke. It can also be set to detect specific key strokes like, if key a is pressed etc which we will discuss below.

cv2.destroyAllWindows() simply destroys all the windows we created. If you want to destroy any specific window, use the function cv2.destroyWindow() where you pass the exact window name as the argument.

See the code below:

cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

Write an image

Use the function cv2.imwrite() to save an image.
First argument is the file name, second argument is the image you want to save.
cv2.imwrite('messigray.png',img)
This will save the image in PNG format in the working directory.

--Sum it up--

Below program loads an image in grayscale, displays it, save the image if you press ‘s’ and exit, or simply exit without saving if you press ESC key.

import numpy as np
import cv2

img = cv2.imread('messi5.jpg',0)
cv2.imshow('image',img)
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k == ord('s'): # wait for 's' key to save and exit
    cv2.imwrite('messigray.png',img)
    cv2.destroyAllWindows()

Using Matplotlib

Matplotlib is a plotting library for Python which gives you wide variety of plotting methods. You will see them in coming articles. Here, you will learn how to display image with Matplotlib. You can zoom images, save it etc using Matplotlib.

import numpy as np
import cv2
from matplotlib import pyplot as plt

img = cv2.imread('messi5.jpg',0)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.show()



2.Getting Started with Videos : 

3.Drawing Functions in OpenCV
4.Mouse as a Paint-Brush
5.Trackbar as the Color Palette










