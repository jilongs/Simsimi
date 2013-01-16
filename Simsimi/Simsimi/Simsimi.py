from __future__ import division # for division
import sys
import codecs
import re
import time
import datetime
import os
import binascii
import MySQLdb as mdb
import string
import nltk
import cPickle as pickle
from nltk.stem.porter import PorterStemmer
import nltk.corpus
import urllib2
import simplejson as json
from Log import Log
from DBConnection import MysqlConnecttion

#main
if __name__ == "__main__":
    request = urllib2.Request(r"http://api.simsimi.com/request.p?key=jilongs&lc=en&ft=1.0&text=hi")
    response = urllib2.urlopen(request)
    print "%s"%response
    raw_input()