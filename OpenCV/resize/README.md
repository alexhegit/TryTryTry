# Measure the Performance of OpenCV resize()

## Prerequistes
Put the original image files in ./images

## Build and Compile
mkdir ./build
cd ./build/
cmake  ../
make

## Run Test
cd ../
./build/Resize

The test log like bellow.
```
total image : 6
1280px.png resize to 224x224 time =0.395012 ms
8K.png resize to 224x224 time =0.679722 ms
1024px.png resize to 224x224 time =0.33905 ms
320px.png resize to 224x224 time =0.130322 ms
640px.png resize to 224x224 time =0.265546 ms
800px.png resize to 224x224 time =0.325004 ms
```
