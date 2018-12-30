#!/usr/bin/env python3
import pyperclip
from googletrans import Translator
import os
import sys
import argparse
import http.server
import socketserver
from urllib.parse import urlparse
from urllib.parse import parse_qs


class CallbackServer(http.server.BaseHTTPRequestHandler):
    def __init__(self, callback, *args):
        self.callback = callback
        http.server.BaseHTTPRequestHandler.__init__(self, *args)

    def do_GET(self):
        parsed_path = urlparse(self.path)
        query = parsed_path.query
        self.send_response(200)
        self.end_headers()
        result = self.callback(query)
        message = '\r\n'.join(result)
        self.wfile.write(message.encode('utf-8'))

    def do_HEAD(self):
        pass

    def do_POST(self):
        pass


def start(port, callback):
    def handler(*args):
        CallbackServer(callback, *args)
    server = http.server.HTTPServer(('', int(port)), handler)
    server.serve_forever()


def callback_method(query):
    query_dict = parse_qs(query)
    text = ''
    if 'text' in query_dict:
        text = '\n'.join(query_dict['text'])
    else:
        return ''

    print('----orig----')
    print("{0}".format(text), end="\n")
    print('------------')

    isascii = (lambda s: len(s) == len(s.encode()))
    lang = 'en'
    if isascii(text):
        lang = 'ja'
    try:
        text = (Translator().translate(text, dest=lang).text)
    except:
        text = '[network error]'
    return [text]


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-p', '--port', default=0)
    parser.add_argument('texts', nargs='*')

    args, extra_args = parser.parse_known_args()
    port = args.port
    if port != 0:
        print("serving at port", port)
        start(port, callback_method)
        return

    text = ' '.join(args.texts) + '\n'

    if len(args.texts) is 0:
        if not sys.stdin.isatty():
            lines = sys.stdin.readlines()
            text = '\n'.join(lines)
        else:
            text = pyperclip.paste()
    print_trans_result(text)


def print_trans_result(text):
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
