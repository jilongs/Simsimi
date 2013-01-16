import sys
import codecs
import re
import time
import datetime
import os
import binascii
import string


class Log:
    def __init__(self, log_file):
       self.f = file(r"d:\test\%s.txt"%log_file, "w")
    def write(self, content):
        self.f.write(content.encode("utf-8") + "\n")
        self.f.flush()
        os.fsync(self.f.fileno())
    def __del__(self):
        self.f.close()