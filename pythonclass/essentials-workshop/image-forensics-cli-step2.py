import argparse
parser=argparse.ArgumentParser()

#Now we added a -d or --display optional argument. It is optional simply because it has dashes in the name.
parser.add_argument('image_directory', help='A file path containing images to process')
parser.add_argument('-d','--display',help='Display the image')

args=parser.parse_args()

print("Here is what was extracted from the command line.")
print(args)

print("Image Directory", args.image_directory)
print("Display images?", args.display)


