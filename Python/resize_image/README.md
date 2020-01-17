Many different implementation should be.

<<<<<<< HEAD
The imageMagick (http://www.imagemagick.org/) is a free image process software.
The example 1,2 use two commands of imageMagick do the image resize. You can
install it by 'sudo apt install imagemagick' in Ubuntu.

1. Use convert in python script
=======
1. Use convert do the batch resize

>>>>>>> 3308e2b6e00e1a77719cb429fb9ea0c70637c4a4
$python batch_convert_resize.py --resolution 224x224 --input images --output temp

2. Use mogrify in Bash script
$./batch_resize.sh 200x200 image500_640_480/ image500_200_200/

