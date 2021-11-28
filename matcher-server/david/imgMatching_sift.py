import cv2
import numpy as np
import matplotlib.pyplot as plt
import os

bf = cv2.BFMatcher()
def calculateMatches(des1,des2,k=2,t=0.9):
    matches = bf.knnMatch(des1,des2,k=k)
    topResults1 = []
    for m,n in matches:
        if m.distance < t*n.distance:
            topResults1.append([m])
            
    matches = bf.knnMatch(des2,des1,k=k)
    topResults2 = []
    for m,n in matches:
        if m.distance < t*n.distance:
            topResults2.append([m])
    
    topResults = []
    for match1 in topResults1:
        match1QueryIndex = match1[0].queryIdx
        match1TrainIndex = match1[0].trainIdx

        for match2 in topResults2:
            match2QueryIndex = match2[0].queryIdx
            match2TrainIndex = match2[0].trainIdx

            if (match1QueryIndex == match2TrainIndex) and (match1TrainIndex == match2QueryIndex):
                topResults.append(match1)
    return topResults

def find_similar_images(currImage, DBpath):
    def is_image(filename):
        f = filename.lower()
        return f.endswith(".png") or f.endswith(".jpg") or f.endswith(".jpeg") or f.endswith(".bmp") or f.endswith(".gif") or f.endswith(".svg")
    
    if(is_image(currImage)):
        image_filenames = []
        for userpath in DBpath:
            image_filenames += [os.path.join(userpath, path) for path in os.listdir(userpath) if is_image(path)]
        
        results = {}
        sift=cv2.SIFT_create()

        img1=cv2.imread(currImage,4)

        for y in image_filenames:

            img2=cv2.imread(y,4)

            # find the keypoints and descriptors with SURF
            kp1, des1 = sift.detectAndCompute(img1,None)
            kp2, des2 = sift.detectAndCompute(img2,None)

            # BFMatcher with default params
            matches = calculateMatches(des1,des2)

            results[y] = 100 * (len(matches)/min(len(kp1),len(kp2)))

        return sorted([(k,results[k]) for k in results], key = lambda x: x[1], reverse=True)

foto = "foto_botella.jpg"
print(find_similar_images(foto,["."]))