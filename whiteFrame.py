from PIL import Image, ImageOps, ExifTags
import glob
import os
import argparse

def add_border(input_image, output_image, border):
    '''
    Draws a white border around an image. The resulting image will
    be a squared image keeping the aspect ratio of the input image.

    Args:
        input_image (string): path to the input image
        output_image (string): path to the output image
        border (int): border size on the maximum image side
    '''
    img = Image.open(input_image)
    # Preserve auto rotation of PIL thumbnail method
    if hasattr(img, '_getexif'): # only present in JPEGs
        for orientation in ExifTags.TAGS.keys(): 
            if ExifTags.TAGS[orientation]=='Orientation':
                break 
        # returns None if no EXIF data
        e = img._getexif()       
        if e is not None:
            exif=dict(e.items())
            orientation = exif[orientation] 

            if orientation == 3:   img = img.transpose(Image.ROTATE_180)
            elif orientation == 6: img = img.transpose(Image.ROTATE_270)
            elif orientation == 8: img = img.transpose(Image.ROTATE_90)
    # Resize
    img.thumbnail((1080, 1080), Image.ANTIALIAS)

    width, height = img.size
    size = max(width, height)
    
    # Add border
    bimg = ImageOps.expand(img, border=((size-width)//2 + border, (size-height)//2 + border), fill='white')
    bimg.save(output_image)

def walk_images(in_dir, our_dir, border):
    '''
    Iterates through images in a given directory and draws a white border around them.

    Args:
        in_dir (string): path to the input image directory
        out_dir (string): path to the output directory
        border (int): border size on the maximum image side
    '''
    images = glob.glob(in_dir + "/*.jpg")
    for i in images:
        head, tail = os.path.split(i)
        add_border(i, output_image=out_dir + '/framed_' + tail, border=border)
        print("Framed image " + i)

def parse_args():
    '''
    Parses the command line arguments.

    Returns:
        args (object): wrapper for the command line argument values
    '''
    parser = argparse.ArgumentParser(description='test', fromfile_prefix_chars="@")
    parser.add_argument('-i', '--input_directory', default="./")
    parser.add_argument('-o', '--output_directory', default="./")
    parser.add_argument('-b', '--border', type=int, default="30")
    args = parser.parse_args()
    return args
 
if __name__ == '__main__':
    args = parse_args()
    walk_images(args.input_directory, args.output_directory, args.border)
