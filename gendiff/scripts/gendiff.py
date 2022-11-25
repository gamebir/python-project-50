#!/usr/bin/env python3
from gendiff.cli import parser
from gendiff.gendiff import generate_diff


def main():
    parser()
    generate_diff()


if __name__ == '__main__':
    main()
