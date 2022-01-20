# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:23:04 2021

@author: wricw

Version:  0.0.0

"""
import sys
import logging
# import rollerbar
from PyQt5 import QtCore , QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QMainWindow,QAction,QFrame,QLabel
from PyQt5.QtGui import QIcon

from PyQt5.QtCore import QRect
import csv
import os.path
from datetime  import date
# from attrs import asdict, define, make_class, Factory

# Create a custom logger
logging.basicConfig(level=logging.DEBUG)
wrwislog = logging.getLogger(__name__)
# Create handlers
c_handler = logging.StreamHandler()
f_handler = logging.FileHandler('file.log')
c_handler.setLevel(logging.WARNING)
f_handler.setLevel(logging.ERROR)

# Create formatters and add it to handlers
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
f_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
c_handler.setFormatter(c_format)
f_handler.setFormatter(f_format)

# Add handlers to the logger
wrwislog.addHandler(c_handler)
wrwislog.addHandler(f_handler)

# wrwislog.warning('This is a warning')
# wrwislog.error('This is an error')

# rollbar.init('POST_SERVER_ITEM_ACCESS_TOKEN', 'development')  # access_token, environment

# try:
#     main_app_loop()
# except IOError:
#     rollbar.report_message('Got an IOError in the main loop', 'warning')
# except:
#     # catch-all
#     rollbar.report_exc_info()
#     # equivalent to rollbar.report_exc_info(sys.exc_info())

def  loadcsv(file):
    if file == 'all':
        files = ('system','codes','members','units','connect')
        for file in files:
            if os.path.isfile('data/' + file +'.cvs'):
              result_list=[]
              reader = csv.DictReader(open('data/' + file +'.cvs'))
              for row in reader:
                  result_list.append(dict(row))
              return result_list
            else:
                   wrwislog.warning('%s.csv does not exist',file)
    if os.path.isfile('data/' + file +'.cvs'):
          result_list=[]
          # with open('data/' + file +'.cvs','a+') as csv_file:
          reader = csv.DictReader(open('data/' + file +'.cvs'))
          for row in reader:
              result_list.append(row)
          return result_list
              
    else:
            wrwislog.warning('%s.csv does not exist',file)

def savecsv(file, fldnames, content, datestamp: bool):
    if not os.path.isfile('data/' + file +'.cvs'):
        with open('data/' + file + '.cvs', 'w') as csv_file:
           writer = csv.DictWriter(csv_file, fieldnames=fldnames)
           writer.writeheader()
    with open('data/' + file + '.cvs', 'a+') as csv_file:
        if datestamp:
            if content['createdate'] == '':
                content['createdate'] = date.today()
            content['updatedate'] = date.today()
            writer = csv.DictWriter(csv_file, fieldnames=fldnames)
            writer.writerow(content)    

def updater(file):
    with open(file, newline= "") as file:
        readData = [row for row in csv.DictReader(file)]
        # print(readData)
        readData[0]['Rating'] = '9.4'
        # print(readData)

    readHeader = readData[0].keys()
    savecsv(file,readHeader, readData, True)

def quit():
    quit()
    
class MainProg(QMainWindow):
    """
    class to set up of MainProg

    """
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height() - 50 - 65
        self.width = self.screenRect.width()
        print('height is '+str(self.height) + '  width is '+str(self.width))
        self.setGeometry(50, 50, self.width, self.height)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        container = QFrame(self)
        self.create_menu()
        self.frames = {}
        for F in (Blank, Home,Settingeditor, Uc):
              frame = F(container, self)
              frame.setGeometry(QtCore.QRect(0, 100, self.width, self.height - 100))
              self.frames[F] = frame
        self.show_frame(Blank)
        self.show_frame(Home)
        try:
            self.setWindowTitle("Housing Charge Calculator")
            self.setWindowIcon(QIcon('/Images/SCIcon.ico'))
        except Exception as e:
            print(str(e))

    def show_frame(self,cont):

        frame = self.frames[cont]
        frame.setFrameShadow(QFrame.Raised)
        # self.container = cont.container 


    def create_menu(self):
        """

        Function to call create the menu

        """
        mainmenu = self.menuBar()
        settingmenu = mainmenu.addMenu("Setting")

        settingeditor = QAction("Setting Editor", self)
        settingmenu.addAction(settingeditor)
        settingeditor.triggered.connect(self.editor)

        membersaction = QAction("Members", self)
        settingmenu.addAction(membersaction)
        membersaction.triggered.connect(self.members)

        unitsaction = QAction("Units", self)
        settingmenu.addAction(unitsaction)
        unitsaction.triggered.connect(self.units)


        ratescaleaction = QAction("RateScale", self)
        settingmenu.addAction(ratescaleaction)
        ratescaleaction.triggered.connect(self.ratescale)

        codesaction = QAction("Codes", self)
        settingmenu.addAction(codesaction)
        codesaction.triggered.connect(self.codes)

        exitaction = QAction('Exit', self)
        settingmenu.addAction(exitaction)
        exitaction.triggered.connect(self.closeapp)

    def editor(self):
        """

        Function to call Setting Editor

        """
        wrwislog.debug('in Settingeditor')
        self.show_frame(Blank)
        self.show_frame(Settingeditor)
        

    def members(self):
        """

        Function to call nenbers

        """
        wrwislog.debug('in members')
        self.show_frame(Blank)
        self.show_frame(Uc)


    def units(self):
        """

        Function to call units

        """
        self.show_frame(Blank)
        self.show_frame(Uc)


    def ratescale(self):
        """

        Function to call ratescale

        """
        self.show_frame(Blank)
        self.show_frame(Uc)



    def codes(self):
        """

        Function to call codes

        """
        self.show_frame(Blank)
        self.show_frame(Uc)
        

    def closeapp(self):
        """

        Function to call close app

        """
        self.close()
        quit()
        
"""
    class to display Blank

"""
class Blank(QFrame):

    def __init__(self, parent, container):
        QFrame.__init__(self, parent)            
        wrwislog.debug('inside Blank')
        HCCalculator =  QLabel()
        HCCalculator.setGeometry(QtCore.QRect(100, 220, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        HCCalculator.setFont(font)
        HCCalculator.setAlignment(QtCore.Qt.AlignCenter)
        HCCalculator.setText(' ')
        HCCalculator.setObjectName("HCCalculator")

"""
    class to display home

GIT"""

class Home(QFrame):

    def __init__(self, parent, container):
        QFrame.__init__(self, parent)            
        sys = loadcsv('system')
        wrwislog.debug('inside Home')
        HCCalculator = QtWidgets.QLabel(container)
        HCCalculator.setGeometry(QtCore.QRect(560, 220, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        HCCalculator.setFont(font)
        HCCalculator.setAlignment(QtCore.Qt.AlignCenter)
        HCCalculator.setText('Housing Charge Calculator')
        HCCalculator.setObjectName("HCCalculator")
    
    
        ontversion = QtWidgets.QLabel(container)
        ontversion.setGeometry(QtCore.QRect(600, 400, 561, 50))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        ontversion.setFont(font)
        ontversion.setAlignment(QtCore.Qt.AlignCenter)
        ontversion.setText("Ontario Version")
        ontversion.setObjectName("ontversion")
    
        versiondate = QtWidgets.QLabel(container)
        versiondate.setGeometry(QtCore.QRect(600, 500, 561, 50))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(25)
        versiondate.setFont(font)
        versiondate.setAlignment(QtCore.Qt.AlignCenter)
        versiondate.setText("Version 1.0.0")
        versiondate.setObjectName("versiondate")
    
        logo = QtWidgets.QLabel(container)
        logo.setGeometry(QtCore.QRect(800, 600, 100, 100))
        logo.setText("")
        logo.setPixmap(QtGui.QPixmap("Images/site_logo.gif"))
        logo.setScaledContents(True)
        logo.setObjectName("logo")
    
        lbltop = QtWidgets.QLabel(container)
        lbltop.setGeometry(QtCore.QRect(900, 600, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbltop.setFont(font)
        lbltop.setText("WRWoods Infornation")
        lbltop.setObjectName("lbltop")
    
        lblbtm = QtWidgets.QLabel(container)
        lblbtm.setGeometry(QtCore.QRect(900, 680, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lblbtm.setFont(font)
        lblbtm.setText("Solutions Inc.")
        lblbtm.setObjectName("lblbtm")
        lbladr1 = QtWidgets.QLabel(container)
        lbladr1.setGeometry(QtCore.QRect(900, 700, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbladr1.setFont(font)
        lbladr1.setText("22-456 Kingscourt Drive")
        lbladr1.setObjectName("lbladr1")
        lbladr2 = QtWidgets.QLabel(container)
        lbladr2.setGeometry(QtCore.QRect(900, 720, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbladr2.setFont(font)
        lbladr2.setText("Waterloo On N2K 3S1")
        lbladr2.setObjectName("lbladr2")
        lbltel = QtWidgets.QLabel(container)
        lbltel.setGeometry(QtCore.QRect(900, 740, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbltel.setFont(font)
        lbltel.setText("519-886-6649")
        lbltel.setObjectName("lbltel")

"""
    class to display Setting Editor

"""
class Settingeditor(QFrame):

    def __init__(self, parent, container):
        QFrame.__init__(self,parent)            
        sys = loadcsv('system')
        wrwislog.debug('inside settingeditor')
        lbltitle = QtWidgets.QLabel(container)
        lbltitle.setGeometry(QtCore.QRect(720, 75, 400, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        lbltitle.setFont(font)
        lbltitle.setText('Setting Editor')
        lbltitle.setObjectName("lbltitle")


        lblbaseelement = QtWidgets.QLabel(container)
        lblbaseelement.setGeometry(QtCore.QRect(50, 120, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblbaseelement.setFont(font)
        lblbaseelement.setText = 'Base Element'
        lblbaseelement.setObjectName("lblbaseelement")

        cboxbaseelement = QtWidgets.QComboBox(container)
        cboxbaseelement.addItems(['system', 'codes', 'members', 'units', 'connect'])
        cboxbaseelement.setGeometry(QtCore.QRect(50, 190, 125, 25))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        cboxbaseelement.setFont(font)
        cboxbaseelement.setObjectName("cboxbaseelemwnt")


        lblpostonscreen = QtWidgets.QLabel(container)
        lblpostonscreen.setGeometry(QtCore.QRect(204, 120, 210, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblpostonscreen.setFont(font)
        lblpostonscreen.setText = 'Positon on the Screen'
        lblpostonscreen.setObjectName("lblpostonscreen")
        
        lblheight = QtWidgets.QLabel(container)
        lblheight.setGeometry(QtCore.QRect(210, 150, 66, 25))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblheight.setFont(font)
        lblbaseelement.setText = 'Height'
        lblheight.setObjectName("lblheight")

        lblwidth = QtWidgets.QLabel(container)
        lblwidth.setGeometry(QtCore.QRect(351, 150, 66, 25))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblwidth.setFont(font)
        lblwidth.setText = 'Width'
        lblwidth.setObjectName("lblwidth")

        lblelementnane = QtWidgets.QLabel(container)
        lblelementnane.setGeometry(QtCore.QRect(460, 120, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblelementnane.setFont(font)
        lblelementnane.setText = 'Element Nane'
        lblelementnane.setObjectName("lblelementnane")
   
        lblniumberofitems = QtWidgets.QLabel(container)
        lblniumberofitems.setGeometry(QtCore.QRect(630, 120, 166, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblniumberofitems.setFont(font)
        lblniumberofitems.setText = 'Number of Items'
        lblniumberofitems.setObjectName("lblniumberofitems")
        
        leheight = QtWidgets.QLineEdit(container)
        leheight.setGeometry(QtCore.QRect(210, 190, 50, 25))
        leheight.setObjectName("leheight")
        
        lewidth = QtWidgets.QLineEdit(container)
        lewidth.setGeometry(QtCore.QRect(350, 190, 50, 25))
        lewidth.setObjectName("lewidth")
        
        leeementname = QtWidgets.QLineEdit(container)
        leeementname.setGeometry(QtCore.QRect(460, 190, 130, 25))
        leeementname.setObjectName("leeementname")

        lenunberofitems = QtWidgets.QLineEdit(container)
        lenunberofitems.setGeometry(QtCore.QRect(670, 190, 50, 25))
        lenunberofitems.setObjectName("lenunberofitems")

        leitem = QtWidgets.QLineEdit(container)
        leitem.setGeometry(QtCore.QRect(358, 364, 766, 25))
        leitem.setObjectName("leitem")

        lblitem = QtWidgets.QLabel(container)
        lblitem.setGeometry(QtCore.QRect(360, 360, 773, 25))
        lblitem.setObjectName("lblitem")

        btmedit = QtWidgets.QPushButton('Edit')
        btmedit.setGeometry(QtCore.QRect(1133, 360, 60, 26))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        btmedit.setFont(font)
        btmedit.setObjectName("btmedit")
        
        btmadd = QtWidgets.QPushButton('Add')
        btmadd.setGeometry(QtCore.QRect(1204, 363, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        btmadd.setFont(font)
        btmadd.setObjectName("btmadd")
        
        btmdelete = QtWidgets.QPushButton('Delete')
        btmdelete.setGeometry(QtCore.QRect(1285, 363, 80, 26))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        btmdelete.setFont(font)
        btmdelete.setObjectName("btmdelete")
        
        
class Uc(QFrame):
    """
    class to set up of under construction

    """

    def __init__(self,parent, container):
        QFrame.__init__(self, parent)
        wrwislog.debug('inside UC')
        imguc = QLabel()
        imguc.setGeometry(QRect(0, 50, 791, 521))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(20)
        imguc.setFont(font)
        imguc.setFrameShape(QFrame.Box)
        imguc.setText("")
        imguc.setPixmap(QtGui.QPixmap("Images/UnderConstruction.gif"))
        imguc.setScaledContents(True)
        imguc.setAlignment(QtCore.Qt.AlignCenter)
        imguc.setObjectName("imguc")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainProg()
    win.show()
    app.exec()
    sys.exit(app.exec_())



