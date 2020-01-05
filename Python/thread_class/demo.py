#!/usr/bin/env python

import argparse
from c_core import demo

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--vdev',
        type=int,
        default='0',        
        help='vdev - /dev/videoX')
    parser.add_argument(
        '--morphology_meth',
        type=str,
        default='chuangda',
        help='morphology method - xilinx | chuangda')
    parser.add_argument(
        '--data_type',
        type=str,
        default='dilun',
        help='test data type - dilun | mianbu | mbpds')
    parser.add_argument(
        '--print_en',
        type=str,
        default='d',
        help='print timing - d | e')
    parser.add_argument(
        '--jobs',
        type=int,
        default='2',
        help='number of jobs')
    parser.add_argument(
        '--fps',
        type=int,
        default='60',
        help='FPS of camera')
    parser.add_argument(
        '--show',
        type=str,
        default='off',
        help='show bad, off | on')

    FLAGS, unparsed = parser.parse_known_args()

    demo(FLAGS)
