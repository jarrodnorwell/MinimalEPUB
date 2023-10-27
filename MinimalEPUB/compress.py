# built-in modules
from os import sep

# pip modules
from PIL import Image

# local modules
from utilities import percentage

def compress(root: str, file: str, image: Image, percentage_input: int):
    image.resize((int(percentage(percentage_input, image.width)),
                  int(percentage(percentage_input, image.height))))
    image.save(root + sep + file)