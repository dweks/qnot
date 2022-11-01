#!/usr/bin/env python3
from util import sys
from db import db_init
from router import router


def main():
    try:
        db_init()
        router(sys.argv)
    except Exception as e:
        # typ, value, traceback = sys.exc_info()
        # print(typ, value, traceback)
        print(e)


if __name__ == "__main__":
    main()
