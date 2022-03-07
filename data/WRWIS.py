"""
WRWIS stamp

"""

"""
    super().__init__()
    wrwislog.debug('inside Wrwis')
    # Create a QGridLayout instance

    layout = QGridLayout()
    
    # Add widgets to the layout

    layout.addWidget(QLabel('Housing Charge Calculator',font=LARGE_FONT),0,3,1,1, Qt.AlignHCenter)

"""
def __init__(layout):
    layout.addWidget(QPixmap("Images/site_logo.gif"),4,2,1,3, Qt.AlignHCenter)
    layout.addWidget(QLabel("WRWoods Infornation",font=TINY_FONT),5,3,1,1, Qt.AlignRight)
    layout.addWidget(QLabel("Solutions Inc.",font=TINY_FONT),5,3,1,1, Qt.AlignLeft)
    layout.addWidget(QLabel("22-456 Kingscourt Drive",font=TINY_FONT),6,3,1,1, Qt.AlignLeft)
    layout.addWidget(QLabel("Waterloo On N2K 3S1",font=TINY_FONT),7,3,1,1, Qt.AlignLeft)
    layout.addWidget(QLabel("519-886-6649",font=TINY_FONT),8,3,1,1, Qt.AlignLeft)
