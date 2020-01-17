from PIL import Image
import png, array

unknown_flags = ['flag_1.png', 'flag_2.png', 'flag_3.png']
known_flags = []

unknown_flag_path = ''
known_flag_path = ''




def color_dist_flag(flag_path):

    color_dist = [[[0] * 256] * 256] * 256

    reader = png.Reader(filename=flag_path)
    w, h, pixels, metadata = reader.read_flat()

    pix = im.load()

    print pix
    print im.mode

    for

    for pixel in pixel_values:
        print pixel
        exit(1)

color_dist_flag('/Users/mattlee/riddler/github_clean/Riddler/Jan3_2020/Express/scrambled/flag_1.png')
