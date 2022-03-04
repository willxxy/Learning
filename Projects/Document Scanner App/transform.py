import cv2
import numpy as np


def order_points(pts):
    
    #initialize list of coordinates that will be ordered such that
    #the first entry in the list is the top left, the second entry
    #is the top right, third is bottom right, fourth is bottom left
    
    
    rect = np.zeros((4,2), dtype = 'float32')

    #top left point will have the smallest sum
    #bottom right will have largest sum

    s = pts.sum(axis = 1)

    rect[0] = pts[np.argmin(s)]
    rect[2] = pts[np.argmax(s)]

    #compute  difference between points
    #top right point will have smallest difference
    #bottome left will have the largest difference

    diff = np.diff(pts, axis = 1)
    rect[1] = pts[np.argmin(diff)]
    rect[3] = pts[np.argmax(diff)]

    #return ordered coordinates
    return rect



def four_point_transform(image, pts):

    #obtain a consistent order of the points and unpack them individually

    rect = order_points(pts)
    #tl - top left
    (tl, tr, br, bl) = rect

    #compute width of new image, which is max distance between br and bl
    #x coordinates or tr and tl x coordinates

    widthA = np.sqrt(((br[0]-bl[0] ** 2) + ((br[1] - bl[1]) **2)))
    widthB = np.sqrt(((tr[0]-tl[0] ** 2) + ((tr[1] - tl[1]) **2)))
    maxWidth = max(int(widthA), int(widthB))


    #compute height of new image, which is max distance between tr and br
    #y coordinates or tl and bl y coordinates
    heightA = np.sqrt(((tr[0] - br[0]**2) + ((tr[1] - br[1]) **2)))
    heightB = np.sqrt(((tl[0] - bl[0] **2) + ((tl[1] - bl[1]) **2)))
    maxHeight = max(int(heightA), int(heightB))

    #constructing set of points for top down view

    dst = np.array([
        [0, 0],
        [maxWidth - 1, 0],
        [maxWidth - 1, maxHeight - 1],
        [0, maxHeight - 1]], dtype = 'float32')

    #compute perspective transform matrix
    M = cv2.getPerspectiveTransform(rect, dst)
    warped = cv2.warpPerspective(image, M, (maxWidth, maxHeight))

    #return warped iamge
    return warped
















    
    
