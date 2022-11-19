import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('first file')
    parser.add_argument('second file')
    parser.add_argument('-f', '--format', required=True, help='set format of output')
    return parser.parse_args()
