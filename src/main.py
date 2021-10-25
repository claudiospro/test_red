#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import time

import logic

parser = argparse.ArgumentParser(description='Tools by save network measurements')
parser.add_argument('--interval', '-i', help="Interval in minutes execute measurements", type=int)
parser.add_argument('--file_path', '-f', help="Address of the file where it will be saved.")
parser.add_argument('--test_mode', '-t', help="Test Mode")

minute_interval = 5
file_path = './files/data.csv'

if __name__ == "__main__":
    args = parser.parse_args()
    if args.interval:
        minute_interval = args.interval
    if args.file_path:
        file_path = args.file_path

    if args.test_mode:
        while True:
            logic.execute(file_path)
            time.sleep(minute_interval * 60)
    print('test mode')
    logic.execute(file_path)
