from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys
import os

if __name__ == '__main__':

    app = QApplication(sys.argv)


    listWidget = QListWidget()
    listWidget.show()
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir("C:\\Users\\akash\\Downloads\\pics") ]
    images=["C:\\Users\\akash\\Downloads\\pics\\i1.jpg"]
    #ls = ['test', 'test2', 'test3']
    for i in range(len(onlyfiles)):
            label = QtWidgets.QLabel()
            pm = QtGui.QPixmap(join("C:\\Users\\akash\\Downloads\\pics", onlyfiles[i]))
            label.setPixmap(pm.scaled(QtCore.QSize(150,100)))
            item = QtWidgets.QListWidgetItem(str(i))
            item.setSizeHint(QtCore.QSize(100,100))
            listWidget.addItem(item)
            listWidget.setItemWidget(item,label)

    #listWidget.addItem(ls)

    sys.exit(app.exec_())
