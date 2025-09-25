import cv2
#  load the image
image = cv2.imread("My_Creation_SunFlower_cut.png") # 1 -> color, 2 -> grayscale, -1 -> unchanged(Default)

if image is not None:
    H, w, c = image.shape
    print(f"The Loaded Image's\n\tHeight is {H}\n\tWidth is {w}\n\tChannels is {c}")
else:
    print("Load successfully...")