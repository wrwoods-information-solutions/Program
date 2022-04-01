# -*- coding: utf-8 -*-
"""
Created on Wed July 28 2021
@author: WR Woods

Version:  0.0.0
"""
import sys
import logging
from PyQt5 import QtCore , QtGui, QtWidgets 
from PyQt5.QtWidgets import QApplication,QMainWindow, QStackedWidget, QVBoxLayout, QGridLayout, QWidget, QAction, QLabel,QComboBox,QLineEdit,QSpinBox, QPushButton,QHBoxLayout,QMenuBar
from PyQt5.QtGui import QIcon,QFont,QPixmap,QIntValidator
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

class Blank(QWidget):
    def __init__(self):
        """
            class to display Blank

        """
        super().__init__()
        wrwislog.debug('inside Blank')
        layout = QGridLayout()
        
        # Add widgets to the blank

        layout.addWidget(QLabel(' '),0,0)

        # Set the layout on the application's window

        self.setLayout(layout) 


class Home(QWidget):
        """
            class to display home

        """
        def __init__(self):
            super().__init__()
            sys = loadcsv('system')
            wrwislog.debug('inside Home')

            # Create a QGridLayout instance

            layout = QGridLayout()

            # Add widgets to the home
            
            layout.addWidget(QLabel('Housing Charge Calculator',font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)
            layout.addWidget(QLabel(vars.versionarea,font=LARGE_FONT),2,2,1,3, Qt.AlignHCenter)
            layout.addWidget(QLabel('Verson No.:  ' + vars.version,font=LARGE_FONT),3,2,1,3, Qt.AlignHCenter)
            im = QPixmap("Images/site_logo.gif")
            label = QLabel()
            label.setPixmap(im)
            layout.addWidget(label,4,2,1,3, Qt.AlignHCenter)
            layout.addWidget(QLabel("WRWoods Infornation",font=TINY_FONT),5,3,1,1, Qt.AlignRight)
            layout.addWidget(QLabel("Solutions Inc.",font=TINY_FONT),5,3,1,1, Qt.AlignLeft)
            layout.addWidget(QLabel("22-456 Kingscourt Drive",font=TINY_FONT),6,3,1,1, Qt.AlignLeft)
            layout.addWidget(QLabel("Waterloo On N2K 3S1",font=TINY_FONT),7,3,1,1, Qt.AlignLeft)
            layout.addWidget(QLabel("519-886-6649",font=TINY_FONT),8,3,1,1, Qt.AlignLeft)


            # Set the home on the application's window

            self.setLayout(layout)
        

class SettingEditor(QWidget): 
    """
        class to display Setting Editor

    """
    def __init__(self):

        super().__init__()
        sys = loadcsv('system')
        wrwislog.debug('inside settingeditor')
        self.setWindowTitle("Setting Editor")

        # Create a QGridLayout instance

        layout = QGridLayout()

        # Add widgets to the Settinged

        layout.addWidget(QLabel('Setting Editor',font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)

        layout.addWidget(QLabel('Base Element',font=NORMAL_FONT),1,0,1,1, Qt.AlignLeft)
        cboxbaseelement = QComboBox()
        cboxbaseelement.addItems(['ADD','system', 'codes', 'members', 'units', 'connect','DELETE'])
        layout.addWidget(cboxbaseelement,3,0,Qt.AlignLeft)
        
        layout.addWidget(QLabel('Positon on the Screen',font=NORMAL_FONT),1,1,1,2, Qt.AlignLeft)
        layout.addWidget(QLabel('Height',font=NORMAL_FONT),2,1,1,1, Qt.AlignLeft)
        scnheight = QSpinBox()
        scnheight.value = 0
        scnheight.maximum = 965
        scnheight.minimum = 0
        scnheight.singleStep = 60
        scnhno = scnheight.value
        layout.addWidget(scnheight,3,1,Qt.AlignLeft)
        layout.addWidget(QLabel('Width',font=NORMAL_FONT),2,2,1,1, Qt.AlignLeft)
        scnwidth = QSpinBox()
        scnwidth.value = 0
        scnwidth.maximum = 1920
        scnwidth.minimum = 0
        scnwidth.singleStep = 60
        scnwno = scnwidth.value
        layout.addWidget(scnwidth,3,2,Qt.AlignLeft)

        layout.addWidget(QLabel('Element Nane',font=NORMAL_FONT),1,3,1,1, Qt.AlignLeft)
        elementname = QLineEdit()
        layout.addWidget(elementname,3,3,Qt.AlignLeft)

        layout.addWidget(QLabel('Number of Items',font=NORMAL_FONT),1,4,1,1, Qt.AlignLeft)
        noofitems = QSpinBox()
        noofitems.value = 1
        noofitems.maximum = 99
        noofitems.minimum = 1
        noofitems.singleStep =1
        noitem = noofitems.value
        layout.addWidget(noofitems,3,4 ,Qt.AlignLeft)
        layout.addWidget(QLabel('Item',font=NORMAL_FONT),4,1,Qt.AlignHCenter)
    
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
            layout.addWidget(item,rowno,1,Qt.AlignHCenter)

            btmedit = btmedit+str(rowno)
            btmedit = QPushButton('Edit')
            btmedit.clicked.connect(lambda:self.actionEdit(rowno))  
            layout.addWidget(btmedit,rowno,3,Qt.AlignLeft)

            btmadd = btmadd+str(rowno)
            btmadd = QPushButton('Add')
            btmadd.clicked.connect(lambda:self.actionAdd(rowno))  
            layout.addWidget(btmadd,rowno,2,Qt.AlignHCenter)

            btmdelete = btmdelete+str(rowno)
            btmdelete = QPushButton('Delete')
            btmdelete.clicked.connect(lambda:self.actionDelete(rowno))  
            layout.addWidget(btmdelete,rowno,3,Qt.AlignRight)

        # Set the Settinged on the application's window

        self.setLayout(layout)

    def actionEdit(rowno):
        print('Edit pressed')

    def actionAdd(rowno):
        print('Add pressed')

    def actionDelete(rowno):
        print('Delete pressed')

class Uc(QWidget):    
    def __init__(self):
        super().__init__()
        wrwislog.debug('inside UC')

        # Create a QGridLayout instance

        layout = QGridLayout()

        # Add widgets to the uc

        layout.addWidget(QLabel("Under Construction",font=TITLE_FONT),0,3,1,1, Qt.AlignHCenter)
        im = QPixmap("Images/UnderConstruction.gif")
        label = QLabel()
        label.setPixmap(im)
        layout.addWidget(label,4,2,1,3, Qt.AlignHCenter)

        # Set the uc on the application's window
        self.setLayout(layout)

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
        self.body = QStackedWidget (self)
        self.body.addWidget (Blank())
        self.body.addWidget (Home())
        self.body.addWidget (SettingEditor())
        self.body.addWidget (Uc())
        self.create_menu()
        self.displayHome()        
  
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

        initialize = QAction("Initialize", self)
        settingmenu.addAction(initialize)
        initialize.triggered.connect(self.init)

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
        pass

        
    def outputhc(self):
        """

        Function to call outputhc

        """
        pass 


    def pdf(self):
        """

        Function to call pdf

        """
        pass 


    def printhc(self):
        """

        Function to call printhc

        """
        pass 
    def init(self):
        """

        Function to call Initialize

        """
        wrwislog.debug('in Initialize')
        self.displayUc()
        pass

    def editor(self):
        """

        Function to call Setting Editor

        """
        wrwislog.debug('in editor')
        self.displaySettingEditor()
        pass


    def members(self):
        """

        Function to call nenbers

        """
        wrwislog.debug('in members')
        self.displayUc()
        pass 


    def units(self):
        """

        Function to call units

        """
        wrwislog.debug('in Units')
        self.displayUc()
        pass 


    def ratescale(self):
        """

        Function to call ratescale

        """
        wrwislog.debug('in ratescale')
        self.displayUc()
        pass 


    def codes(self):
        """

        Function to call codes

        """
        wrwislog.debug('in codes')
        self.displayUc()
        pass 


    def helphelp(self):
        """

        Function to call helphelp

        """
        wrwislog.debug('in helphelp')
        self.displayUc()
        pass 



    def calendar(self):
        """

        Function to call Calendar

        """
        wrwislog.debug('in calendar')
        self.displayUc()
        pass 



    def overview(self):
       """

          Function to call overview

       """
       wrwislog.debug('in overview')
       self.displayUc()
       pass 

    def inputhelp(self):
       """

          Function to call input help

       """
       wrwislog.debug('in imput help')
       self.displayUc()
       pass

    def outputhelp(self):
       """

          Function to call outputhelp

       """
       self.displayUc()
       pass

    def codeshelp(self):
       """

          Function to call codeshelp

       """
       self.displayUc()
       pass

    def closeapp(self):
        """

        Function to call close app

        """
        quit()


    def displayBlank(self,parent):

      parent.body.setCurrentIndex(0)

    def displayHome(self):
      self.body.setCurrentIndex(1)

    def displaySettingEditor(self):
      self.body.setCurrentIndex(2)

    def displayUc(self):

      self.body.setCurrentIndex(3)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MainProg()
    win.show()
    app.exec()
    sys.exit(app.exec_())
