# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 16:09:55 2021

@author: wricw
"""
# import sys
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QFrame
# from PyQt5.QtGui import QIcon
# import db


class Home(QFrame):
    """
    class to display home

    """

    def __init__(self, parent, controller):
        super().__init__(self)
        QFrame.__init__(self, parent)
        self.controller = controller
        frmHome = QtWidgets.QFrame(self)
        frmHome.setGeometry(QtCore.QRect(0, 150, self.width, self.height))
        frmHome.setFrameShape(QtWidgets.QFrame.StyledPanel)
        # frmHome.setFrameShadow(QtWidgets.QFrame.Raised)
        frmHome.setObjectName("frmHome")
        lblFellowshipOne = QtWidgets.QLabel()
        lblFellowshipOne.setGeometry(QtCore.QRect(100, 220, 561, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        lblFellowshipOne.setFont(font)
            # self.lblFellowshipOne.setFrameShape(QtWidgets.QFrame.Box)
        lblFellowshipOne.setAlignment(QtCore.Qt.AlignCenter)
        lblFellowshipOne.setText('Housing Charge Calcularor')
        lblFellowshipOne.setObjectName("lblFellowshipOne")
    
    
        lblFellowshipOne_2 = QtWidgets.QLabel()
        lblFellowshipOne_2.setGeometry(QtCore.QRect(400, 400, 561, 50))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        lblFellowshipOne_2.setFont(font)
            # self.lblFellowshipOne_2.setFrameShape(QtWidgets.QFrame.Box)
        lblFellowshipOne_2.setAlignment(QtCore.Qt.AlignCenter)
        lblFellowshipOne_2.setText("Ontario Version")
        lblFellowshipOne_2.setObjectName("lblFellowshipOne_2")
    
            # self.lblFellowshipOne_tool = QtWidgets.QLabel(self.frmHome)
            # self.lblFellowshipOne_tool.setGeometry(QtCore.QRect(400, 500, 561, 50))
            # font = QtGui.QFont()
            # font.setFamily("Garamond")
            # font.setPointSize(40)
            # self.lblFellowshipOne_tool.setFont(font)
            # # self.lblFellowshipOne_tool.setFrameShape(QtWidgets.QFrame.Box)
            # self.lblFellowshipOne_tool.setAlignment(QtCore.Qt.AlignCenter)
            # self.lblFellowshipOne_tool.setText("Tool")
            # self.lblFellowshipOne_tool.setObjectName("lblFellowshipOne_tool")
    
        lblFellowshipOne_3 = QtWidgets.QLabel()
        lblFellowshipOne_3.setGeometry(QtCore.QRect(400, 600, 561, 50))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(25)
        lblFellowshipOne_3.setFont(font)
            # self.lblFellowshipOne_3.setFrameShape(QtWidgets.QFrame.Box)
        lblFellowshipOne_3.setAlignment(QtCore.Qt.AlignCenter)
        lblFellowshipOne_3.setText("July 2021")
        lblFellowshipOne_3.setObjectName("lblFellowshipOne_3")
    
        label = QtWidgets.QLabel()
        label.setGeometry(QtCore.QRect(600, 800, 100, 100))
        label.setText("")
        label.setPixmap(QtGui.QPixmap("Images/site_logo.gif"))
        label.setScaledContents(True)
        label.setObjectName("label")
    
        lblline1 = QtWidgets.QLabel()
        lblline1.setGeometry(QtCore.QRect(700, 800, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lblline1.setFont(font)
        lblline1.setText("WRWoods Infornation")
        lblline1.setObjectName("lblline1")
    
        lblline2 = QtWidgets.QLabel()
        lblline2.setGeometry(QtCore.QRect(700, 890, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lblline2.setFont(font)
        lblline2.setText("Solutions Inc.")
        lblline2.setObjectName("lblline2")
