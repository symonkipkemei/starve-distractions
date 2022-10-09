# distractionStopper1000
A short script that helps you stay focused while working

Essentially, the script closes a social media website that you might be distracted by whenever you open it. The script uses pyautogui to scan for the logo of the social media site because all social media sites have their logo at the top somewhere. When it detects that a logo is on the screen it uses the hotkey "ctrl" and "w" to close the tab. This is all done with pyautogui. 

# HOW TO USE

1. put the youtubetutorial.py file in a python project
2. go to your terminal or command prompt and install:
pip install pyautogui
pip install opencv-python
pip install pillow
pip install requests
3. run it and it should work

# HOW TO ADD MORE SITES
1. on line 10 inside the dictionary type the image url of the site logo in quotations make sure it has a .png .jpg etc. at the end of the url
2. after the quotation type a colon and in quotes type any name for the file and add whatever file type at the end of the name
3. add a comma if you want to add more, but if you are done put a curly bracket at the end

here's an example of all the sites i've added:

image_url = {"https://i.imgur.com/pl9mJJT.png": "youtube_dark.png",
             "https://i.imgur.com/qv25l8p.png": "tiktok_light.png",
             "https://i.imgur.com/uagowcj.png": "reddit_dark.png",
             "https://i.imgur.com/TgW9j05.png": "twitter_dark.png",
             "https://i.imgur.com/sbjWhlD.png": "youtube_light.png"}
            
there is also directions inside of the python file
