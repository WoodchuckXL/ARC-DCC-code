import numpy as np

"""
This code is only used to store camera matrix and distance coefficient data for the drones we are using.
If a drone not listed here needs to run this file, then it needs to be calibarated, and the results should be added here.
"""

# Camera Matrices for the drones our team is using.
cameraMatrix97 = np.array([[907.58839883, 0., 479.23143996],
                           [0., 906.60788285, 357.19406609],
                           [0., 0., 1.]])
cameraMatrixF5 = np.array([[923.98915213, 0., 469.69065169],
                           [0., 922.72523926, 342.54322594],
                           [0., 0., 1.]])
cameraMatrixFC = np.array([[914.50777095, 0., 500.62865674],
                           [0., 915.64647849, 350.32158452],
                           [0., 0., 1.]])

cameraMatrices = {
    "97": cameraMatrix97,
    "F5": cameraMatrixF5,
    "FC": cameraMatrixFC
}

# Distance coefficients for the drones we are using
distCoeff97 = np.array([[-1.56851774e-01, 1.87229360e+00, 1.17708648e-03, -2.78244208e-03, -7.73842410e+00]])
distCoeffF5 = np.array([[2.51357081e-01, -5.02994320e+00, -7.72284927e-04, 1.42386601e-04, 3.01352728e+01]])
distCoeffFC = np.array([[7.90431059e-02, -1.04308176e+00, -2.32651721e-03, 2.48823110e-03, 3.44641074e+00]])

distCoeffs = {
    "97" : distCoeff97,
    "F5" : distCoeffF5,
    "FC" : distCoeffFC
}