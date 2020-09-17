#!/usr/bin/python3
import sys
import urllib3
import os
import json
from PySide2 import QtWidgets, QtCore, QtGui


class mainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        gb = QtWidgets.QGroupBox("Button Group Box")
        pb1 = QtWidgets.QPushButton("One")
        pb2 = QtWidgets.QPushButton("Two")
        hbl = QtWidgets.QHBoxLayout()
        hbl.addWidget(pb1)
        hbl.addWidget(pb2)
        hbl.addStretch(1)
        gb.setLayout(hbl)
        mhbl = QtWidgets.QHBoxLayout()
        mpic = QtWidgets.QLabel()
        mvbl = QtWidgets.QVBoxLayout()
        te = QtWidgets.QTextEdit()
        mvbl.addWidget(te)
        # mvbl.addWidget(gb)
        mw = QtWidgets.QWidget()
        mw.setLayout(mvbl)
        mhbl.addWidget(mw)
        mhbl.addWidget(mpic)
        cwid = QtWidgets.QWidget()
        cwid.setLayout(mhbl)
        self.setCentralWidget(cwid)
        http = urllib3.PoolManager()
        key = os.environ['NASA_KEY']
        nasaurl = u'https://api.nasa.gov/planetary/apod?api_key='+key
        r = http.request('GET', nasaurl)
        myd = json.loads(r.data)
        te.setText(myd['explanation'])
        pixmap = QtGui.QPixmap()
        pdata = http.request('GET', (myd['url']))
        pixmap.loadFromData(pdata.data)
        mpic.setPixmap(pixmap.scaledToWidth(600))
        self.setMaximumWidth(900)
        self.setMinimumWidth(900)
        self.setMaximumHeight(500)
        self.setMinimumHeight(500)


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    progwidget = mainWindow()
    progwidget.resize(400, 400)
    progwidget.show()
    sys.exit(app.exec_())
