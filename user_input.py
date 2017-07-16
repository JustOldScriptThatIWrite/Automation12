#! /usr/bin/python
# -*- coding: utf-8 -*-
import xml.etree.ElementTree as ET
import os

class dataFromXml(object):
    filename = "myxmlfile.xml"
    fullpath = os.path.abspath(os.path.join('getData',filename))
    def searchForID(self,serial):

        dom = ET.parse(self.fullpath)
        alerts = dom.findall('alert')
        for c in alerts:
            sn =  c.find('serial').text
            if sn in serial:
                desc = c.find('Title').text
                js =  c.find('json').text
                pdate = c.find('publish_date').text
                return desc,js,pdate

