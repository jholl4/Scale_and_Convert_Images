#!/usr/bin/env python3

import os
from PIL import Image

# Source of the images to be converted
src = "./images/"
# Destination directory for the images after conversion
dst = "./opt/icons/"
# Size to resize the images to
size = (128, 128)
# Path of the source images
imgs = os.listdir(src)

def pic_converter():
    # Counter for how many pictures have been processed
    counter = 0

    # Make the destination directory
    try:
        os.makedirs("./opt/icons")
    except:
        print("directory already exists")
    

    # Iterate over pictures in folder
    for img  in imgs:
        try:
            with Image.open(src + img) as im:
                im = im.convert('RGB')
                im = im.resize(size)
                im = im.rotate(270)
                im.save(dst + img, 'JPEG')
                # Increment the counter
                counter += 1
        except OSError:
            print("Cannot convert" + img)

    # Print the total amount of pictures processed
    print("{} pictures rotated 90 degrees clockwise, resized to 128x128 and saved in ./opt/icons/".format(counter))
    

if __name__ == "__main__":
    # Call pic_converter while passing the path as a command line argument
    pic_converter()


