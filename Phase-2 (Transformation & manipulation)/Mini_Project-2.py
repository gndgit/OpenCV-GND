""" Target :: Project :: User Friendly
--> take input image location from user
--> give user to options what they want to do with his/her image
--> options are  1> Draw line
                2> Draw circle
                3> Draw Rectangle
                4> Add any text in Image
"""
# importing the required library
import cv2

print("\n\n\t\t\t\t\t :::WELCOME TO GND IMAGE APPLICATION:::")
print("\t\t\t\t\t\t ::: Mini Project - 2 :::\n")
path = input("\t |- Enter path/location of your Image: ")
image = cv2.imread(path)

if image is None:
    print("\n\n\t\t Error: Image Not Found!!!\n")
    print("\t\t Please check your Image Location, Please Use again...\n")
else:
    print("\n\t\t\t\t\t Image Loaded successfully. ")
    H,W,C = image.shape
    print("\t\t\t\t      Welcome to our Mini Project - 2")
    print("\t\t----------------------------------------------------------------------------\n")
    print(f"\n\t\tYour Image's |- Height: {H}px\t |- Width: {W}px\t |- channel: {C} color mix\n")
    print("\t\t |- Please Choose One from below:")
    print("\t\t\t |- <1> for DRAW LINE")
    print("\t\t\t |- <2> for DRAW RECTANGLE")
    print("\t\t\t |- <3> for DRAW CIRCLE")
    print("\t\t\t |- <4> for ADD TEXT TO YOUR IMAGE")
    print("\t\t\t |- <5> for Resize (OR) Cropping the image")
    choice = input("\t\t\t\t\t |- Your Choice: ")
    
    if choice == "1":
        print("\t\t----------------------------------------------------------------------------\n")
        print("\t\t\t\tYou Select <1> for Draw LINE")
        pt1 = eval(input("\t\tEnter Point 1's x1 and y1 coordinate in pixels (Only int): "))
        pt2 = eval(input("\t\tEnter Point 2's x2 and y2 coordinate in pixels (Only int): "))
        color = eval(input("\t\tEnter color in (Blue, Green, Red) format-each range 0-255: "))
        thickness = int(input("\t\t Enter Thickness of your line in pixel- singe value: "))
        cv2.line(image,pt1,pt2,color,thickness)
        while(True):
            select = input("\n\t\t\t 1 for show the Image\n\t\t\t 2 for Show & Save the image\n\t\t\t\t Your Choise : ")
            if select == '1':
                print("\t\t Showing the image")
                cv2.imshow("Line Draw On Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            elif select == '2':
                print("\t\t Showing & Saving the image")
                name = input("\t\t\t Enter your image name to save: ")
                cv2.imwrite(f"{name}",image)
                cv2.imshow(f"{name}", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            else:
                print("\n\t\t\t\t Invalid Input: Please enter correct input.")
    elif choice == '2':
        print("\t\t----------------------------------------------------------------------------\n")
        print("\t\t\t\tYou Select <2> for Draw RECTANGLE")
        pt1 = eval(input("\n\t\t |- Enter Point-1 (Left-top corner) value x,y: "))
        pt2 = eval(input("\n\t\t |- Enter Point-2 (Right-button corner) value x,y: "))
        color = eval(input("\n\t\t |- Enter Color B G R format Range(0-255): "))
        thickness = int(input("\n\t\t |- Enter Thickness in px: "))
        while True:
            fill = input(' Are you fill the Rectangle(y or n): ')
            if fill == 'y':
                thickness = -1
                cv2.rectangle(image, pt1, pt2, color, thickness)
                cv2.imshow("Rectangle Full Fill Image",image)
                print("\n\t\t || Rectangle Image full fill showing...")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            elif fill == 'n':
                cv2.rectangle(image, pt1, pt2, color, thickness)
                cv2.imshow("Rectangle Image",image)
                print("\n\t\t || Rectangle Image showing...")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            else:
                print("\n\t\t Enter Valid Key According to instruction")
        
    elif choice == '3':
        print("\t\t----------------------------------------------------------------------------\n")
        print("\t\t\t\tYou Select <3> for Draw CIRCLE")
        center = eval(input("\n\t\t |- Enter center Point value x,y: "))
        radious = int(input("\n\t\t |- Enter Radious in px: "))
        color = eval(input("\n\t\t |- Enter Color B G R format Range(0-255): "))
        thickness = int(input("\n\t\t |- Enter Thickness in px: "))
        while True:
            fill = input(' Are you fill the Circle(y or n): ')
            if fill == 'y':
                thickness = -1
                cv2.circle(image, center, radious, color, thickness)
                cv2.imshow("Circle Full Fill Image",image)
                print("\n\t\t || Circle Image full fill showing...")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            elif fill == 'n':
                cv2.circle(image, center, radious, color, thickness)
                cv2.imshow("Circle Image",image)
                print("\n\t\t || Circle Image showing...")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            else:
                print("\n\t\t Enter Valid Key According to instruction")
    elif choice == '4':
        print("\t\t----------------------------------------------------------------------------\n")
        print("\t\t\t\tYou Select <4> for Draw Add TEXT to your Image")
        text = input("\n\t\t |- Enter Text to add in photo: ")
        org = eval(input("\n\t\t |- Enter Position Point x, y value in px: "))
        font = cv2.FONT_HERSHEY_SIMPLEX
        scale = 3
        color = eval(input("\n\t\t |- Enter Text Color in B, G, R format: "))
        thickness = int(input("\n\t\t |- Enter text's Thickness in px: "))
        cv2.putText(image, text, org, font, scale, color,thickness)
        while(True):
            select = input("\n\t\t\t 1 for show the Image\n\t\t\t 2 for Show & Save the image\n\t\t\t\t Your Choise : ")
            if select == '1':
                print("\t\t Showing the image")
                cv2.imshow("Text Added On Image", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            elif select == '2':
                print("\t\t Showing & Saving the image")
                name = input("\t\t\t Enter your image name to save: ")
                print("\t\t Showing and Saving the image")
                cv2.imwrite(f"{name}",image)
                cv2.imshow(f"{name}", image)
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                break
            else:
                print("\n\t\t\t\t Invalid Input: Please enter correct input.")   
    elif choice == '5':
        print("\t\t----------------------------------------------------------------------------\n")
        print("\t\t\t\tYou Select <5> for Resize (OR) Cropping the image")
        print("\n\t\t |- 1 for Resize the image")    
        print("\t\t |- 2 for Cropping the image")
        select = input("\t\t\t\t |- Your Choice :")
        if select == '1':
            print("\n\t\t You Select Resizing the Image. ")
            size = eval(input("\t\t |- Enter How many size you eant in pixel width, height: "))
            resize_image =  cv2.resize(image, size)
            while(True):
                select = input("\n\t\t\t 1 for show the Image\n\t\t\t 2 for Show & Save the image\n\t\t\t\t Your Choise : ")
                if select == '1':
                    print("\t\t Showing the image")
                    cv2.imshow("Resized Image", resize_image)
                    cv2.imshow("Original Image", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    break
                elif select == '2':
                    print("\t\t Showing & Saving the image")
                    name = input("\t\t\t Enter your image name to save: ")
                    print("\t\t Showing and Saving the image")
                    cv2.imwrite(f"{name}",resize_image)
                    cv2.imshow(f"{name}", resize_image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    break
                else:
                    print("\n\t\t\t\t Invalid Input: Please enter correct input.")
        elif select == '2':
            print("\n\t\t You Select cropping the Image. ")
            starty = int(input("\n\t\t |- Enter start Y point: "))
            endy = int(input("\n\t\t |- Enter end Y point: "))
            startx = int(input("\n\t\t |- Enter start X point: "))
            endx = int(input("\n\t\t |- Enter end X point: "))
            cropped = image [starty:endy, startx:endx]
            while(True):
                select = input("\n\t\t\t 1 for show the Image\n\t\t\t 2 for Show & Save the image\n\t\t\t\t Your Choise : ")
                if select == '1':
                    print("\t\t Showing the image")
                    cv2.imshow("Cropped Image", cropped)
                    cv2.imshow("Original Image", image)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    break
                elif select == '2':
                    print("\t\t Showing & Saving the image")
                    name = input("\t\t\t Enter your image name to save: ")
                    print("\t\t Showing and Saving the image")
                    cv2.imwrite(f"{name}",cropped)
                    cv2.imshow(f"{name}", cropped)
                    cv2.waitKey(0)
                    cv2.destroyAllWindows()
                    break
                else:
                    print("\n\t\t\t\t Invalid Input: Please enter correct input.")
            
    else:
        print("Invalid Input Please Select CORRECT input.")
        