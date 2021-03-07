# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 5.15.1
################################################################################

import asyncio
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from qasync import asyncClose
from functools import partial
from modules import globals, browsers


class F95Checker_GUI(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent, Qt.WindowFlags())

        self.setupUi()

    def setupUi(self):
        self.questions = {}
        if not self.objectName():
            self.setObjectName(u"F95Checker")
        self.main = QWidget(self)
        self.main.setObjectName(u"main")
        self.horizontalLayout = QHBoxLayout(self.main)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.games_section = QScrollArea(self.main)
        self.games_section.setObjectName(u"games_section")
        self.games_section.setFrameShape(QFrame.NoFrame)
        self.games_section.setWidgetResizable(True)
        self.games_section.verticalScrollBar().setSingleStep(10)
        self.games_list_container = QWidget()
        self.games_list_container.setObjectName(u"games_list_container")
        self.games_list_container.setEnabled(True)
        self.games_list_container.setGeometry(QRect(0, 0, 589, 43))
        self.game_list = {}
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.games_list_container.sizePolicy().hasHeightForWidth())
        self.games_list_container.setSizePolicy(sizePolicy)
        self.games_layout = QVBoxLayout(self.games_list_container)
        self.games_layout.setObjectName(u"verticalLayout")
        self.games_layout.setContentsMargins(6, 6, 0, 6)
        self.games_layout.setSpacing(0)
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)

        self.games_section.setWidget(self.games_list_container)

        self.verticalLayout.addWidget(self.games_section)

        self.add_section = QFrame(self.main)
        self.add_section.setObjectName(u"add_section")
        self.add_section.setFrameShape(QFrame.StyledPanel)
        self.add_section.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.add_section)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(3, 0, 3, 3)
        self.add_input = QLineEdit(self.add_section)
        self.add_input.setObjectName(u"add_input")

        self.horizontalLayout_2.addWidget(self.add_input)

        self.add_button = QPushButton(self.add_section)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setMinimumSize(QSize(88, 20))

        self.horizontalLayout_2.addWidget(self.add_button)

        self.verticalLayout.addWidget(self.add_section)

        self.horizontalLayout.addLayout(self.verticalLayout)

        # options
        self.options_section = QFrame(self.main)
        self.options_section.setObjectName(u"options_section")
        self.options_section.setMinimumSize(QSize(0, 0))
        self.options_section.setFrameShape(QFrame.NoFrame)
        self.options_section.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.options_section)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 4, 4, 4)

        self.refresh_button = QPushButton(self.options_section)
        self.refresh_button.setObjectName(u"refresh_button")
        self.refresh_button.setEnabled(True)
        self.refresh_button.setMinimumSize(QSize(0, 100))
        self.refresh_button.setBaseSize(QSize(0, 0))

        self.gridLayout_2.addWidget(self.refresh_button, 0, 0, 1, 3)

        self.refresh_bar = QProgressBar(self.options_section)
        self.refresh_bar.setObjectName(u"refresh_bar")
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.refresh_bar.sizePolicy().hasHeightForWidth())
        self.refresh_bar.setSizePolicy(sizePolicy2)
        self.refresh_bar.setTextVisible(False)
        self.refresh_bar.setMinimumSize(QSize(0, 100))
        self.refresh_bar.setVisible(False)

        self.gridLayout_2.addWidget(self.refresh_bar, 0, 0, 1, 3)

        self.refresh_label = QLabel(self.options_section)
        self.refresh_label.setObjectName(u"refresh_label")
        self.refresh_label.setAlignment(Qt.AlignCenter)
        self.refresh_label.setVisible(False)

        self.gridLayout_2.addWidget(self.refresh_label, 0, 0, 1, 3)

        self.browser_buttons = {}

        self.browser_buttons["chrome"] = QPushButton(self.options_section)
        self.browser_buttons["chrome"].setObjectName(u"browser_button")
        sizePolicy1.setHeightForWidth(self.browser_buttons["chrome"].sizePolicy().hasHeightForWidth())
        self.browser_buttons["chrome"].setSizePolicy(sizePolicy1)
        self.browser_buttons["chrome"].setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.browser_buttons["chrome"], 1, 0, 1, 1)

        self.browser_buttons["firefox"] = QPushButton(self.options_section)
        self.browser_buttons["firefox"].setObjectName(u"browser_button")
        sizePolicy1.setHeightForWidth(self.browser_buttons["firefox"].sizePolicy().hasHeightForWidth())
        self.browser_buttons["firefox"].setSizePolicy(sizePolicy1)
        self.browser_buttons["firefox"].setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.browser_buttons["firefox"], 1, 1, 1, 1)

        self.browser_buttons["brave"] = QPushButton(self.options_section)
        self.browser_buttons["brave"].setObjectName(u"browser_button")
        sizePolicy1.setHeightForWidth(self.browser_buttons["brave"].sizePolicy().hasHeightForWidth())
        self.browser_buttons["brave"].setSizePolicy(sizePolicy1)
        self.browser_buttons["brave"].setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.browser_buttons["brave"], 1, 2, 1, 1)

        self.browser_buttons["edge"] = QPushButton(self.options_section)
        self.browser_buttons["edge"].setObjectName(u"browser_button")
        sizePolicy1.setHeightForWidth(self.browser_buttons["edge"].sizePolicy().hasHeightForWidth())
        self.browser_buttons["edge"].setSizePolicy(sizePolicy1)
        self.browser_buttons["edge"].setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.browser_buttons["edge"], 2, 0, 1, 1)

        self.browser_buttons["opera"] = QPushButton(self.options_section)
        self.browser_buttons["opera"].setObjectName(u"browser_button")
        sizePolicy1.setHeightForWidth(self.browser_buttons["opera"].sizePolicy().hasHeightForWidth())
        self.browser_buttons["opera"].setSizePolicy(sizePolicy1)
        self.browser_buttons["opera"].setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.browser_buttons["opera"], 2, 1, 1, 1)

        self.browser_buttons["operagx"] = QPushButton(self.options_section)
        self.browser_buttons["operagx"].setObjectName(u"browser_button")
        sizePolicy1.setHeightForWidth(self.browser_buttons["operagx"].sizePolicy().hasHeightForWidth())
        self.browser_buttons["operagx"].setSizePolicy(sizePolicy1)
        self.browser_buttons["operagx"].setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.browser_buttons["operagx"], 2, 2, 1, 1)

        self.private_button = QCheckBox(self.options_section)
        self.private_button.setObjectName(u"private_button")
        self.private_button.setMinimumSize(QSize(128, 22))

        self.gridLayout_2.addWidget(self.private_button, 3, 0, 1, 3, Qt.AlignHCenter)

        self.saved_html_button = QCheckBox(self.options_section)
        self.saved_html_button.setObjectName(u"saved_html_button")
        self.saved_html_button.setMinimumSize(QSize(128, 22))

        self.gridLayout_2.addWidget(self.saved_html_button, 4, 0, 1, 3, Qt.AlignHCenter)

        self.start_refresh_button = QCheckBox(self.options_section)
        self.start_refresh_button.setObjectName(u"start_refresh_button")
        self.start_refresh_button.setMinimumSize(QSize(128, 22))

        self.gridLayout_2.addWidget(self.start_refresh_button, 5, 0, 1, 3, Qt.AlignHCenter)

        self.sort_label = QLabel(self.options_section)
        self.sort_label.setObjectName(u"sort_label")

        self.gridLayout_2.addWidget(self.sort_label, 7, 0, 1, 1)

        self.sort_input = QComboBox(self.options_section)
        self.sort_input.addItem("")
        self.sort_input.addItem("")
        self.sort_input.addItem("")
        self.sort_input.addItem("")
        self.sort_input.setObjectName(u"sort_input")
        self.sort_input.setMinimumSize(QSize(128, 26))

        self.gridLayout_2.addWidget(self.sort_input, 7, 1, 1, 2)

        self.retries_label = QLabel(self.options_section)
        self.retries_label.setObjectName(u"retries_label")

        self.gridLayout_2.addWidget(self.retries_label, 8, 0, 1, 2)

        self.retries_input = QSpinBox(self.options_section)
        self.retries_input.setObjectName(u"retries_input")
        self.retries_input.setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.retries_input, 8, 2, 1, 1)

        self.color_label = QLabel(self.options_section)
        self.color_label.setObjectName(u"color_label")

        self.gridLayout_2.addWidget(self.color_label, 10, 0, 1, 2)

        self.color_button = QPushButton(self.options_section)
        self.color_button.setObjectName(u"color_button")
        sizePolicy1.setHeightForWidth(self.color_button.sizePolicy().hasHeightForWidth())
        self.color_button.setSizePolicy(sizePolicy1)
        self.color_button.setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.color_button, 10, 2, 1, 1)

        self.edit_label = QLabel(self.options_section)
        self.edit_label.setObjectName(u"edit_label")

        self.gridLayout_2.addWidget(self.edit_label, 11, 0, 1, 2)

        self.edit_button = QPushButton(self.options_section)
        self.edit_button.setObjectName(u"edit_button")
        sizePolicy1.setHeightForWidth(self.edit_button.sizePolicy().hasHeightForWidth())
        self.edit_button.setSizePolicy(sizePolicy1)
        self.edit_button.setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.edit_button, 11, 2, 1, 1)

        self.bg_refresh_label = QLabel(self.options_section)
        self.bg_refresh_label.setObjectName(u"bg_refresh_label")

        self.gridLayout_2.addWidget(self.bg_refresh_label, 12, 0, 1, 2)

        self.bg_refresh_input = QSpinBox(self.options_section)
        self.bg_refresh_input.setObjectName(u"bg_refresh_input")
        self.bg_refresh_input.setMinimumSize(QSize(64, 26))
        self.bg_refresh_input.setMinimum(5)
        self.bg_refresh_input.setMaximum(999)

        self.gridLayout_2.addWidget(self.bg_refresh_input, 12, 2, 1, 1)

        self.background_label = QLabel(self.options_section)
        self.background_label.setObjectName(u"background_label")

        self.gridLayout_2.addWidget(self.background_label, 13, 0, 1, 2)

        self.background_button = QPushButton(self.options_section)
        self.background_button.setObjectName(u"background_button")
        sizePolicy1.setHeightForWidth(self.background_button.sizePolicy().hasHeightForWidth())
        self.background_button.setSizePolicy(sizePolicy1)
        self.background_button.setMinimumSize(QSize(64, 26))

        self.gridLayout_2.addWidget(self.background_button, 13, 2, 1, 1)

        self.watermark = QLabel(self.options_section)
        self.watermark.setObjectName(u"watermark")
        self.watermark.setAlignment(Qt.AlignBottom | Qt.AlignRight | Qt.AlignTrailing)

        self.gridLayout_2.addWidget(self.watermark, 15, 0, 1, 3)

        self.sidebar_spacer = QSpacerItem(0, 0, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout_2.addItem(self.sidebar_spacer, 14, 0, 1, 3)

        self.horizontalLayout.addWidget(self.options_section)

        self.setCentralWidget(self.main)

        QMetaObject().connectSlotsByName(self)
    # setupUi

        self.setWindowTitle(QCoreApplication.translate("F95Checker", u"F95Checker", None))
        self.add_button.setText(QCoreApplication.translate("F95Checker", u"Add", None))
        self.refresh_button.setText(QCoreApplication.translate("F95Checker", u"Refresh!", None))
        self.refresh_label.setText(QCoreApplication.translate("F95Checker", u"Refresh!", None))
        self.browser_buttons["chrome"].setText(QCoreApplication.translate("F95Checker", u"Chrome", None))
        self.browser_buttons["firefox"].setText(QCoreApplication.translate("F95Checker", u"Firefox", None))
        self.browser_buttons["brave"].setText(QCoreApplication.translate("F95Checker", u"Brave", None))
        self.browser_buttons["edge"].setText(QCoreApplication.translate("F95Checker", u"Edge", None))
        self.browser_buttons["opera"].setText(QCoreApplication.translate("F95Checker", u"Opera", None))
        self.browser_buttons["operagx"].setText(QCoreApplication.translate("F95Checker", u"OperaGX", None))
        self.private_button.setText(QCoreApplication.translate("F95Checker", u"Open Browser  in  Private Mode", None))
        self.start_refresh_button.setText(QCoreApplication.translate("F95Checker", u"Refresh  List  at  Program  Start", None))
        self.saved_html_button.setText(QCoreApplication.translate("F95Checker", u"Open  Pages   as   Saved  HTML", None))
        self.sort_label.setText(QCoreApplication.translate("F95Checker", u"   Auto Sort:", None))
        self.sort_input.setItemText(0, QCoreApplication.translate("F95Checker", u"Don't Sort", None))
        self.sort_input.setItemText(1, QCoreApplication.translate("F95Checker", u"Last Updated", None))
        self.sort_input.setItemText(2, QCoreApplication.translate("F95Checker", u"First Added", None))
        self.sort_input.setItemText(3, QCoreApplication.translate("F95Checker", u"Alphabetical", None))
        self.retries_label.setText(QCoreApplication.translate("F95Checker", u"   Max Retries per Request:", None))
        self.color_label.setText(QCoreApplication.translate("F95Checker", u"   Change  GUI  Colors:", None))
        self.color_button.setText(QCoreApplication.translate("F95Checker", u"Picker", None))
        self.edit_label.setText(QCoreApplication.translate("F95Checker", u"   Remove   Games:", None))
        self.edit_button.setText(QCoreApplication.translate("F95Checker", u"Edit", None))
        self.bg_refresh_label.setText(QCoreApplication.translate("F95Checker", u"   BG Refresh Delay (mins):", None))
        self.background_label.setText(QCoreApplication.translate("F95Checker", u"   Switch  to  Background:", None))
        self.background_button.setText(QCoreApplication.translate("F95Checker", u"Switch", None))
        self.refresh_button.setToolTip('Click this to check\nfor game updates!')
        for browser in self.browser_buttons:
            self.browser_buttons[browser].setToolTip('Click this to select the\nbrowser to use to open links!')
        self.private_button.setToolTip('This toggles whether links should be\nopened in incognito / private mode!')
        self.saved_html_button.setToolTip('This toggles whether links should be opened as a local HTML,\nallowing you to see links and spoilers without logging in!')
        self.start_refresh_button.setToolTip('This toggles whether the tool should\nrefresh automatically when you open it!')
        self.sort_input.setToolTip('This changes how\ngames get sorted!')
        self.sort_label.setToolTip('This changes how\ngames get sorted!')
        self.retries_input.setToolTip('This changes how many times a\nfailed request will be retried!')
        self.retries_label.setToolTip('This changes how many times a\nfailed request will be retried!')
        self.color_button.setToolTip('Here you can change\nhow the tool looks!')
        self.color_label.setToolTip('Here you can change\nhow the tool looks!')
        self.edit_button.setToolTip('With this you can remove\ngames from the list!')
        self.edit_label.setToolTip('With this you can remove\ngames from the list!')
        self.bg_refresh_input.setToolTip('This changes how often (in minutes)\nthe list refreshes in background mode!')
        self.bg_refresh_label.setToolTip('This changes how often (in minutes)\nthe list refreshes in background mode!')
        self.background_button.setToolTip('With this you can turn\non background mode!')
        self.background_label.setToolTip('With this you can turn\non background mode!')
        self.watermark.setToolTip('You can click this to view the thread\non F95Zone! Go and rate my tool :D')
        self.add_input.setToolTip('Here you can paste a link to a F95Zone\nthread to add that game to the list!')
        self.add_button.setToolTip('Click this to add the game\nyou pasted on the left!')

    @asyncClose
    async def closeEvent(self, event):
        try:
            await globals.http.close()
        except:
            pass

    def get_stylesheet(self, style):
        if ((int(style['back'][1:2], 16) * 299) + (int(style['back'][3:5], 16) * 587) + (int(style['back'][5:7], 16) * 114)) / 1000 >= 100:
            font = '#181818'
            font_disabled = '#8A8B8C'
            check = 'check-light'
            arrow_normal = 'arrow-light'
            arrow_active = 'arrow-dark'
        else:
            font = '#CDCECF'
            font_disabled = '#8A8B8C'
            check = 'check-dark'
            arrow_normal = 'arrow-dark'
            arrow_active = 'arrow-light'
        if ((int(style['alt'][1:2], 16) * 299) + (int(style['alt'][3:5], 16) * 587) + (int(style['alt'][5:7], 16) * 114)) / 1000 >= 100:
            font_alt = '#181818'
        else:
            font_alt = '#CDCECF'
        qss = """
QWidget {
    background: """+style['back']+""";
    color: """+font+"""
}

QLabel#highlighted {
    color: """+style['accent']+"""
}

QLabel#refresh_label {
    background: transparent
}

QLabel#status_completed {
    color: #00D800
}

QLabel#status_onhold {
    color: #0180F1
}

QLabel#status_abandoned {
    color: #DD3333
}

QFrame#game_container_frame_alt, QFrame#game_container_frame_alt QPushButton, QFrame#game_container_frame_alt QLabel#name, QFrame#game_container_frame_alt QLabel#version, QFrame#game_container_frame_alt QLabel#status, QFrame#game_container_frame_alt QCheckBox, QFrame#game_container_frame_alt QCheckBox::indicator:unchecked {
    background: """+style['alt']+""";
    color: """+font_alt+"""
}

QFrame#game_container_frame_alt QLabel#highlighted {
    background: """+style['alt']+""";
    color: """+style['accent']+"""
}

QPushButton {
    background: transparent;
    border: 1px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px;
    padding-top: 2px;
    padding-bottom: 2px;
    padding-right: 4px;
    padding-left: 4px;
}

QPushButton:disabled {
    border-color: """+style['disabled']+""";
    color: """+font_disabled+"""
}

QFrame#game_container_frame_alt QPushButton:disabled {
    border-color: """+style['disabled']+""";
    color: """+font_disabled+"""
}

QPushButton:hover {
    border-color: """+style['hover']+"""
}

QPushButton:pressed {
    border: 2px solid """+style['accent']+"""
}

QPushButton#browser_button_selected {
    border: 2px solid """+style['accent']+"""
}

QPushButton#browser_button_selected:disabled {
    border-color: """+style['disabled']+""";
    color: """+font_disabled+"""
}

QPushButton#browser_button_selected:hover {
    border: 2px solid """+style['accent']+"""
}

QPushButton#browser_button_selected:pressed {
    border: 2px solid """+style['accent']+"""
}

QSpinBox {
    background: """+style['back']+""";
    border: 1px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px;
    padding-left: 6px;
    selection-color: """+style['accent']+""";
    selection-background-color: rgba(0, 0, 0, 30%)
}

QSpinBox:hover {
    border-color: """+style['hover']+"""
}

QSpinBox::up-button {
    background: """+style['accent']+""";
    border: 1px solid """+style['back']+""";
    border-radius: """+str(style['radius'])+"""px;
    image: url(resources/icons/up-"""+arrow_normal+""".png);
    width: 15px
}

QSpinBox::up-button:pressed {
    image: url(resources/icons/up-"""+arrow_active+""".png)
}

QSpinBox::down-button {
    background: """+style['accent']+""";
    border: 1px solid """+style['back']+""";
    border-radius: """+str(style['radius'])+"""px;
    image: url(resources/icons/down-"""+arrow_normal+""".png);
    width: 15px
}

QSpinBox::down-button:pressed {
    image: url(resources/icons/down-"""+arrow_active+""".png)
}

QCheckBox::indicator {
    border: 2px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px;
    background: """+style['back']+""";
    width: 16px;
    height: 16px
}

QCheckBox::indicator:checked {
    border-color: """+style['accent']+""";
    background: """+style['accent']+""";
    image: url(resources/icons/"""+check+""".png)
}

QCheckBox::indicator:unchecked:hover {
    border-color: """+style['hover']+"""
}

QCheckBox:disabled {
    color: """+font_disabled+"""
}

QCheckBox::indicator:disabled {
    border-color: """+style['disabled']+"""
}

QComboBox {
    background: transparent;
    border: 1px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px;
    padding-left: 10px
}

QComboBox:hover {
    border-color: """+style['hover']+"""
}

QComboBox::drop-down {
    background: """+style['accent']+""";
    border: 2px solid """+style['back']+""";
    border-radius: """+str(style['radius'])+"""px;
    image: url(resources/icons/down-"""+arrow_normal+""".png);
    width: 13px
}

QComboBox::drop-down:pressed {
    image: url(resources/icons/down-"""+arrow_active+""".png)
}

QComboBox QAbstractItemView {
    border: 1px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px;
    selection-background-color: """+style['accent']+"""
}

QScrollBar:horizontal {
    background: transparent;
    height: 16px;
    padding: 2px;
}

QScrollBar::handle:horizontal {
    background: """+style['border']+""";
    border: 0px solid """+style['back']+""";
    border-radius: 3px;
    margin: 3px
}

QScrollBar::handle:horizontal:hover {
    background: """+style['hover']+"""
}

QScrollBar::handle:horizontal:pressed {
    background: """+style['accent']+"""
}

QScrollBar::add-line:horizontal {
    width: 0px
}

QScrollBar::sub-line:horizontal {
    width: 0px
}

QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {
    background: transparent;
}

QScrollBar:vertical {
    background: transparent;
    width: 16px;
    padding: 2px;
}

QScrollBar::handle:vertical {
    background: """+style['border']+""";
    border: 0px solid """+style['back']+""";
    border-radius: 3px;
    margin: 3px
}

QScrollBar::handle:vertical:hover {
    background: """+style['hover']+"""
}

QScrollBar::handle:vertical:pressed {
    background: """+style['accent']+"""
}

QScrollBar::add-line:vertical {
    height: 0px
}

QScrollBar::sub-line:vertical {
    height: 0px
}

QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {
    background: transparent;
}

QLineEdit {
    border: 1px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px;
    min-height: 18px
}

QLineEdit:disabled {
    border-color: """+style['disabled']+""";
    color: """+font_disabled+"""
}

QLineEdit:hover {
    border-color: """+style['hover']+"""
}

QLineEdit:focus {
    border: 1px solid """+style['accent']+"""
}

QPushButton#back_color_selection {
    background: """+style['back']+""";
    border: 1px solid grey
}

QPushButton#back_color_selection:hover {
    background: """+style['back']+""";
    border: 1px solid grey
}

QPushButton#back_color_selection:pressed {
    background: """+style['back']+""";
    border: 1px solid grey
}

QPushButton#alt_color_selection {
    background: """+style['alt']+""";
    border: 1px solid grey
}

QPushButton#alt_color_selection:hover {
    background: """+style['alt']+""";
    border: 1px solid grey
}

QPushButton#alt_color_selection:pressed {
    background: """+style['alt']+""";
    border: 1px solid grey
}

QPushButton#accent_color_selection {
    background: """+style['accent']+""";
    border: 1px solid grey
}

QPushButton#accent_color_selection:hover {
    background: """+style['accent']+""";
    border: 1px solid grey
}

QPushButton#accent_color_selection:pressed {
    background: """+style['accent']+""";
    border: 1px solid grey
}

QPushButton#border_color_selection {
    background: """+style['border']+""";
    border: 1px solid grey
}

QPushButton#border_color_selection:hover {
    background: """+style['border']+""";
    border: 1px solid grey
}

QPushButton#border_color_selection:pressed {
    background: """+style['border']+""";
    border: 1px solid grey
}

QPushButton#hover_color_selection {
    background: """+style['hover']+""";
    border: 1px solid grey
}

QPushButton#hover_color_selection:hover {
    background: """+style['hover']+""";
    border: 1px solid grey
}

QPushButton#hover_color_selection:pressed {
    background: """+style['hover']+""";
    border: 1px solid grey
}

QPushButton#disabled_color_selection {
    background: """+style['disabled']+""";
    border: 1px solid grey
}

QPushButton#disabled_color_selection:hover {
    background: """+style['disabled']+""";
    border: 1px solid grey
}

QPushButton#disabled_color_selection:pressed {
    background: """+style['disabled']+""";
    border: 1px solid grey
}

QSpinBox#radius_selection::up-button, QSpinBox#radius_selection::down-button {
    border-radius: """+("4" if style["radius"] > 4 else str(style['radius']))+"""px
}

QProgressBar {
    background: """+style['back']+""";
    border: 1px solid """+style['border']+""";
    border-radius: """+str(style['radius'])+"""px
}

QProgressBar::chunk {
    background-color: """+style['accent']+"""
}
"""
        return qss


# Game section frame object
class GameContainer(QFrame):
    def __init__(self, alt):
        super().__init__(globals.gui.games_list_container)
        self.setObjectName(u"game_container_frame" + u"_alt" if alt else u"")
        self.setFrameShape(QFrame.StyledPanel)
        self.setFrameShadow(QFrame.Raised)
        self.game_container = QHBoxLayout(self)
        self.game_container.setObjectName(u"game_container" + u"_alt" if alt else u"")
        self.game_container.setContentsMargins(7, 4, 3, 4)

        self.remove_button = QPushButton(self)
        self.remove_button.setObjectName(u"remove_button")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.remove_button.sizePolicy().hasHeightForWidth())
        self.remove_button.setSizePolicy(sizePolicy1)
        self.remove_button.setMinimumSize(QSize(26, 26))

        self.name = QLabel(self)
        self.name.setObjectName(u"name")
        sizePolicy2 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy2)

        self.status = QLabel(self)
        self.status.setObjectName(u"status")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.status.sizePolicy().hasHeightForWidth())
        self.status.setSizePolicy(sizePolicy3)

        self.version = QLabel(self)
        self.version.setObjectName(u"version")
        sizePolicy3 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.version.sizePolicy().hasHeightForWidth())
        self.version.setSizePolicy(sizePolicy3)

        self.played_button = QCheckBox(self)
        self.played_button.setObjectName(u"played_button")
        sizePolicy1.setHeightForWidth(self.played_button.sizePolicy().hasHeightForWidth())
        self.played_button.setSizePolicy(sizePolicy1)

        self.installed_button = QCheckBox(self)
        self.installed_button.setObjectName(u"installed_button")
        sizePolicy1.setHeightForWidth(self.installed_button.sizePolicy().hasHeightForWidth())
        self.installed_button.setSizePolicy(sizePolicy1)

        self.open_button = QPushButton(self)
        self.open_button.setObjectName(u"open_button")
        sizePolicy1.setHeightForWidth(self.open_button.sizePolicy().hasHeightForWidth())
        self.open_button.setSizePolicy(sizePolicy1)
        self.open_button.setMinimumSize(QSize(26, 26))

        self.view_button = QPushButton(self)
        self.view_button.setObjectName(u"view_button")
        sizePolicy1.setHeightForWidth(self.view_button.sizePolicy().hasHeightForWidth())
        self.view_button.setSizePolicy(sizePolicy1)
        self.view_button.setMinimumSize(QSize(26, 26))

        self.game_container.addWidget(self.open_button)
        self.game_container.addWidget(self.name)
        self.game_container.addWidget(self.status)
        self.game_container.addWidget(self.version)
        self.game_container.addWidget(self.played_button)
        self.game_container.addWidget(self.installed_button)
        self.game_container.addWidget(self.view_button)
        self.game_container.addWidget(self.remove_button)

        self.remove_button.setText(QCoreApplication.translate("F95Checker", u"", None))
        self.remove_button.setFont(globals.font_awesome)
        self.remove_button.setVisible(False)
        self.status.setFont(globals.font_awesome)
        self.played_button.setText(QCoreApplication.translate("F95Checker", u"  ", None))
        self.played_button.setFont(globals.font_awesome)
        self.installed_button.setText(QCoreApplication.translate("F95Checker", u"  ", None))
        self.installed_button.setFont(globals.font_awesome)
        self.open_button.setText(QCoreApplication.translate("F95Checker", u"", None))
        self.open_button.setFont(globals.font_awesome)
        self.view_button.setText(QCoreApplication.translate("F95Checker", u"", None))
        self.view_button.setFont(globals.font_awesome)
        self.name.setToolTip('Click on the name to see\nthe game\'s changelog!')
        self.open_button.setToolTip('Click this to play the game!')
        self.version.setToolTip('This is the game\'s version!')
        self.played_button.setToolTip('This checkbox indicates whether\nyou fully played this update')
        self.installed_button.setToolTip('This checkbox indicates whether\nyou installed this update')
        self.view_button.setToolTip('Click this to open the game\'s\nwebpage in your browser!')
        self.remove_button.setToolTip('Click this to remove this game from your list!')

    def update_details(self, name: str = None, version: str = None, status: str = None, highlight: bool = None, installed: bool = None, played: bool = None, alt: bool = None, link: str = None):
        if alt is not None:
            self.setObjectName(u"game_container_frame" + u"_alt" if alt else u"")
            self.game_container.setObjectName(u"game_container" + u"_alt" if alt else u"")
            # Refresh style
            self.setStyleSheet("/* /")
        if name is not None:
            self.name.setText(name)
        if version is not None:
            self.version.setText(version + "    ")
            if version == "N/A":
                self.version.setToolTip('This game does not have a properly formatted\ntitle,identifying the version was not possible!')
            else:
                self.version.setToolTip('This is the game\'s version!')
        if status is not None:
            if status == 'completed':
                text = ""
                self.status.setToolTip("Status: Completed!")
                self.status.setObjectName(u"status_completed")
            elif status == 'onhold':
                text = ""
                self.status.setToolTip("Status: On Hold...")
                self.status.setObjectName(u"status_onhold")
            elif status == 'abandoned':
                text = ""
                self.status.setToolTip("Status: Abandoned D:")
                self.status.setObjectName(u"status_abandoned")
            else:
                text = ""
                self.status.setToolTip("")
                self.status.setObjectName(u"status")
            self.status.setText(text)
        if highlight is not None:
            if not highlight:
                self.name.setObjectName(u"name")
            else:
                self.name.setObjectName(u"highlighted")
            # Refresh style
            self.name.setStyleSheet("/* /")
        if installed is not None:
            self.installed_button.setChecked(installed)
        if played is not None:
            self.played_button.setChecked(played)
        if link is not None:
            try:
                self.view_button.clicked.disconnect()
            except TypeError:
                pass
            self.view_button.clicked.connect(partial(browsers.open_webpage_async_helper, link))


class StyleGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"StyleGUI")
        self.resize(280, 150)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setObjectName(u"gridLayout")
        self.alternate = QPushButton(self)
        self.alternate.setObjectName(u"alt_color_selection")
        self.alternate.setFixedSize(QSize(18, 18))

        self.gridLayout.addWidget(self.alternate, 1, 2, 1, 1)

        self.accent_label = QLabel(self)
        self.accent_label.setObjectName(u"accent_label")

        self.gridLayout.addWidget(self.accent_label, 2, 0, 1, 1)

        self.accent = QPushButton(self)
        self.accent.setObjectName(u"accent_color_selection")
        self.accent.setFixedSize(QSize(18, 18))

        self.gridLayout.addWidget(self.accent, 2, 2, 1, 1)

        self.background = QPushButton(self)
        self.background.setObjectName(u"back_color_selection")
        self.background.setFixedSize(QSize(18, 18))

        self.gridLayout.addWidget(self.background, 0, 2, 1, 1)

        self.restore = QPushButton(self)
        self.restore.setObjectName(u"restore")
        self.restore.setFixedSize(QSize(106, 18))

        self.gridLayout.addWidget(self.restore, 3, 0, 1, 3)

        self.horizontalSpacer = QSpacerItem(10, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer, 0, 1, 3, 1)

        self.background_label = QLabel(self)
        self.background_label.setObjectName(u"background_label")

        self.gridLayout.addWidget(self.background_label, 0, 0, 1, 1)

        self.radius_label = QLabel(self)
        self.radius_label.setObjectName(u"radius_label")

        self.gridLayout.addWidget(self.radius_label, 3, 4, 1, 1)

        self.border = QPushButton(self)
        self.border.setObjectName(u"border_color_selection")
        self.border.setFixedSize(QSize(18, 18))

        self.gridLayout.addWidget(self.border, 0, 6, 1, 1)

        self.radius = QSpinBox(self)
        self.radius.setObjectName(u"radius_selection")
        self.radius.setMaximum(6)

        self.gridLayout.addWidget(self.radius, 3, 5, 1, 2)

        self.hover = QPushButton(self)
        self.hover.setObjectName(u"hover_color_selection")
        self.hover.setFixedSize(QSize(18, 18))

        self.gridLayout.addWidget(self.hover, 1, 6, 1, 1)

        self.disabled = QPushButton(self)
        self.disabled.setObjectName(u"disabled_color_selection")
        self.disabled.setFixedSize(QSize(18, 18))

        self.gridLayout.addWidget(self.disabled, 2, 6, 1, 1)

        self.disabled_label = QLabel(self)
        self.disabled_label.setObjectName(u"disabled_label")

        self.gridLayout.addWidget(self.disabled_label, 2, 4, 1, 1)

        self.alternate_label = QLabel(self)
        self.alternate_label.setObjectName(u"alternate_label")

        self.gridLayout.addWidget(self.alternate_label, 1, 0, 1, 1)

        self.border_label = QLabel(self)
        self.border_label.setObjectName(u"border_label")

        self.gridLayout.addWidget(self.border_label, 0, 4, 1, 1)

        self.hover_label = QLabel(self)
        self.hover_label.setObjectName(u"hover_label")

        self.gridLayout.addWidget(self.hover_label, 1, 4, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(16, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_2, 0, 5, 4, 1)

        self.horizontalSpacer_3 = QSpacerItem(20, 0, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_3, 0, 3, 4, 1)

        QMetaObject.connectSlotsByName(self)
    # setupUi

        self.setWindowTitle(QCoreApplication.translate("StyleGUI", u"F95Checker Styler", None))
        self.alternate.setText("")
        self.accent_label.setText(QCoreApplication.translate("StyleGUI", u"Accent", None))
        self.accent.setText("")
        self.background.setText("")
        self.restore.setText(QCoreApplication.translate("StyleGUI", u"Restore to Defaults", None))
        self.background_label.setText(QCoreApplication.translate("StyleGUI", u"Background", None))
        self.radius_label.setText(QCoreApplication.translate("StyleGUI", u"Corner Radius", None))
        self.border.setText("")
        self.hover.setText("")
        self.disabled.setText("")
        self.disabled_label.setText(QCoreApplication.translate("StyleGUI", u"Buttons Disabled", None))
        self.alternate_label.setText(QCoreApplication.translate("StyleGUI", u"Alternate BG", None))
        self.border_label.setText(QCoreApplication.translate("StyleGUI", u"Buttons Border", None))
        self.hover_label.setText(QCoreApplication.translate("StyleGUI", u"Buttons Hover", None))


class ChangelogGUI(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        self.setupUi()

    def setupUi(self):
        if not self.objectName():
            self.setObjectName(u"Form")
        self.resize(600, 690)
        self.gridLayout = QGridLayout(self)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.scrollArea = QScrollArea(self)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setFrameShape(QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 799, 770))
        self.gridLayout_2 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(9, 9, 9, 9)
        self.text = QPlainTextEdit(self.scrollAreaWidgetContents_2)
        self.text.setObjectName(u"plainTextEdit")
        self.text.setFrameShape(QFrame.NoFrame)
        self.text.setReadOnly(True)

        self.gridLayout_2.addWidget(self.text, 0, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 0, 0, 1, 1)

        QMetaObject.connectSlotsByName(self)


class LoginUI(QDialog):
    def __init__(self, parent):
        self.alive = True
        super().__init__(parent)
        self.setupUi(self)

    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.setSizeGripEnabled(False)
        Dialog.setModal(True)
        self.gridLayout = QGridLayout(Dialog)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setContentsMargins(14, 12, 14, 12)
        self.label_3 = QLabel(Dialog)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 2)

        self.lineEdit = QLineEdit(Dialog)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout.addWidget(self.lineEdit, 1, 1, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 1, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(Dialog)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEchoMode(QLineEdit.Password)

        self.gridLayout.addWidget(self.lineEdit_2, 2, 1, 1, 1)

        self.buttonBox = QDialogButtonBox(Dialog)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setOrientation(Qt.Horizontal)
        self.buttonBox.setStandardButtons(QDialogButtonBox.Save)
        self.buttonBox.accepted.connect(self.closeEvent)

        self.gridLayout.addWidget(self.buttonBox, 3, 0, 1, 2)

        self.label_2 = QLabel(Dialog)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 2, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"Please enter your F95Zone login credentials to continue...", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Username", None))
        self.lineEdit_2.setText("")
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Password", None))
    # retranslateUi

    @asyncClose
    async def closeEvent(self, event=None):
        self.alive = False
        self.accept()


class QuestionPopup(QMessageBox):
    def __init__(self, parent, title, message, extra_message=None, details=None):
        self.alive = True
        super().__init__(parent)
        self.setWindowIcon(QIcon('resources/icons/icon.ico' if globals.user_os == "windows" else 'resoures/icons/icon.png'))
        self.setWindowTitle(title)
        self.setIcon(QMessageBox.Question)
        self.setText(message)
        if extra_message:
            self.setInformativeText(extra_message)
        if details:
            self.setDetailedText(details)
        self.setStandardButtons(QMessageBox.Yes | QMessageBox.No)
        self.finished.connect(self.closeEvent)

    @asyncClose
    async def closeEvent(self, event=None):
        self.alive = False
        if event == 16384:
            self.result = True
        elif event == 65536:
            self.result = False
        else:
            self.result = None

    @staticmethod
    async def ask(parent, title, message, extra_message=None, details=None):
        msg = QuestionPopup(parent, title, message, extra_message, details)
        msg.show()
        while msg.alive:
            await asyncio.sleep(0.25)
        return msg.result


class WarningPopup(QMessageBox):
    def __init__(self, parent, title, message):
        self.alive = True
        super().__init__(parent)
        self.setWindowIcon(QIcon('resources/icons/icon.ico' if globals.user_os == "windows" else 'resoures/icons/icon.png'))
        self.setWindowTitle(title)
        self.setIcon(QMessageBox.Warning)
        self.setText(message)
        self.setStandardButtons(QMessageBox.Ok)
        self.finished.connect(self.closeEvent)

    @asyncClose
    async def closeEvent(self, event=None):
        self.alive = False

    @staticmethod
    async def open(parent, title, message):
        msg = WarningPopup(parent, title, message)
        msg.show()
        while msg.alive:
            await asyncio.sleep(0.25)
        return True


class InfoPopup(QMessageBox):
    def __init__(self, parent, title, message):
        self.alive = True
        super().__init__(parent)
        self.setWindowIcon(QIcon('resources/icons/icon.ico' if globals.user_os == "windows" else 'resoures/icons/icon.png'))
        self.setWindowTitle(title)
        self.setIcon(QMessageBox.Information)
        self.setText(message)
        self.setStandardButtons(QMessageBox.Ok)
        self.finished.connect(self.closeEvent)

    @asyncClose
    async def closeEvent(self, event=None):
        self.alive = False

    @staticmethod
    async def open(parent, title, message):
        msg = InfoPopup(parent, title, message)
        msg.show()
        while msg.alive:
            await asyncio.sleep(0.25)
        return True