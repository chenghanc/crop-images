# Crop Images

## Usage:
- ### Run the command `./darknet detector test custom.data custom.cfg custom.weights -thresh 0.4 -dont_show -ext_output < val.txt > result-dr.txt`

- ### Copy the file `result-dr.txt` to the working directory

- ### Copy the image files to the folder `val-images/`

- ### Remove lines from the text file containing specific words
  1) **grep -vE "(Enter)" result-dr.txt > result4.txt**
  2) **grep -vE "(Detection)" result4.txt > result.txt**

