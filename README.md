# Simple image resizing CLI tool

Simple python CLI tool for resizing images recursively while retaining folder structure

Help dialog:

```
usage: resize_images.py [-h] [-i INPUT_DIR] [-o OUTPUT_DIR] [-f FACTOR] [-v]

Recursively resize images in a directory by a factor, creating the same directory structure

options:
  -h, --help            show this help message and exit
  -i INPUT_DIR, --input-dir INPUT_DIR
                        Input dir containing images. 
                        Default: a subdir called images (images/)
  -o OUTPUT_DIR, --output-dir OUTPUT_DIR
                        Output dir containing resized images. 
                        Default: a subdir called resized_images (images_resized/)
  -f FACTOR, --factor FACTOR
                        Factor to resize images by. 
                        Default: keeps images unchanged: 1
  -v, --verbose         Display files as they're converted
                        Default: False
```
