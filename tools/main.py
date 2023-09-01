# OSM Images
# A easy way to use Github Raw to host images for OSM
# Github: https://www.github.com/lewisevans2007/OSM_Images
# Licence: GNU General Public License v3.0
# By: Lewis Evans

"""
README
# OSM Images

A easy way to use Github Raw to host images for OSM.

## Usage

1. Clone this repo and clear out the images folder.
2. Configure `config.json` and set `user` to your Github username.
3. Run `make`. This will ask you to add the image to the `ADD_HERE` folder.
4. Continue with the prompts.
5. You will be given a github raw link. This is the image link once it is uploaded.
6. Commit then add to the image tag on your OSM change.

"""


import os
import json
import datetime


def main():
    with open("config.json", "r") as f:
        config = json.load(f)

    try:
        config["user"]
    except KeyError:
        print("Username doesnt exist on the config file")
        exit()

    try:
        config["repo"]
    except KeyError:
        print("Repo doesnt exist on the config file")
        exit()

    if not os.path.exists("ADD_HERE"):
        os.mkdir("ADD_HERE")

    input("Add the image to the ADD_HERE folder and press enter to continue")
    while True:
        if len(os.listdir("ADD_HERE")) == 0:
            input("Add the image to the ADD_HERE folder and press enter to continue")

        elif len(os.listdir("ADD_HERE")) > 1:
            print("Please only have one image in the ADD_HERE folder")
            input("Press enter once there is only one file in the ADD_HERE folder")
        else:
            break

    image_name = os.listdir("ADD_HERE")[0]

    now = datetime.datetime.now()
    folder_path = f"images/{now.year}/{now.month}/{now.day}"
    os.makedirs(folder_path, exist_ok=True)
    file_path = f"{folder_path}/{now.hour}_{now.minute}_{now.second}.{image_name.split('.')[-1]}"
    os.rename(f"ADD_HERE/{image_name}", file_path)
    print("Now commit this change and add the following link to the image tag")
    print(
        f"https://raw.githubusercontent.com/{config['user']}/{config['repo']}/main/{file_path}"
    )
    os.rmdir("ADD_HERE")
    exit()


if __name__ == "__main__":
    main()
