import argparse
parser=argparse.ArgumentParser()

#We define a list of valued choices for directories with choices=['list of values']
#We make -d or --display a required field with required=True
#We allow two values to follow -d
parser.add_argument('image_directory', choices=['/tmp','/home/student'], help='A file path containing images to process')
parser.add_argument('-d','--display',nargs=2,required=True,help='Display the image')

args=parser.parse_args()

print("Here is what was extracted from the command line.")
print(args)

print("Image Directory", args.image_directory)
print("Display images?", args.display)


