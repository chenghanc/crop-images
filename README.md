# Crop Images

Cropping images using trained darknet model

## Usage:
- #### Extract detected objects information

1. `class names`, `confidence` and `bbox coordinates` by running the command
2. Extract the information by running the command

`./darknet detector test custom.data custom.cfg custom.weights -thresh 0.4 -dont_show -ext_output < val.txt > result-dr.txt`

- #### Copy the file `result-dr.txt` to the working directory

- #### Copy the image files to the folder `val-images/`

- #### Remove lines from the text file containing specific words

  1) Remove **Enter** by typing `grep -vE "(Enter)" result-dr.txt > result4.txt`

  2) Remove **Detection** by typing `grep -vE "(Detection)" result4.txt > result.txt`

- #### Run the code 

