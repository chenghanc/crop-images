# Crop Images

Cropping images using trained darknet model

## Usage:
- #### Extract detected objects information

    * `class names`, `confidence` and `bbox coordinates`
    * Extract the information by running the command

`./darknet detector test custom.data custom.cfg custom.weights -thresh 0.4 -dont_show -ext_output < val.txt > result-dr.txt`

- #### Copy the file

    * Copy the file `result-dr.txt` to the working directory

- #### Copy the image files

    * Copy the image files to the folder `val-images/`

- #### Remove lines from the text file containing specific words

    * Remove **Enter** by typing `grep -vE "(Enter)" result-dr.txt > result4.txt`
    * Remove **Detection** by typing `grep -vE "(Detection)" result4.txt > result.txt`

- #### Run the code

    * `python parsing.py`

