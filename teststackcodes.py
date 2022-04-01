# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:23:04 2021

@author: wricw

Version:  0.0.0

"""
#from shutil import move
from ast import Str
from inspect import currentframe
import sys
import logging
from turtle import home
from typing_extensions import Self
# import rollerbar
from PyQt5 import QtCore , QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow, QStackedWidget, QVBoxLayout, QGridLayout, QWidget, QAction, QLabel,QComboBox,QLineEdit,QSpinBox, QPushButton,QHBoxLayout,QMenuBar
from PyQt5.QtGui import QIcon,QFont,QPixmap,QIntValidator
from PyQt5.QtCore import QRect,Qt
import csv
import os.path
from datetime  import date

from numpy import maximum, minimum
import vars

TITLE_FONT = QFont("Garmond", 20)
NORMAL_FONT = QFont("Garmond", 14)
LARGE_FONT = QFont("Garmond", 16)
SMALL_FONT = QFont("Garmond", 8)
TINY_FONT = QFont("Garmond", 8)

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
    '''
    The above function updates the csv file.
    
    :param file: the name of the file to be saved
    :return: a list of dictionaries.
    '''
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

 

class MainProg (QMainWindow):
    
    """
    class to set up of MainProg

    """
    def __init__(self):
        super().__init__()
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height() - 50 - 65
        self.width = self.screenRect.width()
        print('height is '+str(self.height) + '  width is '+ str(self.width))
       
        self.setGeometry(50, 50, self.width, self.height)
        self.setWindowTitle("Housing Charge Calculator")
        self.setWindowIcon(QIcon('/Images/SCIcon.ico'))

        self.mainmenu = QMenuBar()
        settingmenu = self.mainmenu.addMenu("Setting")

        initialize = QAction("Initialize", self)
        settingmenu.addAction(initialize)
        initialize.triggered.connect(self.init)

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

        self.blank0 = QWidget()
        self.home1 = QWidget()
        self.settingeditor2 = QWidget()
        self.uc99 = QWidget()

        self.home()
        self.settingeditor()
        self.uc()
		
        self.body = QStackedWidget (self)
        self.body.addWidget (self.home1)
        self.body.addWidget (self.settingeditor2)
        self.body.addWidget (self.uc99)

        self.show

    def blank(self):
        """
            class to display Blank

        """
        super().__init__()
        wrwislog.debug('inside Blank')
        blank = QGridLayout()
        
        # Add widgets to the blank

        blank.addWidget(QLabel(' '),0,0)

        # Set the blank on the application's window

        self.blank0.setLayout(blank) 

        """
            class to display home

        """
    def home(self):
        super().__init__()
        sys = loadcsv('system')
        wrwislog.debug('inside Home')

        # Create a QGridLayout instance

        home = QGridLayout()

        # Add widgets to the home
           
        home.addWidget(QLabel('Housing Charge Calculator',font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)
        home.addWidget(QLabel(vars.versionarea,font=LARGE_FONT),2,2,1,3, Qt.AlignHCenter)
        home.addWidget(QLabel('Verson No.:  ' + vars.version,font=LARGE_FONT),3,2,1,3, Qt.AlignHCenter)
        im = QPixmap("Images/site_logo.gif")
        label = QLabel()
        label.setPixmap(im)
        home.addWidget(label,4,2,1,3, Qt.AlignHCenter)
        home.addWidget(QLabel("WRWoods Infornation",font=TINY_FONT),5,3,1,1, Qt.AlignRight)
        home.addWidget(QLabel("Solutions Inc.",font=TINY_FONT),5,3,1,1, Qt.AlignLeft)
        home.addWidget(QLabel("22-456 Kingscourt Drive",font=TINY_FONT),6,3,1,1, Qt.AlignLeft)
        home.addWidget(QLabel("Waterloo On N2K 3S1",font=TINY_FONT),7,3,1,1, Qt.AlignLeft)
        home.addWidget(QLabel("519-886-6649",font=TINY_FONT),8,3,1,1, Qt.AlignLeft)


        # Set the home on the application's window

        self.home1.setLayout(home)
    
    """
        class to display Setting Editor

    """
    def settingeditor(self):
        super().__init__()
        sys = loadcsv('system')
        wrwislog.debug('inside settingeditor')
        self.setWindowTitle("Setting Editor")
        self.move(0,100)
        self.resize(965,1820 )

        # Create a QGridLayout instance

        settinged = QGridLayout()

        # Add widgets to the Settinged

        settinged.addWidget(QLabel('Setting Editor',font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)

        settinged.addWidget(QLabel('Base Element',font=NORMAL_FONT),1,0,1,1, Qt.AlignLeft)
        cboxbaseelement = QComboBox()
        cboxbaseelement.addItems(['ADD','system', 'codes', 'members', 'units', 'connect','DELETE'])
        settinged.addWidget(cboxbaseelement,3,0,Qt.AlignLeft)
        
        settinged.addWidget(QLabel('Positon on the Screen',font=NORMAL_FONT),1,1,1,2, Qt.AlignLeft)
        settinged.addWidget(QLabel('Height',font=NORMAL_FONT),2,1,1,1, Qt.AlignLeft)
        scnheight = QSpinBox()
        scnheight.value = 0
        scnheight.maximum = 965
        scnheight.minimum = 0
        scnheight.singleStep = 60
        scnhno = scnheight.value
        settinged.addWidget(scnheight,3,1,Qt.AlignLeft)
        settinged.addWidget(QLabel('Width',font=NORMAL_FONT),2,2,1,1, Qt.AlignLeft)
        scnwidth = QSpinBox()
        scnwidth.value = 0
        scnwidth.maximum = 1920
        scnwidth.minimum = 0
        scnwidth.singleStep = 60
        scnwno = scnwidth.value
        settinged.addWidget(scnwidth,3,2,Qt.AlignLeft)

        settinged.addWidget(QLabel('Element Nane',font=NORMAL_FONT),1,3,1,1, Qt.AlignLeft)
        elementname = QLineEdit()
        settinged.addWidget(elementname,3,3,Qt.AlignLeft)

        settinged.addWidget(QLabel('Number of Items',font=NORMAL_FONT),1,4,1,1, Qt.AlignLeft)
        noofitems = QSpinBox()
        noofitems.value = 1
        noofitems.maximum = 99
        noofitems.minimum = 1
        noofitems.singleStep =1
        noitem = noofitems.value
        print(noitem)
        settinged.addWidget(noofitems,3,4 ,Qt.AlignLeft)
        settinged.addWidget(QLabel('Item',font=NORMAL_FONT),4,1,Qt.AlignHCenter)
    
        try:
            noofitems
        except NameError:    
            noofitems = 1
        ln = 0
        rowno = 6
        outtext = []
        btmedit = 'Edit'
        btmadd = 'Add'
        btmdelete = 'Delete'
        for i in range(noitem):
            item = QLineEdit()
            outtext.append(item.text)
            settinged.addWidget(item,rowno,1,Qt.AlignHCenter)

            btmedit = btmedit+str(rowno)
            btmedit = QPushButton('Edit')
            btmedit.clicked.connect(lambda:self.actionEdit(rowno))  
            settinged.addWidget(btmedit,rowno,3,Qt.AlignLeft)

            btmadd = btmadd+str(rowno)
            btmadd = QPushButton('Add')
            btmadd.clicked.connect(lambda:self.actionAdd(rowno))  
            settinged.addWidget(btmadd,rowno,2,Qt.AlignHCenter)

            btmdelete = btmdelete+str(rowno)
            btmdelete = QPushButton('Delete')
            btmdelete.clicked.connect(lambda:self.actionDelete(rowno))  
            settinged.addWidget(btmdelete,rowno,3,Qt.AlignRight)

        # Set the Settinged on the application's window

        self.settingeditor2.setLayout(settinged)

    def actionEdit(rowno):
        print('Edit pressed')

    def actionAdd(rowno):
        print('Add pressed')

    def actionDelete(rowno):
        print('Delete pressed')
    
    def uc(self):
        super().__init__()
        wrwislog.debug('inside UC')

        # Create a QGridLayout instance

        uclo = QGridLayout()

        # Add widgets to the uc

        uclo.addWidget(QLabel("Under Construction",font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)
        im = QPixmap("Images/UnderConstruction.gif")
        label = QLabel()
        label.setPixmap(im)
        uclo.addWidget(label,4,2,1,3, Qt.AlignHCenter)

        # Set the uc on the application's window
        self.uc99.setLayout(uclo)


    def init(self):
        """

        Function to call Initialize

        """
        wrwislog.debug('in Initialize')
        self.body.setCurrentWidget(self.uc)
       
    def editor(self):
        """

        Function to call Setting Editor

        """
        wrwislog.debug('in Settingeditor')
        self.body.setCurrentWidget(self.settingeditor)

        

    def members(self):
        """

        Function to call nenbers

        """
        wrwislog.debug('in members')
        self.body.setCurrentWidget(self.uc)


    def units(self):
        """

        Function to call units

        """
        self.body.setCurrentWidget(self.uc)


    def ratescale(self):
        """

        Function to call ratescale

        """
        self.body.setCurrentWidget(self.uc)


    def codes(self):
        """

        Function to call codes

        """
        self.body.setCurrentWidget(self.uc)


    def closeapp(self):
        """

        Function to call close app

        """
        quit()

    def displayhome(self):
      self.body.setCurrentIndex(1)

	
if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainProg()
    win.show()
    app.exec()
    sys.exit(app.exec_())
