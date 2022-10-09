import time
import pyautogui
import requests

image_url = {"https://i.imgur.com/pl9mJJT.png": "youtube_dark.png",
             "https://i.imgur.com/qv25l8p.png": "tiktok_light.png",
             "https://i.imgur.com/uagowcj.png": "reddit_dark.png",
             "https://i.imgur.com/TgW9j05.png": "twitter_dark.png",
             "https://i.imgur.com/sbjWhlD.png": "youtube_light.png"}
# to add more sites here just put a link to the image, then choose a name for the file and add the
# file type at the end, examples are above of sites I already added
for key, value in image_url.items():
    img_data = requests.get(key).content
    with open(value, 'wb') as handler:
        handler.write(img_data)

while True:

    for key, value in image_url.items():
        screenShot = pyautogui.locateCenterOnScreen(value, confidence=0.8)
        print(screenShot)
        if screenShot is not None:
            pyautogui.hotkey("ctrl", "w")
            break
    time.sleep(5)
