import os
import argparse

#from __future__ import print_function

def get_file_name(path):
    dirName, fileName = os.path.split(path)
    print("dirName: {}, fileName: {}".format(dirName, fileName))
    return fileName

def convert_resize(resolution, filename, inputpath, outputdir):
    #fname = get_file_name(inputpath)
    sourcefile = os.path.join(inputpath, filename)
    outfile = os.path.join(outputdir, filename)
    cmd = "convert -resize" + " " + resolution + "!" + " " + sourcefile + " " + outfile
    os.system(cmd)
    #print(cmd)

def batch_resize(FLAGS):
    if not os.path.exists(FLAGS.output):
        os.makedirs(FLAGS.output)

    #print(os.listdir(FLAGS.input))
    for f in os.listdir(FLAGS.input):
        if not os.path.isfile(os.path.join(FLAGS.input, f)):
            continue
        if f.split('.', 1)[1] != "jpg":
            print("{} is not jpg".format(f))
            continue
        convert_resize(FLAGS.resolution, f, FLAGS.input, FLAGS.output)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--input',
        type=str,
        default='input',
        help='input dir'
    )
    parser.add_argument(
        '--output',
        type=str,
        default='output',
        help='output dir'
    )
    parser.add_argument(
        '--resolution',
        type=str,
        default='224x224',
        help='resize resolution'
    )

    FLAGS, unparsed = parser.parse_known_args()

    batch_resize(FLAGS)
