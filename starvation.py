
#In order to enable dual screen ( primary and secondary to be visible)
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


#imports come after enabling a dual screen
import time
import pyautogui
import requests
import pathlib


def screenshot_finder(flag = True):
    """ Search any logos(images) within the screenshots folder and close any open tabs with the same logos(images) in a chromium browser such as : Google chrome, brave, microsoft edge

    Args:
        flag (bool, optional): If False the program,will terminate once all the open tabs with detected images in the screenshots folder have been closed. Defaults to True.
    """

    # establish current working directory
    path = pathlib.Path.cwd()

    # establish/create the screenshots directory
    screenshots_path = path.joinpath("screenshots")
    screenshots_path.mkdir(exist_ok=True)

    # load images you want the program to search to screenshots directory

    # loop through the screenshots directory
    loop = True
    while loop:
        for image_path in screenshots_path.iterdir():
            # establish absolute path to images the relative path does not work with pyautogui
            absolute_image_path = str(image_path.absolute())

            #locate sceenshot on the single/dual screen
            screenShot = pyautogui.locateCenterOnScreen(image=absolute_image_path, confidence=0.8)
            print(screenShot)
            if screenShot is not None:
                #close the screen
                print(f"closing {image_path.name}")
                pyautogui.hotkey("ctrl", "w")
                time.sleep(5)
        loop = flag
        
        
if __name__ == "__main__":
    screenshot_finder()


    


        
