import argparse
import cv2
import numpy as np
import math
import os
from model_loader import *




#min number of matches that have to be found
#to consider the recognition is valid

min_matches = 10
default_color = (0,0,0)

def load():
    """
    This function loads target surface img
    """

    homography = None
    
    #matrix of camera parameters (tune)
    
    camera_parameters = np.array([[800, 0, 320], [0, 800, 240], [0, 0, 1]])
    
    #create cv ORB keypoint detector
    
    orb = cv2.ORB_create()
    
    #create BFMatcher object based on hamming distance
    
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck = True)
    
    #load reference model that will search video
    
    dir_name = os.getcwd()
    model = cv2.imread(os.path.join(dir_name, 'reference_models/poly_low.jpeg'), 0)
    
    #compute model keypoints and descriptors
    
    kp_model, desc_model = orb.detectAndCompute(model, None)
    
    #Load 3D model from OBJ file
    
    obj = OBJ(os.path.join(dir_name, '3D_models/steve-obj/steve.obj'), swapyz = True)
    
    #init video capture
    
    cap = cv2.VideoCapture(0)
    
    while True:
        
        #read current frame
        
        ret, frame = cap.read()
        if not ret:
            print("Unable to capture video")
            return
        
        #find and draw keypoints of frame
        
        kp_frame, desc_frame = orb.detectAndCompute(frame, None)
        
        #match frame descriptors with model descriptors
        
        matches = bf.match(desc_model, desc_frame)
        
        #sort by distance
        #the lower the distance, the better the match
        
        matches = sorted(matches, key=lambda x: x.distance)
        
        #compute Homography if enough matches are found
        if len(matches) > min_matches:
            
            #differenciate between source point and destination point
            
            src_pts = np.float32([kp_model[m.queryIdx].pt for m in matches]).reshape(-1, 1, 2)
            dst_pts = np.float32([kp_frame[m.trainIdx].pt for m in matches]).reshape(-1, 1, 2)
            
            #compute homography
            
            homography, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
            if args.rectangle:
                
                #draw rectangle that marks the found model in the frame
                
                h, w = model.shape
                pts = np.float32([[0, 0], [0, h-1], [w-1, h-1], [w-1, 0]]).reshape(-1, 1, 2)
                
                #project corners into frame
                
                dst = cv2.perspectiveTransform(pts, homography)
                
                #connect them with lines
                
                frame = cv2.polylines(frame, [np.int32(dst)], True, 255, 3, cv2.LINE_AA)
                
                #if valid homography matrix was found render cube on model plane
                
            if homography is not None:
                try:
                    
                    #obtain 3D projection matrix from homography matrix and camera parameters
                    projection - projection_matrix(camera_parameters, homography)
                    
                    #project cube or model
                    
                    frame = render(frame, obj, projection, model, False)
                    
                    #frame = render(frame, model, projection)
                except:
                    pass
                
            #draw first 10 matches
            
            if args.matches:
                frame =cv2.drawMatches(model, kp_model, frame, kp_frame, matches[:10], 0, flags=2)
                
                #show result
                cv2.imshow('frame', frame)
                
                if cv2.waitKey(1) & 0xFF == ord('q'):
                    break
        else:
            print("Not enough matches found - %d/%d" % (len(matches), min_matches))
    
    cap.release()
    cv2.destroyAllWindows()
    return 0



def render(img, obj, projection, model, color = False):
    """
    Render a loaded obj model into the current video frame
    """
    
    vertices = obj.vertices
    scale_matrix = np.eye(3) * 3
    h, w = model.shape
    
    for face in obj.faces:
        face_vertices = face[0]
        points = np.array([vertices[vertex - 1] for vertex in face_vertices])
        points = np.dot(points, scale_matrix)
        
        #render model in middle of reference model, model points must be displaced
        
        points = np.array([[p[0] + w / 2, p[1] + h / 2, p[2]] for p in points])
        dst = cv2.perspectiveTransform(points.reshape(-1, 1, 3), projection)
        imgpts = np.int32(dst)
        if color is False:
            cv2.fillConvexPoly(img, imgpts, DEFAULT_COLOR)
        else:
            color = hext_to_rgb(face[-1])
            color = color[::-1] #reverse
            cv2.fillConvexPoly(img, imgpts, color)
            
    return img




def projection_matrix(camera_parameters, homography):
    """
    from the camera calibration matrix and the estimated homography
    compute the 3D projection matrix
    """

    #compute rotation along x and y axis as well as the translation
    
    homography = homography * (-1)
    rot_and_transl = np.dot(np.linalg.inv(camera_parameters), homography)
    col_1 = rot_and_transl[:, 0]
    col_2 = rot_and_transl[:, 1]
    col_3 = rot_and_transl[:, 2]
    
    #normalise vectors
    
    l = math.sqrt(np.linalg.norm(col_1, 2) * np.linalg.norm(col_2, 2))
    rot_1 = col_1 / l
    rot_2 = col_2 / l
    translation = col_3 / l
    
    #compute the orthonormal basis
    
    c = rot_1 + rot_2
    p = np.cross(rot_1, rot_2)
    d = np.cross(c, p)
    
    rot_1 = np.dot(c / np.linalg.norm(c, 2) + d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
    rot_2 = np.dot(c / np.linalg.norm(c, 2) - d / np.linalg.norm(d, 2), 1 / math.sqrt(2))
    rot_3 = np.cross(rot_1, rot_2)
    
    #compute 3D projection matrix from model to current frame
    
    projection = np.stack((rot_1, rot_2, rot_3, translation)).T
    return np.dot(camera_parameters, projection)


def hex_to_rgb(hex_color):
    """
    convert hex strings to RGB
    """
    
    hex_color = hex_color.lstrip('#')
    h_len = len(hex_color)
    return tuple(int(hex_color[i:i + h_len // 3], 16) for i in range(0, h_len, h_len//3))


#comman line arg parse
    
    
    
parser = argparse.ArgumentParser(description='Augmented reality application')

parser.add_argument('-r','--rectangle', help = 'draw rectangle delimiting target surface on frame', action = 'store_true')
parser.add_argument('-mk','--model_keypoints', help = 'draw model keypoints', action = 'store_true')
parser.add_argument('-fk','--frame_keypoints', help = 'draw frame keypoints', action = 'store_true')
parser.add_argument('-ma','--matches', help = 'draw matches between keypoints', action = 'store_true')

#parser.add_argument('-mo','--model', help = 'Specify model to be projected', action = 'store_true')

args = parser.parse_args()

if __name__ == '__main__':
    load()







