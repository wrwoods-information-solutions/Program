# -*- coding: utf-8 -*-
"""
Created on Fri Nov 12 15:23:04 2021

@author: wricw

Version:  0.0.0

"""
#from shutil import move
from ast import Str
import sys
import logging
from turtle import home
from typing_extensions import Self
# import rollerbar
from PyQt5 import QtCore , QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow, QStackedWidget, QVBoxLayout, QGridLayout, QWidget, QAction, QLabel,QComboBox,QLineEdit, QPushButton,QHBoxLayout
from PyQt5.QtGui import QIcon,QFont,QPixmap

from PyQt5.QtCore import QRect,Qt
import csv
import os.path
from datetime  import date
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

 
class MainProg(QMainWindow): 
    def blank(self):
        """
            class to display Blank

        """
        wrwislog.debug('inside Blank')
        # Create a QGridLayout instance

        blank = QGridLayout()
        
        # Add widgets to the blank

        blank.addWidget(QLabel(' '),0,0)

        # Set the blank on the application's window

        self.setLayout(blank)

    def home(self):
        """
            class to display home

        """
        sys = loadcsv('system')
        wrwislog.debug('inside Home')
        self.setWindowTitle('Home')
        self.move(0,50)
        self.resize(965,1920 )

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

        self.setLayout(home)

    def settingeditor(self):
        """
            class to display Setting Editor

        """
        sys = loadcsv('system')
        wrwislog.debug('inside settingeditor')
        self.setWindowTitle("Setting Editor")
        self.move(0,100)
        self.resize(965,1820 )

        # Create a QGridLayout instance

        Settinged = QGridLayout()

        # Add widgets to the Settinged

        Settinged.addWidget(QLabel('Setting Editor',font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)

        Settinged.addWidget(QLabel('Base Element',font=NORMAL_FONT),1,0,1,1, Qt.AlignLeft)
        cboxbaseelement = QComboBox()
        cboxbaseelement.addItems(['ADD','system', 'codes', 'members', 'units', 'connect','DELETE'])
        Settinged.addWidget(cboxbaseelement,3,0,Qt.AlignLeft)
        
        Settinged.addWidget(QLabel('Positon on the Screen',font=NORMAL_FONT),1,1,1,2, Qt.AlignLeft)
        Settinged.addWidget(QLabel('Height',font=NORMAL_FONT),2,1,1,1, Qt.AlignLeft)
        scnheight = QLineEdit()
        Settinged.addWidget(scnheight,3,1,Qt.AlignLeft)
        Settinged.addWidget(QLabel('Width',font=NORMAL_FONT),2,2,1,1, Qt.AlignLeft)
        scnwidth = QLineEdit()
        Settinged.addWidget(scnwidth,3,2,Qt.AlignLeft)

        Settinged.addWidget(QLabel('Element Nane',font=NORMAL_FONT),1,3,1,1, Qt.AlignLeft)
        elementname = QLineEdit()
        Settinged.addWidget(elementname,3,3,Qt.AlignLeft)
   
        Settinged.addWidget(QLabel('Number of Items',font=NORMAL_FONT),1,4,1,1, Qt.AlignLeft)
        noofitems = QLineEdit()
        Settinged.addWidget(noofitems,3,4 ,Qt.AlignLeft)
        Settinged.addWidget(QLabel('Item',font=NORMAL_FONT),4,1,Qt.AlignHCenter)
        try:
            noofitem
        except NameError:    
            noofitem = 1
        ln = 0
        rowno = 6
        outtext = []
        btmedit = 'Edit'
        btmadd = 'Add'
        btmdelete = 'Delete'
        for i in range(int(noofitem)):
            item = QLineEdit()
            outtext.append(item.text)
            Settinged.addWidget(item,rowno,1,Qt.AlignHCenter)

            btmedit = btmedit+str(rowno)
            btmedit = QPushButton('Edit')
            btmedit.clicked.connect(lambda:self.actionEdit(rowno))  
            Settinged.addWidget(btmedit,rowno,3,Qt.AlignLeft)

            btmadd = btmadd+str(rowno)
            btmadd = QPushButton('Add')
            btmadd.clicked.connect(lambda:self.actionAdd(rowno))  
            Settinged.addWidget(btmadd,rowno,2,Qt.AlignHCenter)

            btmdelete = btmdelete+str(rowno)
            btmdelete = QPushButton('Delete')
            btmdelete.clicked.connect(lambda:self.actionDelete(rowno))  
            Settinged.addWidget(btmdelete,rowno,3,Qt.AlignRight)

        # Set the Settinged on the application's window

        self.setLayout(Settinged)
 
    def actionEdit(rowno):
        print('Edit pressed')

    def actionAdd(rowno):
        print('Add pressed')

    def actionDelete(rowno):
        print('Delete pressed')
      
    def uc(self):
        super().__init__()
        wrwislog.debug('inside UC')
        self.setWindowTitle("Under Construction")
        self.move(0,100)
        self.resize(965,1820 )

        # Create a QGridLayout instance

        uc = QGridLayout()

        # Add widgets to the uc

        uc.addWidget(QLabel("Under Construction",font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)
        im = QPixmap("Images/UnderConstruction.gif")
        label = QLabel()
        label.setPixmap(im)
        uc.addWidget(label,4,2,1,3, Qt.AlignHCenter)

        # Set the uc on the application's window
        self.setLayout(uc)
    
    """
    class to set up of MainProg

    """
    def __init__(self,  *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.blank = QWidget()
        self.home = QWidget()
        self.settingeditor = QWidget()
        self.uc = QWidget()

        self.body = QStackedWidget (self)
        self.body.addWidget(self.blank)         # index 0
        self.body.addWidget(self.home)          # index 1
        self.body.addWidget(self.settingeditor) # index 2
        self.body.addWidget(self.uc)            # index 3
        
        self.desktop = QApplication.desktop()
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height() - 50 - 65
        self.width = self.screenRect.width()
        print('height is '+str(self.height) + '  width is'+ str(self.width))
       
        self.setGeometry(50, 50, self.width, self.height)
        self.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.setWindowTitle("Housing Charge Calculator")
        self.setWindowIcon(QIcon('/Images/SCIcon.ico'))

        self.create_menu()
        self.body.setCurrentIndex(1)

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
        self.display(2)
        

    def members(self):
        """

        Function to call nenbers

        """
        wrwislog.debug('in members')
        self.display(3)

    def units(self):
        """

        Function to call units

        """
        self.display(3)

    def ratescale(self):
        """

        Function to call ratescale

        """
        self.display(3)

    def codes(self):
        """

        Function to call codes

        """
        self.display(3)

    def closeapp(self):
        """

        Function to call close app

        """
        self.close()
        quit()

    def display(self,i):
      self.body.setCurrentIndex(i)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainProg()
    win.show()
    app.exec()
    sys.exit(app.exec_())