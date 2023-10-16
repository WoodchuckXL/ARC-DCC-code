import cv2
import numpy as np

#Color range dictionary
colorRanges = {
    'red' : {
        'loweru' : np.array([176,128,128]),
        'upperu' : np.array([255,255,255]),
        'lowerl' : np.array([0,128,128]),
        'upperl' : np.array([7,255,255]) 
    },
    'orange' : {
        'lower' : np.array([8,128,128]),
        'upper' : np.array([20,255,255]) 
    },
    'yellow' : {
        'lower' : np.array([21,128,128]),
        'upper' : np.array([31,255,255]) 
    },
    'green' : {
        'lower' : np.array([32,128,128]),
        'upper' : np.array([82,255,255]) 
    },  
    'blue' : {
        'lower' : np.array([83,128,128]),
        'upper' : np.array([130,255,255]) 
    },
    'purple' : {
        'lower' : np.array([131,128,128]),
        'upper' : np.array([145,255,255]) 
    },
    'pink' : {
        'lower' : np.array([146,128,128]),
        'upper' : np.array([175,255,255]) 
    }
}

class ColorIdentifier:

    def createColorMask(img,color : str):
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        # Threshold the HSV image to get only blue colors
        if (color != 'red'):
            mask = cv2.inRange(hsv, colorRanges[color]['lower'], colorRanges[color]['upper'])
        else:
            mask1 = cv2.inRange(hsv, colorRanges[color]['lowerl'], colorRanges[color]['upperl'])
            mask2 = cv2.inRange(hsv, colorRanges[color]['loweru'], colorRanges[color]['upperu'])
            mask = mask1 | mask2

        # Bitwise-AND mask and original image
        res = cv2.bitwise_and(img,img, mask= mask)
        cv2.imshow('frame',img)
        cv2.imshow('mask',mask)
        cv2.imshow('res',res)

        cv2.waitKey()

    def getColorStr(color) -> str:
        hsv = cv2.cvtColor(np.uint8([[color]]), cv2.COLOR_BGR2HSV)[0][0]
        for key in colorRanges.keys():
            if (key == 'red'):
                if (all(hsv >= colorRanges['red']['loweru']) & all(hsv <= colorRanges['red']['upperu'])) | (all(hsv >= colorRanges['red']['lowerl']) & all(hsv <= colorRanges['red']['upperl'])): 
                    return key
            else:
                if (all(hsv >= colorRanges[key]['lower']) & all(hsv <= colorRanges[key]['upper'])): return key
        return None