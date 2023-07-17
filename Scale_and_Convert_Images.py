#!/usr/bin/env python3

import os
import sys
import glob
from PIL import Image

# The source folder should be passed as a command line argument when calling this python script
# folder = os.fsencode(sys.argv[1])
# folder = sys.argv[1]

def pic_converter():
    #print(sys.argv[1])
    # Counter for how many pictures have been processed
    counter = 0
    #print(os.path.abspath(folder))
    # Iterate over pictures in folder
    for file in glob.glob("~/images/*", recursive=True):
        # Open each picture being iterated over
        #print(str(file))
        #filename = os.fsdecode(file)
        print("Processing image number {}, {}".format(counter + 1, file))
        im = Image.open(file)

        # Rotate image 90 deg clockwise --trying it all in one line below

        # Resize image from 192x192 to 128x128 --trying it all in one line below

        # Save the image to a new folder in .jpeg format...folder should be /opt/icons/
        im.rotate(270).resize(128,128).save("/opt/icons/" + filename, "JPEG")

        # Increment the counter
        counter += 1

    # Print the total amount of pictures processed
    print("{} pictures rotated 90 degrees clockwise, resized to 128x128 and saved in /opt/icons/".format(counter))
    

if __name__ == "__main__":
    # Call pic_converter while passing the path as a command line argument
    pic_converter()


