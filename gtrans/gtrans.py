#!/usr/bin/env python3
import pyperclip
from googletrans import Translator
import os
import sys
import argparse


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('texts', nargs='*')

    args, extra_args = parser.parse_known_args()
    text = ' '.join(args.texts) + '\n'

    if len(args.texts) is 0:
        if not sys.stdin.isatty():
            lines = sys.stdin.readlines()
            text = '\n'.join(lines)
        else:
            text = pyperclip.paste()

    print('----orig----')
    print("{0}".format(text), end="")
    print('------------')

    try:
        text = (Translator().translate(text, dest='ja').text)
    except:
        print('[network error]')
        sys.exit(1)
    print('-----ja-----')
    print(text)
    print('------------')

    try:
        text = (Translator().translate(text, dest='en').text)
    except:
        print('[network error]')
        sys.exit(1)
    print('-----en-----')
    print(text)
    print('------------')


if __name__ == '__main__':
    main()
