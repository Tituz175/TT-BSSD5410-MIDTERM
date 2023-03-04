import colorsys

from SortFunctions import mergesort
from SearchFunctions import binarySearch_sub
from PixelFunctions import storePixels,  compare_pixels_merge_sort, \
    pixels_to_points, grayscale
from PIL import Image


def im_highlight(IMG_NAME, tuple_start):
    with Image.open(IMG_NAME + ".jpg") as image:
        pixels, yiq_pixels = storePixels(image)
        yiq_pixels = mergesort(yiq_pixels, compare_pixels_merge_sort)
        target_start = (tuple_start[0] / 255, tuple_start[1] / 255, tuple_start[2] / 255)
        print(target_start)
        yiq_target_start = colorsys.rgb_to_yiq(target_start[0], target_start[1], target_start[2])
        print(yiq_target_start[2])
        sub_index_start = binarySearch_sub([b[0][0] for b in yiq_pixels], 0, len(yiq_pixels) - 1, yiq_target_start[2])
        print("target start at: ", sub_index_start)
        grayscale(image, pixels)
        pixels_to_points(image, yiq_pixels[sub_index_start:])
        image.show()


# end def im_highlight():


def main():
    IMG_NAME = "guard"
    tuple_start = (186, 39, 85)

    im_highlight(IMG_NAME, tuple_start)


# end def main():


if __name__ == "__main__":
    main()
