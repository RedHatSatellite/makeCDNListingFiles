#!/usr/bin/env python
# File: makecdn.py
# Author: Rich Jerrido <rjerrido@outsidaz.org>
# Purpose: Given a directory of expanded Red Hat Content ISOs, create a 'listing'
#          file for each subdirectory, suitable to allow Satellite 6 to sync from

import os
import sys
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-c", "--cdn-export-dir", dest="cdnexportdir", help="Directory of expanded CDN content", metavar="CDNEXPORTDIR")
parser.add_option("-v", "--verbose", dest="verbose", action="store_true", help="Verbose output")
(options, args) = parser.parse_args()

if not (options.cdnexportdir):
    print "Must specify directory of expanded CDN content: see usage"
    parser.print_help()
    print "\nExample usage: ./makecdn.py -c /var/www/html/pub/sat-import/"
    sys.exit(1)

if not os.path.exists(options.cdnexportdir):
    print "CDN export directory (%s) doesn't appear to exist" % cdnexportdir
    sys.exit(1)


def get_immediate_subdirectories(a_dir):
    return [name for name in os.listdir(a_dir)
            if os.path.isdir(os.path.join(a_dir, name))]

def create_listing_file(directory):
    listing_file = open(directory + "/listing", "w")
    sorted_subdirs = sorted(get_immediate_subdirectories(directory))
    if options.verbose:
        print "CURRENTDIR - %s " % directory
        print "\t SUBDIRS - %s " % sorted_subdirs
    for directory in sorted_subdirs:
        listing_file.write(directory + "\n")
    listing_file.close()

create_listing_file(options.cdnexportdir)

for root, directories, filenames in os.walk(options.cdnexportdir):
    for subdir in directories:
            currentdir = os.path.join(root, subdir)
            create_listing_file(currentdir)
