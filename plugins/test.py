import numpy as np
import cv2

def execute(image):
    open_cv_image = cv2.cvtColor(image,cv2.COLOR_RGBA2BGR).copy()
    # print(len(image))
    #print(open_cv_image)
    gray = cv2.cvtColor(open_cv_image, cv2.COLOR_BGR2GRAY)
    #cv2.imshow('t', np.asarray(image[0]))
    #cv2.waitKey()
    fm = np.var(cv2.Laplacian(gray, cv2.CV_64F))
    return ("lap_variance", fm, "double")
