# -*- coding: utf-8 -*-
"""
Created on Wed July 28 2021
@author: WR Woods

Version:  0.0.0
"""
import sys
import logging
from PyQt5 import QtCore, QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction,QFrame
from PyQt5.QtGui import QIcon
import csv
import os.path
from datetime  import date
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

"""
    class to display blank frame

"""

class Blank(QFrame):

    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)            
        wrwislog.debug('inside Blank')
        HCCalculator = QtWidgets.QLabel(controller)
        HCCalculator.setGeometry(QtCore.QRect(560, 220, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        HCCalculator.setFont(font)
        HCCalculator.setAlignment(QtCore.Qt.AlignCenter)
        HCCalculator.setText(' ')
        HCCalculator.setObjectName("HCCalculator")

"""
    class to display home

"""

class Home(QFrame):

    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)            
        wrwislog.debug('inside Home')
        HCCalculator = QtWidgets.QLabel(controller)
        HCCalculator.setGeometry(QtCore.QRect(560, 220, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        HCCalculator.setFont(font)
        HCCalculator.setAlignment(QtCore.Qt.AlignCenter)
        HCCalculator.setText('Housing Charge Calcularor')
        HCCalculator.setObjectName("HCCalculator")
    
    
        ontversion = QtWidgets.QLabel(controller)
        ontversion.setGeometry(QtCore.QRect(600, 400, 561, 50))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(40)
        ontversion.setFont(font)
        ontversion.setAlignment(QtCore.Qt.AlignCenter)
        ontversion.setText("Ontario Version")
        ontversion.setObjectName("ontversion")
    
        versiondate = QtWidgets.QLabel(controller)
        versiondate.setGeometry(QtCore.QRect(600, 500, 561, 50))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(25)
        versiondate.setFont(font)
        versiondate.setAlignment(QtCore.Qt.AlignCenter)
        versiondate.setText("Version 1.0.0")
        versiondate.setObjectName("versiondate")
    
        logo = QtWidgets.QLabel(controller)
        logo.setGeometry(QtCore.QRect(800, 600, 100, 100))
        logo.setText("")
        logo.setPixmap(QtGui.QPixmap("Images/site_logo.gif"))
        logo.setScaledContents(True)
        logo.setObjectName("logo")
    
        lbltop = QtWidgets.QLabel(controller)
        lbltop.setGeometry(QtCore.QRect(900, 600, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbltop.setFont(font)
        lbltop.setText("WRWoods Infornation")
        lbltop.setObjectName("lbltop")
    
        lblbtm = QtWidgets.QLabel(controller)
        lblbtm.setGeometry(QtCore.QRect(900, 680, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lblbtm.setFont(font)
        lblbtm.setText("Solutions Inc.")
        lblbtm.setObjectName("lblbtm")
        lbladr1 = QtWidgets.QLabel(controller)
        lbladr1.setGeometry(QtCore.QRect(900, 700, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbladr1.setFont(font)
        lbladr1.setText("22-456 Kingscourt Drive")
        lbladr1.setObjectName("lbladr1")
        lbladr2 = QtWidgets.QLabel(controller)
        lbladr2.setGeometry(QtCore.QRect(900, 720, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbladr2.setFont(font)
        lbladr2.setText("Waterloo On N2K 3S1")
        lbladr2.setObjectName("lbladr2")
        lbltel = QtWidgets.QLabel(controller)
        lbltel.setGeometry(QtCore.QRect(900, 740, 481, 14))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setBold(True)
        font.setWeight(75)
        lbltel.setFont(font)
        lbltel.setText("519-886-6649")
        lbltel.setObjectName("lbltel")


class Settingeditor(QFrame):
    """
    class to set up of Setting Editor

    """

    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)            
        sys = loadcsv('system')
        wrwislog.debug('inside settingeditor')
        lbltitle= QtWidgets.QLabel(controller)
        lbltitle.setGeometry(QtCore.QRect(560, 220, 800, 100))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(18)
        lbltitle.setFont(font)
        lbltitle.setObjectName("lbltitle")
        lbbaseelementl = QtWidgets.QLabel(controller)
        lbbaseelementl.setGeometry(QtCore.QRect(50, 120, 130, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lbbaseelementl.setFont(font)
        lbbaseelementl.setObjectName("lbbaseelementl")
        lblpostonscreen = QtWidgets.QLabel(controller)
        lblpostonscreen.setGeometry(QtCore.QRect(204, 120, 210, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblpostonscreen.setFont(font)
        lblpostonscreen.setObjectName("lblpostonscreen")
        lblheight = QtWidgets.QLabel(controller)
        lblheight.setGeometry(QtCore.QRect(210, 150, 66, 25))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblheight.setFont(font)
        lblheight.setObjectName("lblheight")
        lblwidth = QtWidgets.QLabel(controller)
        lblwidth.setGeometry(QtCore.QRect(351, 150, 66, 25))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblwidth.setFont(font)
        lblwidth.setObjectName("lblwidth")
        lblelementnane = QtWidgets.QLabel(controller)
        lblelementnane.setGeometry(QtCore.QRect(460, 120, 140, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblelementnane.setFont(font)
        lblelementnane.setObjectName("lblelementnane")
        lblniumberofitems = QtWidgets.QLabel(controller)
        lblniumberofitems.setGeometry(QtCore.QRect(630, 120, 166, 20))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        lblniumberofitems.setFont(font)
        lblniumberofitems.setObjectName("lblniumberofitems")
        cboxbaseelemwnt = QtWidgets.QComboBox(controller)
        cboxbaseelemwnt.setGeometry(QtCore.QRect(50, 190, 124, 25))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        cboxbaseelemwnt.setFont(font)
        cboxbaseelemwnt.setObjectName("cboxbaseelemwnt")
        leheight = QtWidgets.QLineEdit(controller)
        leheight.setGeometry(QtCore.QRect(210, 190, 50, 25))
        leheight.setObjectName("leheight")
        lewidth = QtWidgets.QLineEdit(controller)
        lewidth.setGeometry(QtCore.QRect(350, 190, 50, 25))
        lewidth.setObjectName("lewidth")
        leeementname = QtWidgets.QLineEdit(controller)
        leeementname.setGeometry(QtCore.QRect(460, 190, 130, 25))
        leeementname.setObjectName("leeementname")
        lenunberofitems = QtWidgets.QLineEdit(controller)
        lenunberofitems.setGeometry(QtCore.QRect(670, 190, 50, 25))
        lenunberofitems.setObjectName("lenunberofitems")
        leitem = QtWidgets.QLineEdit(controller)
        leitem.setGeometry(QtCore.QRect(358, 364, 766, 25))
        leitem.setObjectName("leitem")
        lblitem = QtWidgets.QLabel(controller)
        lblitem.setGeometry(QtCore.QRect(360, 360, 773, 25))
        lblitem.setObjectName("lblitem")
        btmedit = QtWidgets.QPushButton(controller)
        btmedit.setGeometry(QtCore.QRect(1133, 360, 60, 26))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        btmedit.setFont(font)
        btmedit.setObjectName("btmedit")
        btmadd = QtWidgets.QPushButton(controller)
        btmadd.setGeometry(QtCore.QRect(1204, 363, 71, 26))
        font = QtGui.QFont()
        font.setFamily("Garamond")
        font.setPointSize(14)
        btmadd.setFont(font)
        btmadd.setObjectName("btmadd")
        btmdelete = QtWidgets.QPushButton(controller)
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

    def __init__(self, parent, controller):
        QFrame.__init__(self, parent)
        wrwislog.debug('inside UC')
        imguc = QtWidgets.QLabel()
        imguc.setGeometry(QtCore.QRect(0, 50, 791, 521))
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

class MainProg(QMainWindow):
    """
    class to set up of MainProg

    """
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height() - 50 - 65
        self.width = self.screenRect.width()
        print('height is '+str(self.height) + '  width is '+str(self.width))
        self.setGeometry(0, 50, self.width, self.height)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setWindowTitle("Housing Charge Calculator")
        self.setWindowIcon(QIcon('Images/SCIcon.ico'))
        container =  QtWidgets.QFrame(self)
        self.frames = {}
        for F in (Blank,Home, Settingeditor, Uc):
             frame = F(container, self)
             self.frames[F] = frame
             self.setGeometry(QtCore.QRect(0, 100, self.width, self.height))


        self.create_menu()
        self.show_frame(Blank)
        self.show_frame(Home)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.setFrameShadow(QFrame.Raised)


    def create_menu(self):
        """

        Function to call create the menu

        """
        mainmenu = self.menuBar()

        createmenu = mainmenu.addMenu('Calculate')
        
        calculateaction = QAction('Input', self)
        createmenu.addAction(calculateaction)
        calculateaction.triggered.connect(self.inputhc)

        outputhcaction = QAction('Output', self)
        createmenu.addAction(outputhcaction)
        outputhcaction.triggered.connect(self.outputhc)

        pdfaction = QAction('PDF', self)
        createmenu.addAction(pdfaction)
        pdfaction.triggered.connect(self.pdf)

        docxaction = QAction('Docx', self)
        createmenu.addAction(docxaction)
        docxaction.triggered.connect(self.pdf)

        printhcaction = QAction('Print', self)
        createmenu.addAction(printhcaction)
        printhcaction.triggered.connect(self.printhc)

        exitaction = QAction('Exit', self)
        createmenu.addAction(exitaction)
        exitaction.triggered.connect(self.closeapp)

        settingmenu = mainmenu.addMenu("Setting")

        settingeditor = QAction("Settung Editor", self)
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

        helpaction = QAction("HeLp", self)
        settingmenu.addAction(helpaction)
        helpaction.triggered.connect(self.helphelp)

        chalendaraction = QAction("Chalendar", self)
        settingmenu.addAction(chalendaraction)
        chalendaraction.triggered.connect(self.calendar)

        helpmenu = mainmenu.addMenu("Help")

        overviewaction = QAction("Overview", self)
        helpmenu.addAction(overviewaction)
        overviewaction.triggered.connect(self.overview)

        inputaction = QAction("Input", self)
        helpmenu.addAction(inputaction)
        inputaction.triggered.connect(self.inputhelp)

        outputaction = QAction("Output", self)
        helpmenu.addAction(outputaction)
        outputaction.triggered.connect(self.outputhelp)

        codesaction = QAction("Codes", self)
        helpmenu.addAction(codesaction)
        codesaction.triggered.connect(self.codeshelp)

    def inputhc(self):
        """

        Function to call inputhc

        """
        self.show_frame(Uc)


        
    def outputhc(self):
        """

        Function to call outputhc

        """
        self.show_frame(Uc)



    def pdf(self):
        """

        Function to call pdf

        """
        self.show_frame(Uc)



    def printhc(self):
        """

        Function to call printhc

        """
        self.show_frame(Uc)



    def editor(self):
        """

        Function to call Setting Editor

        """
        wrwislog.debug('in editor')
        self.show_frame(Settingeditor)


    def members(self):
        """

        Function to call nenbers

        """
        wrwislog.debug('in members')
        self.show_frame(Uc)



    def units(self):
        """

        Function to call units

        """
        wrwislog.debug('in Units')
        self.show_frame(Uc)



    def ratescale(self):
        """

        Function to call ratescale

        """
        wrwislog.debug('in ratescalw')
        self.show_frame(Uc)



    def codes(self):
        """

        Function to call codes

        """
        wrwislog.debug('in codes')
        self.show_frame(Uc)



    def helphelp(self):
        """

        Function to call helphelp

        """
        wrwislog.debug('in helphelp')
        self.show_frame(Uc)




    def calendar(self):
        """

        Function to call Calendar

        """
        wrwislog.debug('in calendar')
        self.show_frame(Uc)




    def overview(self):
       """

          Function to call overview

       """
       wrwislog.debug('in overview')
       self.show_frame(Uc)




    def inputhelp(self):
       """

          Function to call input help

       """
       wrwislog.debug('in imput help')
       self.show_frame(Uc)



    def outputhelp(self):
       """

          Function to call outputhelp

       """
       self.show_frame(Uc)




    def codeshelp(self):
       """

          Function to call codeshelp

       """
       self.show_frame(Uc)



    def closeapp(self):
        """

        Function to call close app

        """
        self.close()
        quit()



if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainProg()
    win.show()
    app.exec()
    sys.exit(app.exec_())
