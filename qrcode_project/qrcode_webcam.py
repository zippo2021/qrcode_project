import sys, os
from PyQt4 import QtCore, QtGui
from qrtools import QR
from connect import db
def decodeWebcam(self):
        qr = QR()
        qr.decode_webcam()
        if qr.data_to_string() != 'NULL':
            #qr is a utf8 string    
