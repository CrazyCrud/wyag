import argparse
import collections
import configparser
import hashlib
import os
import sys
import zlib

argparser = argparse.ArgumentParser(description="The stupid content tracker")

argsubparsers = argparser.add_subparsers(title="Command", dest="command")
argsubparsers.required = True


def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
