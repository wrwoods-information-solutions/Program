# -*- coding: utf-8 -*-
"""
Created on Sat Nov 20 16:52:19 2021

@author: wricw
"""

from PyQt5 import QtGui
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QAction,QFrame,QLabel,QLineEdit


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.central_widget = QtGui.QStackedWidget()
        self.setCentralWidget(self.central_widget)
        login_widget = LoginWidget(self)
        login_widget.button.clicked.connect(self.login)
        self.central_widget.addWidget(login_widget)

    def login(self):
        logged_in_widget = LoggedWidget(self)
        self.central_widget.addWidget(logged_in_widget)
        self.central_widget.setCurrentWidget(logged_in_widget)


class LoginWidget(QWidget):
    def __init__(self, parent=None):
        super(LoginWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.button = QtGui.QPushButton('Login')
        layout.addWidget(self.button)
        self.setLayout(layout)
        # you might want to do self.button.click.connect(self.parent().login) here


class LoggedWidget(QWidget):
    def __init__(self, parent=None):
        super(LoggedWidget, self).__init__(parent)
        layout = QtGui.QHBoxLayout()
        self.label = QtGui.QLabel('logged in!')
        layout.addWidget(self.label)
        self.setLayout(layout)



if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()