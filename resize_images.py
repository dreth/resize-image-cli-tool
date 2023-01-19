import argparse
from PIL import Image
import os
from functools import reduce
import operator

# sep
sep = os.path.sep

# CLI argument parser
parser = argparse.ArgumentParser(
    description="Recursively resize images in a directory by a factor, creating the same directory structure", formatter_class=argparse.RawTextHelpFormatter)

# input dir argument
parser.add_argument("-i", "--input-dir", type=str,
                    help="Input dir containing images. \nDefault: a subdir called images (images)", default="images")

# output dir argument
parser.add_argument("-o", "--output-dir", type=str,
                    help="Output dir containing resized images. \nDefault: a subdir called resized_images (images_resized)", default="images_resized")

# factor argument
parser.add_argument("-f", "--factor", type=float, default=1,
                    help="Factor to resize images by. \nDefault: keeps images unchanged: 1")

# verbose argument
parser.add_argument("-v", "--verbose", default=False, help="Display files as they're converted\nDefault: False", action="store_true")

# parse arguments
args = parser.parse_args()

# output dir and input dir can't be the same
if args.input_dir == args.output_dir:
    raise ValueError("Input dir and output dir cannot be the same")

# factor can't be negative
if args.factor < 0:
    raise ValueError("Factor cannot be negative")

# run over file tree
def resize_images(input_dir=args.input_dir, output_dir=args.output_dir, factor=args.factor, verbose=args.verbose):
    # create root images folder
    try_create_dir(output_dir)
    
    # loop over files recursively
    for root, _, files in os.walk(input_dir):
        # save path
        save_path = os.path.join(output_dir, os.path.relpath(root, input_dir))

        # create folder if it doesn't exist
        try_create_dir(save_path)
        
        for file in files:
            # show file if verbose
            if verbose: print(f"{os.path.join(root, file)} --> {os.path.join(save_path, file)}")
            
            # get the path of the file
            path = os.path.join(root, file)
            
            try:
                # open the image
                image = Image.open(path)
            except:
                raise ValueError(f"Could not open {path} or file is not an image")
                
            # resize the image
            image = image.resize(
                (int(image.size[0]*factor), int(image.size[1]*factor)))
            
            # save the image
            image.save(os.path.join(save_path, file))

# abstract this part of the code because i dont like how tryblocks look
def try_create_dir(path):
    try:
        os.makedirs(path)
    except FileExistsError:
        pass

# main
def main():
    resize_images()

# run main
main()
