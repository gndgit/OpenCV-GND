""" Project -1 (Mini Project)
Project Idea and targets:
    1> Take user input location to load the image
    2> Ask to user to convert the image into gray scale or not
    3> ask user to show the image or save the image
            --> If save the image than take user input the Output filename
            --> than display the massage to user the file_name(user which is input to save) saved successfully...
            --> than another massage Thank you to using our Program, please use our program repeatedly, Thank you from GND Team
"""
""" CODE:::"""

# importing Required library
import cv2 
print("\n\n\t\t\t\t\t :::WELCOME TO GND IMAGE APPLICATION:::\n")
input_img = input("\t |- Enter path/location of your Image: ")
image = cv2.imread(input_img)

if image is not None:
    print("\tYour Image is successfully loaded.\n\t\t\t\t___Entering into our Application___")
    gray = input("\n\tAre you Convert your image into GRAYSCALE (y/n): ")
    if gray == 'n':
        print('\n\tPlease Choose one:')
        choose = input("\tEnter\t|- 1 for SHOW IMAGE\n\t\t|- 2 for SAVE IMAGE\n\t\t|- 3 for SAVE & SHOW IMAGE\n\t\t\t\t\t Your choice: ")
        if choose == "1":
            print("\tYou choice option 1 : SHOW IMAGE")
            cv2.imshow("Normal Image ",image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("\tThank You Use Our Application..\n\t\t To USE again Please Run Again OUR application....")
        elif choose == "2":
            print("You choice option 2 : SAVE IMAGE")
            name = input("Enter image name to SAVE with extension: ")
            success = cv2.imwrite(f"{name}",image)
            if success:
                print(f"Successfully Saved the image in {name} Name.")
                print("Thank you for use Our Application.")
            else:
                print("!!Error: File Not saved on local system")
        elif choose == "3":
            print("You choice option 3 : SAVE & SHOW IMAGE")
            name = input("Enter image name to SAVE with extension: ")
            success = cv2.imwrite(f"{name}",image)
            if success:
                print(f"Successfully Saved the image in {name} Name.")
                cv2.imshow(f"{name}",image)
                print(f"Showing your {name} image.")
                cv2.waitKey(0)
                cv2.destroyAllWindows()
                print("Thank you for use Our Application.")
            else:
                print("!!Error: File Not saved on local system")
        else:
            print("\n\t\t Invalid Key please choose correct one...")
    else:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        print('\n\t\tImage Converted into GRAYSCALE successfully...')
        print("\tChoose one:\n\t\t |-1 for SAVE GRAY IMAGE\n\t\t |-2 For SHOW GRAY IMAGE")
        select = input("\t\t\t\tChoice : ")
        if select == "1":
            print("\tYour Selected 1. SAVE THE GRAY IMAGE:")
            name = input("\tEnter Name with Extension For Output Image: ")
            success = cv2.imwrite(f'{name}',gray_image)
            if success:
                print(f"\tsuccessfully Saved the image in {name} name.")
                print("\n\t\t\tThank You using our Service. Please Use Again... ")
            else:
                print(f"\n\t\tSorry!!! Your {name} is not saved successfully...")
        elif select == "2":
            print("\tYou Select Option 2 For SHOW the GRAY IMAGE.")
            cv2.imshow("Gray IMAGE Or Black & White Image", gray_image)
            print("\t\tShowing Gray Image :::")
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            print("\n\t\tSuccessfully show the gray Image.\n\t\tThank You Use Again our Services........\n")
        else:
            print("\n\t\t Invalid Key...")
else:
    print("\n\t\t\t\tError!!, Please Check your path properly...")

print("\n\t\t\t|----|| CODE DEVELOPED BY @gndgit ||----|\n")
