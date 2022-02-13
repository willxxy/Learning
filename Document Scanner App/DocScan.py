from transform import four_point_transform
from skimage.filters import threshold_local
import numpy as np
import argparse
import cv2
import imutils


#construct the arg parse and parse arg

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
                help = "Path to the image to be scanned")
args = vars(ap.parse_args())
print(args)


#load image and compute ratio of old height to new height
#clone then resize

image = cv2.imread(args["image"])
ratio = image.shape[0] / 500.0
orig = image.copy()
image = imutils.resize(image, height = 500)

print(ratio)

#convert iamge to grayscale, blur it, and find edges in image

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)
edged = cv2.Canny(gray, 75, 200)


#show orig img and edge detected img

print("Edge Detection")
cv2.imshow("Image", image)
cv2.imshow("Edged", edged)
cv2.waitKey(0)
cv2.destroyAllWindows()



#find contours in edged image and keep only the larges one
#initialize screen contour 

cnts = cv2.findContours(edged.copy(), cv2.RETR_LIST,
                        cv2.CHAIN_APPROX_SIMPLE)
cnts = imutils.grab_contours(cnts)
cnts = sorted(cnts, key = cv2.contourArea, reverse = True)[:5]

#loop over contours

for c in cnts:
    
    #approx contours
    
    peri = cv2.arcLength(c, True)
    #approx = cv2.approxPolyDP(c, 80, True)

    approx = cv2.approxPolyDP(c, 0.02 * peri, True)
    
    #if approx contour has 4 points, then assume we found
    #screen
    
    if len(approx) ==4:
        screenCnt = approx
        break
        
#show contour (outline) of document

print("Contour Detection")
cv2.drawContours(image, [screenCnt], -1, (0, 255, 0), 3)
cv2.imshow("Outline", image)
cv2.waitKey(0)
cv2.destroyAllWindows()


#apply four point transform to obtain top down view of original image

warped = four_point_transform(orig, screenCnt.reshape(4, 2) * ratio)

#convert warped img to grayscale
#threshold it to give black and white color

warped = cv2.cvtColor(warped, cv2.COLOR_BGR2GRAY)
T = threshold_local(warped, 11, offset = 10, method = "gaussian")
warped = (warped > T).astype("uint8")*255



#show original img and scanned img

print("Apply perspective transform")
cv2.imshow("Original", imutils.resize(orig, height = 650))
cv2.imshow("Scanned", imutils.resize(warped, height= 650))
cv2.waitKey(0)

    
    
