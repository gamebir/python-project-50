import argparse


def parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('first file')
    parser.add_argument('second file')
    parser.add_argument(
        '-f', '--format', help='set format of output', default=None)
    return parser.parse_args()
