import requests
from bs4 import BeautifulSoup
import os
import urllib

def main():
    number_of_images = 5
    search_term = "cat"
    
    google_image_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
    res = requests.get(google_image_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    making_file = True
    i = 1
    while making_file:
        dir_name = f"./{number_of_images}-images-of-{search_term}-v{i}"
        try:
    os.mkdir(dir_name)
            making_file = False
        except FileExistsError:
            i += 1

    images = soup.find_all("img")
    images = images[1:]

    for i in range(number_of_images):
        current_image = urllib.request.urlretrieve(images[i]["src"], f"{dir_name}/image-{i}.jpg")


if __name__ == "__main__":
    main()