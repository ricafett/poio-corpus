# -*- coding: utf-8 -*-
#
# Poio Corpus
#
# Copyright (C) 2009-2013 Poio Project
# Author: Peter Bouda <pbouda@cidles.eu>
# URL: <http://media.cidles.eu/poio/>
# For license information, see LICENSE.TXT

import sys
import re
import codecs

def main(argv):
    f1 = codecs.open(argv[1], "r", "utf-8")
    f2 = codecs.open(argv[2], "w", "utf-8")

    lines_to_delete = [
        u" </noinclude</includeonly»"
    ]

    for line in f1:
        if line.rstrip() in lines_to_delete:
            f2.write("\n")
            continue
            
        f2.write(line)

    f1.close()
    f2.close()

if __name__ == "__main__":
    main(sys.argv)