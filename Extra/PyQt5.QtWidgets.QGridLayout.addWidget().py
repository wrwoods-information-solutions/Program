#----------------------------------------------------------------------------------------#
# Results for PyQt5.QtWidgets.QGridLayout.addWidget()                                    #
#----------------------------------------------------------------------------------------#
# The 5 Most Common Usages Are: (Derived from 4,574 Examples)                            #
#    PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3) [64.7%]                       #
#    PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3,arg4,arg5) [31.4%]             #
#    PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3,arg4) [1.9%]                   #
#    PyQt5.QtWidgets.QGridLayout.addWidget(arg1) [1.3%]                                  #
#    PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3,arg4,arg5,arg6) [0.6%]         #
#----------------------------------------------------------------------------------------#
# See Examples of Each Usage Below                                                       #
#----------------------------------------------------------------------------------------#
# Thoughts? 😀                                                                          #
# Please Take our Survey! https://aka.ms/ApiExamplesSurvey?origin=results&version=0.0.10 #
#----------------------------------------------------------------------------------------#
# type: ignore                                                                           #



# Examples for PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3) [64.7%]

# Example 1 of 3
# GitHub Source https://github.com/remyroy/CDDA-Game-Launcher/blob/e35bc1b99d0a6649ea979cca5250206871de3765/cddagl/ui/views/fonts.py#L17#L17

def __init__(self):
        super(FontsTab, self).__init__()

        layout = QGridLayout()

        font_window = CataWindow(4, 4, QFont('Consolas'), 18, 9, 18, False)
        layout.addWidget(font_window, 0, 0)
        self.font_window = font_window

        self.setLayout(layout)

# Example 2 of 3
# GitHub Source https://github.com/blawar/nut/blob/a26c5e78208f0833f7cab7e5d766a20542b87316/gui/panes/filters.py#L86#L86

def __init__(self):
		super().__init__()

		layout = QGridLayout(self)

		regions = []
		for region, _ in Config.regionLanguages().items():
			regions.append(region)

		regions.sort()

		width = 4
		i = 0
		for region in regions:
			layout.addWidget(RegionEntry(region), i // width, i % width)
			i += 1

# Example 3 of 3
# GitHub Source https://github.com/krassowski/Anki-Night-Mode/blob/b7bd89878ed3b1deeea92549059670c6be5e8614/night_mode/color_map.py#L95#L95

def fill_layout(self):
        remove = create_button('Remove', self.remove)
        grid = self.grid
        grid.addWidget(self.normal, 0, 1, 1, 3)
        arrow = QLabel('→')
        arrow.setAlignment(Qt.AlignCenter)
        grid.addWidget(arrow, 0, 4)
        grid.addWidget(self.night, 0, 5, 1, 3)
        grid.addWidget(remove, 0, 8)

# Examples for PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3,arg4,arg5) [31.4%]

# Example 1 of 3
# GitHub Source https://github.com/zhimingshenjun/DD_Monitor/blob/0e7fe77a370c69a4dec5aefe29ea99f21760c2b1/LayoutPanel.py#L32#L32

def __init__(self, layout, number):
        super(LayoutWidget, self).__init__()
        self.number = number  # 布局编号
        mainLayout = QGridLayout(self)
        for index, rect in enumerate(layout):
            y, x, h, w = rect
            mainLayout.addWidget(Label(str(index + 1)), y, x, h, w)

# Example 2 of 3
# GitHub Source https://github.com/krassowski/Anki-Night-Mode/blob/b7bd89878ed3b1deeea92549059670c6be5e8614/night_mode/color_map.py#L92#L92

def fill_layout(self):
        remove = create_button('Remove', self.remove)
        grid = self.grid
        grid.addWidget(self.normal, 0, 1, 1, 3)
        arrow = QLabel('→')
        arrow.setAlignment(Qt.AlignCenter)
        grid.addWidget(arrow, 0, 4)
        grid.addWidget(self.night, 0, 5, 1, 3)
        grid.addWidget(remove, 0, 8)

# Example 3 of 3
# GitHub Source https://github.com/robertbasic/pugdebug/blob/716b064b2c06cff6b3495b2c8dd31a01b8e3ce0f/pugdebug/gui/variables.py#L153#L153

def __init__(self, parent, item):
        """Dialog to inspect variables in more detail

        Show the contents of a variable in a text edit.
        """
        super(PugdebugVariableDetails, self).__init__(parent)

        edit = QTextEdit(item.text(2))

        layout = QGridLayout(self)
        layout.addWidget(edit, 0, 0, 0, 0)

        self.setLayout(layout)

        self.show()

# Examples for PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3,arg4) [1.9%]

# Example 1 of 3
# GitHub Source https://github.com/yaronzz/Tidal-Media-Downloader/blob/fa6a9fbbf8f555a9611a05f7bf91855a4e047ea3/TIDALDL-GUI-CROSS/tidal_gui/view/aboutView.py#L28#L28

def __initView__(self):
        grid = QGridLayout(self)
        grid.addWidget(self.__initLogo__(), 0, 0, Qt.AlignLeft)
        grid.addLayout(self.__initContent__(), 0, 1)

# Example 2 of 3
# GitHub Source https://github.com/yaronzz/Tidal-Media-Downloader/blob/fa6a9fbbf8f555a9611a05f7bf91855a4e047ea3/TIDALDL-GUI-CROSS/tidal_gui/view/taskView.py#L35#L35

def __initView__(self):
        grid = QGridLayout(self)
        grid.addLayout(self.__initLefTab__(), 0, 0, Qt.AlignLeft)
        grid.addWidget(self.__createContent__('Download'), 0, 1, Qt.AlignTop)
        grid.addWidget(self.__createContent__('Complete'), 0, 1, Qt.AlignTop)
        grid.addWidget(self.__createContent__('Error'), 0, 1, Qt.AlignTop)

# Example 3 of 3
# GitHub Source https://github.com/janbodnar/PyQt5-Tutorial-Examples/blob/10f0d8b1918623fe78205a04f6a827b9517aa816/events/event_object.py#L34#L34

def initUI(self):
        grid = QGridLayout()

        x = 0
        y = 0

        self.text = f'x: {x},  y: {y}'

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 450, 300)
        self.setWindowTitle('Event object')
        self.show()

# Examples for PyQt5.QtWidgets.QGridLayout.addWidget(arg1) [1.3%]

# Example 1 of 3
# GitHub Source https://github.com/carlosgprado/JARVIS/blob/29ffc6e92d2e251d1a29ded71f52d634482a2a57/IDAPlugin/jarvis/jarvis/widgets/OptionsWidget.py#L35#L35

def _createGui(self):
        """
        Grid layout containing groupBoxes
        """
        grid = QGridLayout()

        grid.addWidget(self.createBinaryOptions())
        grid.addWidget(self.createVulnOptions())

        self.setLayout(grid)

# Example 2 of 3
# GitHub Source https://github.com/cryoem/eman2/blob/30c0911a7b6f2df934968aadd9faf06224c20f0e/libpyEM/qtgui/empmwidgets.py#L327#L327

def __init__(self, name, header):
		PMBaseWidget.__init__(self, name)

		gridbox = QtWidgets.QGridLayout()
		self.header = QtWidgets.QLabel()
		font = QtGui.QFont()
		font.setBold(True)
		self.header.setFont(font)
		gridbox.addWidget(self.header)
		self.setLayout(gridbox)

		self.setValue(header)

# Example 3 of 3
# GitHub Source https://github.com/gridsync/gridsync/blob/b8095ed73967a475e549640dead4ea2665c6a2ce/gridsync/gui/history.py#L255#L255

def __init__(self, gateway, gui, deduplicate=True, max_items=30):
        super().__init__()
        layout = QGridLayout(self)
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(HistoryListWidget(gateway, deduplicate, max_items))
        self.status_panel = StatusPanel(gateway, gui)
        layout.addWidget(self.status_panel)

# Examples for PyQt5.QtWidgets.QGridLayout.addWidget(arg1,arg2,arg3,arg4,arg5,arg6) [0.6%]

# Example 1 of 3
# GitHub Source https://github.com/yaronzz/Tidal-Media-Downloader/blob/fa6a9fbbf8f555a9611a05f7bf91855a4e047ea3/TIDALDL-GUI-CROSS/tidal_gui/view/taskView.py#L53#L53

def __initLefTab__(self):
        self._listTab = ListWidget(ListWidgetStyle.TaskTab)
        self._listTab.setIconSize(QSize(20, 20))

        iconPath = getPackagePath() + "/resource/svg/taskTab/"
        self._listTab.addIConTextItem(iconPath + 'download.svg', 'Download')
        self._listTab.addIConTextItem(iconPath + 'complete.svg', 'Complete')
        self._listTab.addIConTextItem(iconPath + 'Error.svg', 'Error')

        self._listTab.itemClicked.connect(self.__tabItemChanged__)

        layout = QGridLayout()
        layout.addWidget(Label("TASK LIST", LabelStyle.PageTitle), 0, 0, Qt.AlignLeft)
        layout.addWidget(self._listTab, 1, 0, Qt.AlignLeft)
        layout.addWidget(Line('V'), 0, 1, 2, 1, Qt.AlignLeft)
        return layout

# Example 2 of 3
# GitHub Source https://github.com/circleguard/circleguard/blob/0d014d7632f9db423b9f3e3177bb920f936b934f/circleguard/widgets.py#L311#L311

def __init__(self, label_text, tooltip, setting):
        setting_options = setting + "_options"
        LinkableSetting.__init__(self, [setting, setting_options])
        QFrame.__init__(self)

        self.setting = setting

        label = QLabel(self)
        label.setText(label_text + ":")
        label.setToolTip(tooltip)

        combobox = ComboBox(self)
        combobox.setInsertPolicy(QComboBox.NoInsert)
        combobox.setMinimumWidth(120)
        setting_options_dict = self.setting_values[setting_options]
        for text, value in setting_options_dict.items():
            combobox.addItem(text, value)

        # select (in the combobx) the current setting value
        current_value = self.setting_values[setting]
        index = list(setting_options_dict.values()).index(current_value)
        combobox.setCurrentIndex(index)

        combobox.currentIndexChanged.connect(self.selection_changed)

        self.combobox = combobox

        layout = QGridLayout()
        layout.setContentsMargins(0, 0, 0, 0)
        layout.addWidget(label, 0, 0, 1, 1)
        layout.addItem(spacer(), 0, 1, 1, 1)
        layout.addWidget(combobox, 0, 2, 1, 3, Qt.AlignRight)
        self.setLayout(layout)

# Example 3 of 3
# GitHub Source https://github.com/electrumsv/electrumsv/blob/be9066fcf954c576fab33cbcfd881a203a073385/electrumsv/gui/qt/qrwindow.py#L49#L49

def __init__(self, win: QWidget) -> None:
        QWidget.__init__(self)
        self.setWindowTitle('ElectrumSV - ' + _('Payment Request'))
        self.label = ''
        self.amount = 0
        self.setFocusPolicy(Qt.NoFocus)

        layout = QGridLayout()

        self.qrw = QRCodeWidget()
        layout.addWidget(self.qrw, 0, 0, 1, 4, Qt.AlignHCenter)

        self._address_label = QLabel(_("Destination") +":")
        layout.addWidget(self._address_label, 1, 1, 1, 1, Qt.AlignRight)
        self._address_edit = QPlainTextEdit()
        self._address_edit.setReadOnly(True)
        self._address_edit.setMinimumWidth(300)
        layout.addWidget(self._address_edit, 1, 2, 1, 1, Qt.AlignLeft)

        self._message_label = QLabel(_("Message") +":")
        layout.addWidget(self._message_label, 2, 1, 1, 1, Qt.AlignRight)
        self._message_edit = QPlainTextEdit()
        self._message_edit.setReadOnly(True)
        self._message_edit.setMinimumWidth(300)
        layout.addWidget(self._message_edit, 2, 2, 1, 1, Qt.AlignLeft)

        self._amount_label = QLabel(_("Amount") +":")
        layout.addWidget(self._amount_label, 3, 1, 1, 1, Qt.AlignRight)
        self._amount_edit = QLineEdit()
        self._message_edit.setReadOnly(True)
        layout.addWidget(self._amount_edit, 3, 2, 1, 1, Qt.AlignLeft)

        self.setLayout(layout)

