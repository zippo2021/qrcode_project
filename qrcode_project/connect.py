# -*- coding: utf8 -*-
import MySQLdb
db = MySQLdb.connect(host="127.0.0.1",
                     port=3306, 
                     user="user", # your username
                      passwd="user", # your password
                      db="qrcode_test") # name of the data base
