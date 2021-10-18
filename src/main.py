#!/usr/bin/python3
# -*- coding: utf-8 -*-

import argparse
import time

import logic

parser = argparse.ArgumentParser(description='Tools by save network measurements')
parser.add_argument('--interval', '-i', help="Interval in minutes execute measurements", type=int)
parser.add_argument('--file_path', '-f', help="Address of the file where it will be saved.")

args = parser.parse_args()
minute_interval = 5
file_path = './files/data.csv'


if __name__ == "__main__":
    if args.interval:
        minute_interval = args.interval
    if args.file_path:
        file_path = args.file_path

    while True:
        logic.execute(file_path)
        time.sleep(minute_interval * 60)
