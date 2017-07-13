#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime, timedelta
from time import gmtime, strftime

class getJson(object):

    def JsonToFile(self, sn, alert):

        Text = json.loads(str(alert))
        db = Text['events'][0]['user_dst']+ '\n' +Text['events'][0]['event_type']
        if sn in 'SN_TESTMCF_27000':
            #self.write(sn,Text['events'][0]['user_dst'])
            self.write(sn,db)
    def write(self,sn,decodedJson):
        print('Creating new text file')
        try:
            file = open('/tmp/'+sn+'.txt', 'w')
            file.write(decodedJson)
            file.close()
        except:
            file = open('/tmp/'+sn+' Error.txt', 'w')
            file.write('Something went wrong! Can\'t tell what? ------- time:   ' + strftime("%d-%m-%Y   %H:%M:%S",
                                                                                             gmtime()) + '\n')
            file.close()

    def getSN(self,sn):
        fChar = sn.index('SN_')
        mChar = sn[fChar:]
        return mChar[:mChar.index(' ')]
