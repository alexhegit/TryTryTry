#conda activate tf1
python3 -m cProfile AllBlur.py | grep -i blur
python3 -V
python3 -c 'import cv2; print("cv2 version:", cv2.__version__)'
