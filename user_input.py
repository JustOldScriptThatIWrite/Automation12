#! /usr/bin/python
# -*- coding: utf-8 -*-

from xml.dom import minidom
xmldoc = minidom.parse('myxmlfile.xml')

itemlist = xmldoc.getElementsByTagName('book')
print(len(itemlist))
#print(itemlist[0].attributes['id'].value)
for s in itemlist:
    print(s.attributes['id'].value)