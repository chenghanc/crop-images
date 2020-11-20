import os
import glob
import cv2
import re
import sys

#############################################################################################################################################################
# Author: Cesare Chung                                                                                                                                      #
# Date: 22/10/2020                                                                                                                                          #
# (A) run the command ./darknet detector test custom.data custom.cfg custom.weights -thresh 0.4 -dont_show -ext_output < val.txt > result-dr.txt            # 
# (B) copy the file result-dr.txt to the working directory                                                                                                  #
# (C) copy the image files to the folder val-images/                                                                                                        #
# (D) perform grep -vE "(Enter)" result-dr.txt > result4.txt                                                                                                # 
#         and grep -vE "(Detection)" result4.txt > result.txt                                                                                               #
#         and sed -i -- 's/white/Head/g' result.txt ...                                                                                                     #
# (E) run the code                                                                                                                                          #
#############################################################################################################################################################

IN_FILE = 'result.txt'
pattern = r'red|blue|white|yellow|AdultHead|RealBabyHead'
inputFolder = 'val-images/'
cropFolder  = 'cropped/'

SEPARATOR_KEY = 'helmet2'
IMG_FORMAT = '.jpg'      # ('.jpg', '.xml')

os.chdir(os.path.dirname(os.path.abspath(__file__)))
parent_path = os.path.abspath(os.path.join(os.getcwd(), os.pardir))
print(parent_path)
WORKING_PATH = os.path.join(parent_path, 'crop')
print(WORKING_PATH)

image_files = [f for f in os.listdir(inputFolder) if f.endswith(IMG_FORMAT)]
print(image_files)

'''
# Get the list of all files in directory tree at given path
listOfFiles = list()
for (dirpath, dirnames, filenames) in os.walk(inputFolder):
    listOfFiles += [os.path.join(dirpath, file) for file in filenames]
# Print the files    
for elem in listOfFiles:
    print(elem)
    print(elem.split('/')[1])
'''

try:
	os.mkdir(cropFolder)
except FileExistsError:
	pass

outfile = None
# Parsing the .txt file
i=0
with open(IN_FILE) as infile:
	for line in infile:
		if SEPARATOR_KEY in line:
			if IMG_FORMAT not in line:
				break
			# get text between two substrings (SEPARATOR_KEY and IMG_FORMAT)
			image_path = re.search(SEPARATOR_KEY + '(.*)' + IMG_FORMAT, line)
			print(image_path)
			# get the image name (the final component of a image_path)
			# e.g., from 'data/horses_1' to 'horses_1'
			#image_name = os.path.basename(image_path.group(0))
			image_name = os.path.basename(image_path.group(1))
			#print(image_name)
			## check if image exists
			for fname in os.listdir(inputFolder):
				if fname.startswith(image_name):
					# image found
					#print(fname)
					#img = cv2.imread(inputFolder + fname)
					# get image width and height
					#img_height, img_width = img.shape[:2]
					break

			img = cv2.imread(inputFolder + image_name + '.jpg')
			img_height, img_width = img.shape[:2]
			
			# close the previous file
			if outfile is not None:
				outfile.close()
			# open a new file
			#outfile = open(os.path.join(cropFolder, image_name + '.txt'), 'w')

		elif re.search(pattern, line):
			cord_raw = line
			cord = cord_raw.split("(")[1].split(")")[0].split("  ")
			#print(cord)

			# Coordinate calculation
			#x_min = int(cord[1])
			#y_min = int(cord[3])
			#x_max = x_min + int(cord[5])
			#y_max = y_min + int(cord[7])

			class_name, info = line.split(':', 1)
			confidence, bbox = info.split('%', 1)
			bbox = bbox.replace(')','')
			#print(bbox)
			x_min, y_min, width, height = [int(s) for s in bbox.split() if s.lstrip('-').isdigit()]
			x_max = x_min + width
			y_max = y_min + height

			# Cropping from the actual image
			#image = cv2.imread(img)
			imgCrop = img[y_min:y_max, x_min:x_max]

			cv2.imwrite("cropped/image%04i.jpg" %i, imgCrop)
			i += 1

