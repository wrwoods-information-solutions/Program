# -*- coding: utf-8 -*-

"""
Created on June 12 2021

@author: W.R.Woods

Version:  1.O.0
"""

from PyQt5 import QtCore, QtGui, QtWidgets


# class UC():
#     """
#     class to set up of under Consturction

#     """
#     def __init__(self):
#         super().__init__()
#         self.displayUC()

def displayhome(self):
      
        self.frmuc = QtWidgets.QFrame()
        self.frmuc.setGeometry(QtCore.QRect(0, 20, 1600, 1080))
        self.frmuc.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frmuc.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frmuc.setObjectName("frmuc")
        self.imguc = QtWidgets.QLabel()
        self.imguc.setGeometry(QtCore.QRect(0, 50, 791, 521))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(20)
        self.imguc.setFont(font)
        self.imguc.setFrameShape(QtWidgets.QFrame.Box)
        self.imguc.setText("")
        self.imguc.setPixmap(QtGui.QPixmap("Images/UnderConstruction.gif"))
        self.imguc.setScaledContents(True)
        self.imguc.setAlignment(QtCore.Qt.AlignCenter)
        self.imguc.setObjectName("imguc")
        # QtCore.QMetaObject.connectSlotsByName()
        