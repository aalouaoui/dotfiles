#! /usr/bin/python3
import requests
import os.path

BING_URL = "https://www.bing.com/HPImageArchive.aspx?format=js&idx=0&n=8&mkt=en-US"
IMG_DIR = os.path.expanduser("~/bing-wallpapers")

# Create IMG_DIR if it does not exist
if not os.path.isdir(IMG_DIR):
    os.mkdir(IMG_DIR)

# Get image list from Bing
images = requests.get(BING_URL).json()["images"]

for i in range(len(images)):
	img = images[i]
	date = img['startdate']
	filename = date[0:4] + "-" + date[4:6] + "-" + date[6:8] + ".jpg"
	file_path = os.path.join(IMG_DIR, filename)
	
	if os.path.isfile(file_path):
		print ("Skipped", file_path)
		continue

	img_data = requests.get("https://bing.com" + img['url'])
	file = open(file_path, "wb")
	file.write(img_data.content)
	file.close()
	print("Saved", file_path)
	
	if i == 0:
		file_path = os.path.join(IMG_DIR, "today.jpg")
		file = open(file_path, "wb")
		file.write(img_data.content)
		file.close()
		print("Saved", file_path)
