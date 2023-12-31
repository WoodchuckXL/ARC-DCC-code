import cv2
import numpy as np

#Color range dictionary
colorRanges = {
    'red' : {
        'loweru' : np.array([146,150,64]),
        'upperu' : np.array([255,255,199]),
        'lowerl' : np.array([0,150,64]),
        'upperl' : np.array([7,255,199]) 
    },
    'pink' : {
        'lower' : np.array([140,50,150]),
        'upper' : np.array([170,255,255]),
    },
    'orange' : {
        'lower' : np.array([8,64,64]),
        'upper' : np.array([20,255,255]) 
    },
    'yellow' : {
        'lower' : np.array([21,64,64]),
        'upper' : np.array([31,255,255]) 
    },
    'light green' : {
        'lower' : np.array([32,64,170]),
        'upper' : np.array([82,255,255]) 
    },
    'dark green' : {
        'lower' : np.array([32,64,64]),
        'upper' : np.array([82,255,169]) 
    },
    'light blue' : {
        'lower' : np.array([83,64,170]),
        'upper' : np.array([120,160,255]) 
    },
    'dark blue' : {
        'lower' : np.array([83,160,64]),
        'upper' : np.array([120,255,255]) 
    },
    'purple' : {
        'lower' : np.array([121,30,64]),
        'upper' : np.array([145,255,255]) 
    },
    'black' : {
        'lower' : np.array([0,0,0]),
        'upper' : np.array([255,255,64]) 
    }
}

class ColorIdentifier:

    def createColorMask(self, img,color : str):
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

    def getColorStr(self, color) -> str:
        colorArr = np.uint8([[color]])
        hsv = cv2.cvtColor(colorArr, cv2.COLOR_RGB2HSV)[0][0]
        print(hsv)
        for key in colorRanges.keys():
            if (key == 'red'):
                if (all(hsv >= colorRanges['red']['loweru']) & all(hsv <= colorRanges['red']['upperu'])) | (all(hsv >= colorRanges['red']['lowerl']) & all(hsv <= colorRanges['red']['upperl'])): 
                    return key
            else:
                if (all(hsv >= colorRanges[key]['lower']) & all(hsv <= colorRanges[key]['upper'])): return key
        return None