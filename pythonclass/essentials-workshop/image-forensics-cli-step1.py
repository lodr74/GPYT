import argparse
parser=argparse.ArgumentParser()

#We add one positional argument called image_directory
parser.add_argument('image_directory', help='A file path containing images to process')

args=parser.parse_args()

print("Here is what was extracted from the command line.")
print(args)



