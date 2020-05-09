import sys
import os
from video import extract_images
from pdf import makePdf
from settings import DELETE_IMAGES
from files import delete_folder

def run(input_name, extention, output):
    extract_succes = extract_images(input_name, extention)
    if extract_succes:
        makePdf(output, "pictures/{}".format(input_name))
        if DELETE_IMAGES:
            delete_folder("pictures/{}".format(input_name))

if __name__ == "__main__":
    input_name = sys.argv[1]
    input_name, extention = os.path.splitext(input_name)
    output = input_name
    if len(sys.argv) == 3:
        output = sys.argv[2]
    run(input_name, extention, output)