#!/usr/bin/env python

import os.path
import shutil

def clean_arena():
    root = os.path.dirname(__file__)
    try:
        shutil.rmtree(os.path.join(root, 'arena'))
    except OSError:
        pass

if __name__ == '__main__':
    clean_arena()
