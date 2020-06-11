import requests
from bs4 import BeautifulSoup
import os
import urllib
from sys import argv

def main():
    argc = len(argv)

    if argc == 1:
        search_term = "cat"
        number_of_images = 10
    else:
        search_term = argv[1]
        for i in range(2, argc - 1):
            search_term += f" {argv[i]}"

        if argv[-1].isnumeric():
            number_of_images = int(argv[-1])
        else:
            search_term += f" {argv[-1]}"
            number_of_images = 10

    google_image_url = f"https://www.google.com/search?q={search_term}&tbm=isch"
    res = requests.get(google_image_url)
    soup = BeautifulSoup(res.text, 'html.parser')

    making_file = True
    i = 1
    hyphen_search = search_term.replace(" ", "-")
    while making_file:
        dir_name = f"./{number_of_images}-images-of-{hyphen_search}-v{i}"
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