import sys
import codecs
import re
import time
import datetime
import os
import binascii
import MySQLdb as mdb
import string

class MysqlConnecttion:
    '''static connnection'''
    def __init__(self):
        '''Initializes the connection.'''
        self.con = mdb.connect('127.0.0.1', 'root', '0000', 'test', 3306) # test
        #self.con = mdb.connect('gsbhrdb01.chicagobooth.edu', 'lyricsadmin', 'Xc62zXQx', 'gartner');
        self.f = file(r"d:\test\log.txt", "w")
    def excute(self, query):
        with self.con:
            query = query.encode("utf-8")
            cur = self.con.cursor()
            ret = ""
            try:
                ret = "%s"%cur.execute(query)
                self.con.commit()
            except mdb.Error,e:
                self.con.rollback()
                print query
                self.f.write(query + "\n")
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                self.f.write("Mysql Error %d: %s" % (e.args[0], e.args[1] + "\n"))
                ret = e.args[1]
                self.f.flush()
                os.fsync(self.f.fileno())
            except UnicodeEncodeError:
                print query
                self.f.write(query + "\n")
                ret = "0"
            finally:
                cur.close()
                return ret
    def excute_with_result(self, query):
        with self.con:
            query = query.encode("utf-8")
            cur = self.con.cursor()
            ret = ""
            rows = ""
            try:
                ret = "%s"%cur.execute(query)
                rows = cur.fetchall()
            except mdb.Error,e:
                self.con.rollback()
                print query
                self.f.write(query + "\n")
                print "Mysql Error %d: %s" % (e.args[0], e.args[1])
                self.f.write("Mysql Error %d: %s" % (e.args[0], e.args[1] + "\n"))
                ret = e.args[1]
                self.f.flush()
                os.fsync(self.f.fileno())
            except UnicodeEncodeError:
                print query
                self.f.write(query + "\n")
                ret = "0"
            finally:
                cur.close()
                return rows
    def log(self, content):
        self.f.write(content + "\n")
    def __del__(self):
        self.con.close()
        self.f.close()