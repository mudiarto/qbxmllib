#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Utility functions, classes, globals, etc for {{schema_name}}lib
"""


#
# Imports

import sys
import qbxmllib


#
# Globals and constants


#
# Functions for external use


def parseString(inString):
    from StringIO import StringIO
    doc = qbxmllib.parsexml_(StringIO(inString))
    rootNode = doc.getroot()
    rootTag, rootClass = qbxmllib.get_root_tag(rootNode)
    if rootClass is None:
        rootTag = 'QBXMLMsgsRq'
        rootClass = qbxmllib.supermod.QBXML
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    doc = None
    #sys.stdout.write('<?xml version="1.0" ?>\n')
    #rootObj.export(sys.stdout, 0, name_=rootTag,
    #    namespacedef_='http://developer.intuit.com/')
    return rootObj


#
# Classes



#
# Functions for internal use and testing

def test():
    pass



USAGE_TEXT = __doc__

def usage():
    print USAGE_TEXT
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 0:
        usage()
    test()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()



