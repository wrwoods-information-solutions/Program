# -*- coding: utf-8 -*-

"""
Created on June 12 2021

@author: W.R.Woods

Version:  1.O.0
"""

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFrame, QLabel


class Uc(QFrame):
    """
    class to set up of under construction

    """

    def __init__(self, parent, controller):
        super().__init__()
        QFrame.__init__(self, parent)
        self.controller = controller
        self.frmUc = QFrame()
        self.frmUc.setGeometry(QtCore.QRect(0, 100,965, 1920))
        self.frmUc.setFrameShape(QFrame.StyledPanel)
        self.frmUc.setFrameShadow(QFrame.Raised)
        self.frmUc.setObjectName("frmUc")
        self.imguc = QtWidgets.QLabel()
        self.imguc.setGeometry(QtCore.QRect(0, 50, 791, 521))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(20)
        self.imguc.setFont(font)
        self.imguc.setFrameShape(QFrame.Box)
        self.imguc.setText("")
        self.imguc.setPixmap(QtGui.QPixmap("Images/UnderConstruction.gif"))
        self.imguc.setScaledContents(True)
        self.imguc.setAlignment(QtCore.Qt.AlignCenter)
        self.imguc.setObjectName("imguc")

        