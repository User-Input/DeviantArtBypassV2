# TODO: Optimize code/make cleaner. Messy asf and doesnt need all the imports. Doesnt need requests
# Imports
import shutil
import urllib.request
from urllib.parse import urlparse
import requests
from bs4 import BeautifulSoup as BS
import re


url = input('Please enter an image URL: ')  # Prompt user for img url


with urllib.request.urlopen(url) as f:  # Opens url as f variable
    data = f.read()
    soup = BS(data, "html.parser")
    tag = soup.find_all(style=re.compile("background-image"))


soup2 = BS(str(tag), "html.parser")
tag2 = soup2.div
print(str(tag2["style"]).index("'"))
Start = str(tag2["style"]).index("'")
print(str(tag2["style"]).rindex("'"))
End = str(tag2["style"]).rindex("'")
tag2 = str(tag2["style"])
RealURL = tag2[Start+1:End]
print(RealURL)


FixedURL = RealURL.replace("w_150,h_150,q_70", "w_1920,h_1080,q_100")
#Need to grab real resolution from main page

# Get the image name
FilePath = str((urlparse(RealURL)).path)
Last = FilePath.rindex("/")
file_name = FilePath[Last+1:]
file_name = file_name.replace("-150.", ".")

res = requests.get(FixedURL, stream=True)


if res.status_code == 200:
    with open(file_name, 'wb') as img:  # img is just a var name
        shutil.copyfileobj(res.raw, img)  # Saves image to local Directory
    print('Image successfully Downloaded: ', file_name)
else:
    print("Image Couldn't be retrieved")
