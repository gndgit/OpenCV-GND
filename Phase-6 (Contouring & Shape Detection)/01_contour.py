"""CONTOUR : it helps to detect the edges of image and detect the shape;
it work only with Binary images; (Binary images mean 'Black & white image')
syntax :
contours, hierarchy = cv2.findcontours(image, mode, method)
                    -> image : source image
                    -> mode : Relatable mode . in which mode you want to detect
                            -> there is many functions are presennt but i discuss 3 only
                        -> RETR_list : it only return the edge points in a list without hierarchy
                        -> RETR_TREE : It for all , it return the edge points and also the hierarachy
                        -> RETR_EXTERNAL : It detect only the outer shape edge
"""
import cv2
import numpy as np

image =  cv2.imread(r"Collection_image\Circle.png")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) # convert image into gray
_, thresh = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY) 
''' the above code _ why use because this is a pyhthon syntax here python say "i dont care about the _ value" mean what ever a value store python ignore that value so programmer use '_' for ignore the value
eg : a, _, c = (4, 3, 8) # here the 3 is ignore by python bcz instad f that value use _ '''

# find contours
contours, heirarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # (threshold_img, mode, method)
                                # cv2.RETR_TREE: return the edges including heirarchy
                                # cv2.CHAIN_APPROX_SIMPLE: it store only corner points
# Draw the contours on original image
cv2.drawContours(image, contours, -1, (255,0,0), 4) # (image, contour_points_variable, contour_index(-1 for draw all shape), color, thickness)

cv2.imshow("Contours ", image)
cv2.waitKey(0)
cv2.destroyAllWindows()