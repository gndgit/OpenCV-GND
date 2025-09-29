"""                         --SHAPE DETECTION--
-> approxPolyDP() function is helps to detect the shape in cv.
-> This function simplify the corner in shape.
-> This Counting the corner present over shape.
-> Using the count corner value we pass our logic to detect the shape.
Syntax: cv2.approxPolyDP(contours, epsilon, True)
        -> contours: this variable store the points of shape it comes from cv2.findContours() fuction
        -> epsilon: it is a value to find how much you detect the shape closer to original
                - Fromula: 0.01 * cv2.arcLength(contiurs, True)
                    - This function simplified the shape and detect how much closer to original
                    - 0.01 value is epsilon:
                        - if you pass smaller value : than it more precise the shape and give more points
                        - if you pass large value it gives rough output, not accurate measure(if lower point present )
                        - Recomended to pass lower vakue so that it detect the shape more accurate
        -> True/False: True mean: it closer to points and gap-less join between points
                        False means it not closer and not gap-less
"""
import cv2
import numpy as np

image = cv2.imread(r"Collection_image\multiple_shape.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # gray conversion

_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)

# Finding the contour points
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
# Drawing the contours 
# cv2.drawContours(image, contours, -1, (0,0,255),4)

# detect the shape
for contour in contours:
    approx = cv2.approxPolyDP(contour, 0.01 * cv2.arcLength(contour,True), True)
                            # (Curve, epsilon, Closed: True|false)
                            # epsilon: 0.01 *cv2.arcLength(curve, Closed: True/False)
    corners = len(approx) # Find the total length of approx mean corners
    
    if corners == 3:
        shape_name = "Triangle"
    elif corners == 4:
        shape_name = "Rectangle"
    elif corners == 5:
        shape_name = "Pentagone"
    elif corners > 5:
        shape_name = "Circle"
    elif corners == 2:
        shape_name = "Line"
    else:
        shape_name = "Unknown"
    
    # how to write this i output
    cv2.drawContours(image, [approx], 0, (0,255, 0), 4) # [approx]: list of corners, 0 indx mean: work on first, color, thickness
    x = approx.ravel()[0] # ravel() if any multidimentional array present it convert into 1D array, & [0] mean fisrt element
    y = approx.ravel()[1] - 10 # why - 10 mean this all things are pixels so text shown in little bit gap between shape and text
    
    # X, Y contain pixel of image . what ever store the approx variable it store only the points (in pixels) so from approx list ot extract the first indec and second index value
    cv2.putText(image, shape_name, (x,y), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0,0,0), 2)
cv2.putText(image, "GND Detected", (10,15), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (10,10,10),2)
cv2.imshow("Shape Detected", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

