#!/usr/bin/env python3
from gendiff.cli import parser
from gendiff.gendiff import generate_diff


def main():
    arg = parser()
    print(generate_diff(arg.first_file, arg.second_file))


if __name__ == '__main__':
    main()
