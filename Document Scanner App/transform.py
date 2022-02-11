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
    
    
