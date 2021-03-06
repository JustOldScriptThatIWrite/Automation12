#! /usr/bin/python
# -*- coding: utf-8 -*-

import sys
import json
from datetime import datetime, timedelta
from time import gmtime, strftime


class getJson(object):

    def JsonToFile(self, sn, alert,title,js,pdate):
        Text = json.loads(str(alert))
        db = Text['events'][0][js]
        response = []
        for row in Text['events']:
            for key, dict_list in row.iteritems():
                user_dst = dict_list[1]
                ip_src = dict_list[2]
                response.append({'count': user_dst['v'], 'year': ip_src['v']})

        print json.dumps(response)
        if sn.find('mcf') == -1:
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
        return mChar[:mChar.index(' ')-2]
