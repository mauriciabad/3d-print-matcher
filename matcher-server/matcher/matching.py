import os

import imagehash
import matplotlib.pyplot as plt
from PIL import Image, ImageFilter


def set_aspect_ratio(im):
    width, height = im.size

    difference = abs(height - width)

    if width != height:
        if height > width:
            return im.crop((0, difference / 2, width, height - (difference / 2)))
        else:
            return im.crop((difference / 2, 0, width - (difference / 2)), height)
    else:
        return im


def get_similarity(first_path, second_path):

    first_image = set_aspect_ratio((Image.open(first_path)))
    second_image = set_aspect_ratio((Image.open(second_path)))

    if first_image.width < second_image.width:
        second_image = second_image.resize((first_image.width, first_image.height))
    else:
        first_image = first_image.resize((second_image.width, second_image.height))

    first_image = first_image.crop(first_image.getbbox())
    second_image = second_image.crop(second_image.getbbox())

    first_image = first_image.filter(ImageFilter.BoxBlur(radius=3))
    second_image = second_image.filter(ImageFilter.BoxBlur(radius=3))

    phashvalue = imagehash.phash(first_image) - imagehash.phash(second_image)
    ahashvalue = imagehash.average_hash(first_image) - imagehash.average_hash(
        second_image
    )

    return phashvalue + ahashvalue
