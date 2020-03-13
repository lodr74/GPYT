import argparse
parser=argparse.ArgumentParser()
parser.add_argument('image_directory',help='A file path containing image to process')
parser.add_argument('-d','--display',help='Display the image')
parser.add_argument('-m','--maps',help='Print google maps links}')
parser.add_argument('-e','--exif',help='Display the exif data')
parser.add_argument('-p','--pause',help='Pause after each image')
args=parser.parse_args()

print("Here is what was extracted from the command line.")
print(args)



