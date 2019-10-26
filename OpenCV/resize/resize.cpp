/**
 * OpenCV resize performance measurement
 *
 * Copyright 2019 by He Ye <heye_dev@163.com>
 *
 */

#include <dirent.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/stat.h>
#include <queue>
#include <string>
#include <vector>
#include <iostream>
#include "opencv2/opencv.hpp"
#include "opencv2/highgui.hpp"
#include "opencv2/imgproc.hpp"
#include "ResizeConfig.h"

using namespace cv;
using namespace std;

const string ImagePath = "./images/";
queue<string> images; // Stroing the list of images

#define RSIZE_H 224
#define RSIZE_W 224


string type2str(int type) {
    string r;

    uchar depth = type & CV_MAT_DEPTH_MASK;

    switch ( depth ) {
        case CV_8U:  r = "8U"; break;
        case CV_8S:  r = "8S"; break;
        case CV_16U: r = "16U"; break;
        case CV_16S: r = "16S"; break;
        case CV_32S: r = "32S"; break;
        case CV_32F: r = "32F"; break;
        case CV_64F: r = "64F"; break;
        default:     r = "User"; break;
    }

    return r;
}


/**
 * @brief put image names to a vector
 *
 * @param path - path of the image direcotry
 * @param images - the vector of image name
 *
 * @return none
 */
void ListImages(string const &path, queue<string> &images) {
    struct dirent *entry;

    /*Check if path is a valid directory path. */
    struct stat s;
    lstat(path.c_str(), &s);
    if (!S_ISDIR(s.st_mode)) {
        fprintf(stderr, "Error: %s is not a valid directory!\n", path.c_str());
        exit(1);
    }

    DIR *dir = opendir(path.c_str());
    if (dir == nullptr) {
        fprintf(stderr, "Error: Open %s path failed.\n", path.c_str());
        exit(1);
    }

    while ((entry = readdir(dir)) != nullptr) {
        if (entry->d_type == DT_REG || entry->d_type == DT_UNKNOWN) {
            string name = entry->d_name;
            string ext = name.substr(name.find_last_of(".") + 1);
            if ((ext == "JPEG") || (ext == "jpeg") || (ext == "JPG") || (ext == "jpg") ||
                (ext == "PNG") || (ext == "png")) {
                images.push(name);
            }
        }
    }

    closedir(dir);
}


int main( int argc, char** argv )
{
    Mat im, om;
    double e1, e2, t;
    om = Mat(Size(RSIZE_H, RSIZE_W), CV_8UC3);
    setUseOptimized(true);
    if (useOptimized()) {
    	printf("Use Optimized code with SSE2, AVX, etc\n");
    }

    ListImages(ImagePath, images);
    if (images.size() == 0) {
        cerr << "\nError: Not images exist in " << ImagePath << endl;
        return -EEXIST;
    } else {
        cout << "total image : " << images.size() << endl;
    }

    int size = images.size();
    while(true) {
        string imageName = images.front();
	if(imageName == "") {
	    break;
	    printf("end!\n");
	}
	images.pop();

    	e1 = (double)getTickCount();
	im = imread(ImagePath + imageName, IMREAD_COLOR);
	// Do resize
    	e1 = (double)getTickCount();
        resize(im, om, cvSize(RSIZE_H, RSIZE_W), 0, 0, INTER_LINEAR);
        e2 = (double)getTickCount();
        t = (e2 - e1) * 1000 / getTickFrequency();
        printf("%s resize to %dx%d time =%g ms\n", &(imageName[0]), RSIZE_H, RSIZE_W, t);
    }

    namedWindow("Display Image", WINDOW_AUTOSIZE);
    imshow("Display Image", om);
    waitKey(0);

    return 0;
}
