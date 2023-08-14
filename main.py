import sys
import config
import os
import platform
import generate_camo

def main():
    print("Initialize Program...\n")
    # Get Config
    opt = config.getConfig()
    print("Taking config input...\n")
    # Pop Selection Menu
    print("Option: \n"
          "1. Camo Generator\n"
          "2. Image Generator\n")

    response = input("Select 1 or 2: \n")
    #input validate
    while(response):
        if(response == "1"):
            print("Input Valid!")
            print("run option 1")
            response = option_1(opt)
        elif(response == "2"):
            print("Input Valid!")
            print("run option 2")
            response  = option_2()
        else:
            print("invalid response, retry")
            response = input("Type '1' or '2': \n")
    sys.exit()
def option_1(opt):

    folder_num = input("Enter background folder number, ex: 1 for background1 or 2 for background2 \n")

    number_img = input("How many image?\n")

    generate_camo.run_generator(int(folder_num), int(number_img), opt)
    return False

def option_2():

    if sys.platform == "win32":
        try:
            "Check Program Files x86"
            os.system("\"C:\\Program Files (x86)\\Blender Foundation\\Blender\\blender.exe\" --background -P generate_img.py")
        except NotADirectoryError:
            print("Path Error, check path")
        finally:
            print("Try Program Files path")
        try:
            os.system("\"C:\\Program Files\\Blender Foundation\\Blender\\blender.exe\" --background -P generate_img.py")
        except NotADirectoryError:
            print("Path Error, check path")
        finally:
            sys.exit()
    elif sys.platform == "darwin":
        print("Macbook OS detected, run Macbook OS")
        os.system("/Applications/Blender/blender.app/Contents/MacOS/blender --background --python generate_img.py")

    return False
if __name__ == "__main__":
    main()
