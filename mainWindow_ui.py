# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindow_ui.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(402, 436)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_5.addWidget(self.label)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_5)

        self.btnInput = QPushButton(self.centralwidget)
        self.btnInput.setObjectName(u"btnInput")

        self.horizontalLayout_5.addWidget(self.btnInput)


        self.verticalLayout.addLayout(self.horizontalLayout_5)

        self.lblInput = QLabel(self.centralwidget)
        self.lblInput.setObjectName(u"lblInput")
        self.lblInput.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblInput)

        self.line = QFrame(self.centralwidget)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_6.addWidget(self.label_3)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_6)

        self.btnOutput = QPushButton(self.centralwidget)
        self.btnOutput.setObjectName(u"btnOutput")

        self.horizontalLayout_6.addWidget(self.btnOutput)


        self.verticalLayout.addLayout(self.horizontalLayout_6)

        self.lblOutput = QLabel(self.centralwidget)
        self.lblOutput.setObjectName(u"lblOutput")
        self.lblOutput.setWordWrap(True)

        self.verticalLayout.addWidget(self.lblOutput)

        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.HLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.rbInch = QRadioButton(self.centralwidget)
        self.rbInch.setObjectName(u"rbInch")
        self.rbInch.setChecked(True)

        self.horizontalLayout.addWidget(self.rbInch)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")

        self.horizontalLayout.addWidget(self.label_5)

        self.txtXBacklash = QLineEdit(self.centralwidget)
        self.txtXBacklash.setObjectName(u"txtXBacklash")
        self.txtXBacklash.setMinimumSize(QSize(100, 0))

        self.horizontalLayout.addWidget(self.txtXBacklash)

        self.horizontalLayout.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.rbMetric = QRadioButton(self.centralwidget)
        self.rbMetric.setObjectName(u"rbMetric")

        self.horizontalLayout_2.addWidget(self.rbMetric)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_2)

        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout_2.addWidget(self.label_6)

        self.txtYBacklash = QLineEdit(self.centralwidget)
        self.txtYBacklash.setObjectName(u"txtYBacklash")
        self.txtYBacklash.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.txtYBacklash)

        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout_3.addWidget(self.label_7)

        self.txtZBacklash = QLineEdit(self.centralwidget)
        self.txtZBacklash.setObjectName(u"txtZBacklash")
        self.txtZBacklash.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_3.addWidget(self.txtZBacklash)

        self.horizontalLayout_3.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_4)

        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_4.addWidget(self.label_8)

        self.txtTolerance = QLineEdit(self.centralwidget)
        self.txtTolerance.setObjectName(u"txtTolerance")
        self.txtTolerance.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_4.addWidget(self.txtTolerance)

        self.horizontalLayout_4.setStretch(0, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.btnRun = QPushButton(self.centralwidget)
        self.btnRun.setObjectName(u"btnRun")

        self.verticalLayout.addWidget(self.btnRun)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 402, 23))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"GCode Backlash Compensation", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Input File", None))
        self.btnInput.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.lblInput.setText(QCoreApplication.translate("MainWindow", u"<No File Selected>", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Output File:", None))
        self.btnOutput.setText(QCoreApplication.translate("MainWindow", u"Select File", None))
        self.lblOutput.setText(QCoreApplication.translate("MainWindow", u"<No File Selected>", None))
        self.rbInch.setText(QCoreApplication.translate("MainWindow", u"Inch", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"X Backlash:", None))
        self.txtXBacklash.setText(QCoreApplication.translate("MainWindow", u"0.005", None))
        self.rbMetric.setText(QCoreApplication.translate("MainWindow", u"Metric", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Y Backlash:", None))
        self.txtYBacklash.setText(QCoreApplication.translate("MainWindow", u"0.005", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Z Backlash:", None))
        self.txtZBacklash.setText(QCoreApplication.translate("MainWindow", u"0.005", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Tolerance:", None))
        self.txtTolerance.setText(QCoreApplication.translate("MainWindow", u"0.005", None))
        self.btnRun.setText(QCoreApplication.translate("MainWindow", u"RUN", None))
    # retranslateUi

