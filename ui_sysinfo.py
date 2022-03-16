# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sysinfo2pwzYEB.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar
from PySide2extn.SpiralProgressBar import spiralProgressBar

import icons_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1058, 676)
        MainWindow.setStyleSheet(u"*{\n"
"	border:none;\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_frame = QFrame(self.centralwidget)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.header_frame.setFrameShape(QFrame.NoFrame)
        self.header_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.header_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_left = QFrame(self.header_frame)
        self.header_left.setObjectName(u"header_left")
        self.header_left.setFrameShape(QFrame.StyledPanel)
        self.header_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.header_left)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.btn_menu = QPushButton(self.header_left)
        self.btn_menu.setObjectName(u"btn_menu")
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        self.btn_menu.setFont(font)
        self.btn_menu.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/scalable/application-menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_menu.setIcon(icon)
        self.btn_menu.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_menu)


        self.horizontalLayout.addWidget(self.header_left, 0, Qt.AlignLeft)

        self.header_body = QFrame(self.header_frame)
        self.header_body.setObjectName(u"header_body")
        self.header_body.setFrameShape(QFrame.StyledPanel)
        self.header_body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.header_body)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label = QLabel(self.header_body)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setFamily(u"Serif")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_3.addWidget(self.label)


        self.horizontalLayout.addWidget(self.header_body)

        self.header_right = QFrame(self.header_frame)
        self.header_right.setObjectName(u"header_right")
        self.header_right.setFrameShape(QFrame.StyledPanel)
        self.header_right.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header_right)
        self.horizontalLayout_2.setSpacing(10)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout.addWidget(self.header_right, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.body_frame = QFrame(self.centralwidget)
        self.body_frame.setObjectName(u"body_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body_frame.sizePolicy().hasHeightForWidth())
        self.body_frame.setSizePolicy(sizePolicy)
        self.body_frame.setStyleSheet(u"background-color: rgb(61, 56, 70);\n"
"color: rgb(255, 255, 255);")
        self.body_frame.setFrameShape(QFrame.NoFrame)
        self.body_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.body_frame)
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.menu_frame_left = QFrame(self.body_frame)
        self.menu_frame_left.setObjectName(u"menu_frame_left")
        self.menu_frame_left.setMinimumSize(QSize(40, 0))
        self.menu_frame_left.setMaximumSize(QSize(20, 16777215))
        self.menu_frame_left.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.menu_frame_left.setFrameShape(QFrame.StyledPanel)
        self.menu_frame_left.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.menu_frame_left)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.menu_frame = QFrame(self.menu_frame_left)
        self.menu_frame.setObjectName(u"menu_frame")
        self.menu_frame.setEnabled(True)
        self.menu_frame.setMinimumSize(QSize(150, 0))
        self.menu_frame.setFrameShape(QFrame.StyledPanel)
        self.menu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.menu_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.btn_cpu = QPushButton(self.menu_frame)
        self.btn_cpu.setObjectName(u"btn_cpu")
        icon1 = QIcon()
        icon1.addFile(u":/scalable/cpu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cpu.setIcon(icon1)
        self.btn_cpu.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_cpu, 0, 0, 1, 1, Qt.AlignLeft)

        self.label_3 = QLabel(self.menu_frame)
        self.label_3.setObjectName(u"label_3")
        font2 = QFont()
        font2.setFamily(u"Sans Serif")
        font2.setBold(True)
        font2.setWeight(75)
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_3.setMargin(5)

        self.gridLayout.addWidget(self.label_3, 0, 1, 1, 1, Qt.AlignLeft)

        self.btn_systeminfo = QPushButton(self.menu_frame)
        self.btn_systeminfo.setObjectName(u"btn_systeminfo")
        icon2 = QIcon()
        icon2.addFile(u":/scalable/system.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_systeminfo.setIcon(icon2)
        self.btn_systeminfo.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_systeminfo, 2, 0, 1, 1, Qt.AlignLeft)

        self.label_7 = QLabel(self.menu_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_7.setMargin(5)

        self.gridLayout.addWidget(self.label_7, 4, 1, 1, 1, Qt.AlignLeft)

        self.btn_activity = QPushButton(self.menu_frame)
        self.btn_activity.setObjectName(u"btn_activity")
        icon3 = QIcon()
        icon3.addFile(u":/scalable/network-rj11-female.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_activity.setIcon(icon3)
        self.btn_activity.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_activity, 3, 0, 1, 1, Qt.AlignLeft)

        self.label_6 = QLabel(self.menu_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_6.setMargin(5)

        self.gridLayout.addWidget(self.label_6, 3, 1, 1, 1, Qt.AlignLeft)

        self.label_5 = QLabel(self.menu_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font2)
        self.label_5.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_5.setMargin(5)

        self.gridLayout.addWidget(self.label_5, 2, 1, 1, 1, Qt.AlignLeft)

        self.label_4 = QLabel(self.menu_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_4.setMargin(5)

        self.gridLayout.addWidget(self.label_4, 1, 1, 1, 1, Qt.AlignLeft)

        self.btn_storage = QPushButton(self.menu_frame)
        self.btn_storage.setObjectName(u"btn_storage")
        icon4 = QIcon()
        icon4.addFile(u":/scalable/drive-harddisk-encrypted.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_storage.setIcon(icon4)
        self.btn_storage.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_storage, 4, 0, 1, 1, Qt.AlignLeft)

        self.btn_battry = QPushButton(self.menu_frame)
        self.btn_battry.setObjectName(u"btn_battry")
        icon5 = QIcon()
        icon5.addFile(u":/scalable/battery.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_battry.setIcon(icon5)
        self.btn_battry.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_battry, 1, 0, 1, 1, Qt.AlignLeft)

        self.label_8 = QLabel(self.menu_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font2)
        self.label_8.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_8.setMargin(5)

        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1, Qt.AlignLeft)

        self.btn_sensors = QPushButton(self.menu_frame)
        self.btn_sensors.setObjectName(u"btn_sensors")
        icon6 = QIcon()
        icon6.addFile(u":/scalable/cs-tablet.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sensors.setIcon(icon6)
        self.btn_sensors.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_sensors, 5, 0, 1, 1, Qt.AlignLeft)

        self.btn_network = QPushButton(self.menu_frame)
        self.btn_network.setObjectName(u"btn_network")
        icon7 = QIcon()
        icon7.addFile(u":/scalable/network-wireless.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_network.setIcon(icon7)
        self.btn_network.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.btn_network, 6, 0, 1, 1, Qt.AlignLeft)

        self.label_9 = QLabel(self.menu_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font2)
        self.label_9.setStyleSheet(u"color: rgb(255, 255, 255);")
        self.label_9.setMargin(5)

        self.gridLayout.addWidget(self.label_9, 6, 1, 1, 1)


        self.horizontalLayout_9.addWidget(self.menu_frame)


        self.horizontalLayout_8.addWidget(self.menu_frame_left, 0, Qt.AlignLeft)

        self.Menu_frame_center = QFrame(self.body_frame)
        self.Menu_frame_center.setObjectName(u"Menu_frame_center")
        self.Menu_frame_center.setStyleSheet(u"")
        self.Menu_frame_center.setFrameShape(QFrame.StyledPanel)
        self.Menu_frame_center.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.Menu_frame_center)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.stackedWidget = QStackedWidget(self.Menu_frame_center)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.cpu = QWidget()
        self.cpu.setObjectName(u"cpu")
        self.verticalLayout_3 = QVBoxLayout(self.cpu)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.cpu)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.frame)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.cpu_count = QLabel(self.frame)
        self.cpu_count.setObjectName(u"cpu_count")
        font3 = QFont()
        font3.setPointSize(15)
        font3.setBold(True)
        font3.setWeight(75)
        self.cpu_count.setFont(font3)

        self.gridLayout_3.addWidget(self.cpu_count, 1, 1, 1, 1)

        self.label_25 = QLabel(self.frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font3)

        self.gridLayout_3.addWidget(self.label_25, 1, 0, 1, 1)

        self.label_30 = QLabel(self.frame)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font3)

        self.gridLayout_3.addWidget(self.label_30, 3, 0, 1, 1)

        self.cpu_info_frame = QFrame(self.frame)
        self.cpu_info_frame.setObjectName(u"cpu_info_frame")
        self.cpu_info_frame.setFrameShape(QFrame.StyledPanel)
        self.cpu_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.cpu_info_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_41 = QLabel(self.cpu_info_frame)
        self.label_41.setObjectName(u"label_41")
        font4 = QFont()
        font4.setPointSize(24)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_41.setFont(font4)
        self.label_41.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.verticalLayout_4.addWidget(self.label_41)


        self.gridLayout_3.addWidget(self.cpu_info_frame, 0, 0, 1, 1)

        self.cpu_main_core = QLabel(self.frame)
        self.cpu_main_core.setObjectName(u"cpu_main_core")
        self.cpu_main_core.setFont(font3)

        self.gridLayout_3.addWidget(self.cpu_main_core, 3, 1, 1, 1)

        self.label_27 = QLabel(self.frame)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font3)

        self.gridLayout_3.addWidget(self.label_27, 2, 0, 1, 1)

        self.cpu_per = QLabel(self.frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setFont(font3)

        self.gridLayout_3.addWidget(self.cpu_per, 2, 1, 1, 1)

        self.cpu_usage = roundProgressBar(self.frame)
        self.cpu_usage.setObjectName(u"cpu_usage")
        self.cpu_usage.setMinimumSize(QSize(200, 200))
        self.cpu_usage.setMaximumSize(QSize(250, 250))

        self.gridLayout_3.addWidget(self.cpu_usage, 0, 2, 4, 1)


        self.verticalLayout_3.addWidget(self.frame)

        self.ram_info_frame = QFrame(self.cpu)
        self.ram_info_frame.setObjectName(u"ram_info_frame")
        font5 = QFont()
        font5.setPointSize(11)
        self.ram_info_frame.setFont(font5)
        self.ram_info_frame.setFrameShape(QFrame.StyledPanel)
        self.ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.ram_info_frame)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.usage_ram = QLabel(self.ram_info_frame)
        self.usage_ram.setObjectName(u"usage_ram")
        self.usage_ram.setFont(font3)

        self.gridLayout_4.addWidget(self.usage_ram, 4, 1, 1, 1)

        self.used_ram = QLabel(self.ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setFont(font3)

        self.gridLayout_4.addWidget(self.used_ram, 2, 1, 1, 1)

        self.avaliable_ram = QLabel(self.ram_info_frame)
        self.avaliable_ram.setObjectName(u"avaliable_ram")
        self.avaliable_ram.setFont(font3)

        self.gridLayout_4.addWidget(self.avaliable_ram, 1, 1, 1, 1)

        self.label_33 = QLabel(self.ram_info_frame)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font3)

        self.gridLayout_4.addWidget(self.label_33, 1, 0, 1, 1)

        self.label_38 = QLabel(self.ram_info_frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font3)

        self.gridLayout_4.addWidget(self.label_38, 4, 0, 1, 1)

        self.Free_ram = QLabel(self.ram_info_frame)
        self.Free_ram.setObjectName(u"Free_ram")
        self.Free_ram.setFont(font3)

        self.gridLayout_4.addWidget(self.Free_ram, 3, 1, 1, 1)

        self.label_32 = QLabel(self.ram_info_frame)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font3)

        self.gridLayout_4.addWidget(self.label_32, 2, 0, 1, 1)

        self.total_ram = QLabel(self.ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setFont(font3)

        self.gridLayout_4.addWidget(self.total_ram, 0, 1, 1, 1)

        self.label_37 = QLabel(self.ram_info_frame)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font3)

        self.gridLayout_4.addWidget(self.label_37, 3, 0, 1, 1)

        self.label_29 = QLabel(self.ram_info_frame)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font3)

        self.gridLayout_4.addWidget(self.label_29, 0, 0, 1, 1)

        self.ram_usage_percent = spiralProgressBar(self.ram_info_frame)
        self.ram_usage_percent.setObjectName(u"ram_usage_percent")
        self.ram_usage_percent.setMinimumSize(QSize(200, 200))
        self.ram_usage_percent.setMaximumSize(QSize(250, 250))

        self.gridLayout_4.addWidget(self.ram_usage_percent, 2, 2, 1, 1)


        self.verticalLayout_3.addWidget(self.ram_info_frame)

        self.stackedWidget.addWidget(self.cpu)
        self.battery = QWidget()
        self.battery.setObjectName(u"battery")
        self.verticalLayout_5 = QVBoxLayout(self.battery)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_42 = QLabel(self.battery)
        self.label_42.setObjectName(u"label_42")
        font6 = QFont()
        font6.setPointSize(20)
        font6.setBold(True)
        font6.setWeight(75)
        self.label_42.setFont(font6)
        self.label_42.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.verticalLayout_5.addWidget(self.label_42, 0, Qt.AlignTop)

        self.frame_4 = QFrame(self.battery)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_4)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setVerticalSpacing(0)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.frame_4)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.frame_6)
        self.gridLayout_6.setSpacing(0)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.battery_charge = QLabel(self.frame_6)
        self.battery_charge.setObjectName(u"battery_charge")
        font7 = QFont()
        font7.setPointSize(16)
        font7.setBold(True)
        font7.setWeight(75)
        self.battery_charge.setFont(font7)

        self.gridLayout_6.addWidget(self.battery_charge, 1, 1, 1, 1)

        self.battery_status = QLabel(self.frame_6)
        self.battery_status.setObjectName(u"battery_status")
        self.battery_status.setFont(font7)

        self.gridLayout_6.addWidget(self.battery_status, 0, 1, 1, 1)

        self.battery_time_left = QLabel(self.frame_6)
        self.battery_time_left.setObjectName(u"battery_time_left")
        self.battery_time_left.setFont(font7)

        self.gridLayout_6.addWidget(self.battery_time_left, 2, 1, 1, 1)

        self.label_45 = QLabel(self.frame_6)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font7)

        self.gridLayout_6.addWidget(self.label_45, 1, 0, 1, 1)

        self.label_43 = QLabel(self.frame_6)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font7)

        self.gridLayout_6.addWidget(self.label_43, 0, 0, 1, 1)

        self.label_47 = QLabel(self.frame_6)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setFont(font7)

        self.gridLayout_6.addWidget(self.label_47, 2, 0, 1, 1)

        self.label_49 = QLabel(self.frame_6)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font7)

        self.gridLayout_6.addWidget(self.label_49, 3, 0, 1, 1)

        self.battery_plugged = QLabel(self.frame_6)
        self.battery_plugged.setObjectName(u"battery_plugged")
        self.battery_plugged.setFont(font7)

        self.gridLayout_6.addWidget(self.battery_plugged, 3, 1, 1, 1)


        self.gridLayout_5.addWidget(self.frame_6, 0, 0, 1, 1)

        self.battery_usage = roundProgressBar(self.frame_4)
        self.battery_usage.setObjectName(u"battery_usage")
        self.battery_usage.setMaximumSize(QSize(150, 150))

        self.gridLayout_5.addWidget(self.battery_usage, 0, 1, 2, 1)


        self.verticalLayout_5.addWidget(self.frame_4)

        self.stackedWidget.addWidget(self.battery)
        self.sysyeminfo = QWidget()
        self.sysyeminfo.setObjectName(u"sysyeminfo")
        self.verticalLayout_7 = QVBoxLayout(self.sysyeminfo)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.systeminfo_frame = QFrame(self.sysyeminfo)
        self.systeminfo_frame.setObjectName(u"systeminfo_frame")
        self.systeminfo_frame.setFrameShape(QFrame.StyledPanel)
        self.systeminfo_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.systeminfo_frame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.system_sys = QLabel(self.systeminfo_frame)
        self.system_sys.setObjectName(u"system_sys")
        font8 = QFont()
        font8.setPointSize(14)
        font8.setBold(True)
        font8.setWeight(75)
        self.system_sys.setFont(font8)

        self.gridLayout_2.addWidget(self.system_sys, 4, 1, 1, 1)

        self.label_12 = QLabel(self.systeminfo_frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font8)

        self.gridLayout_2.addWidget(self.label_12, 7, 0, 1, 1)

        self.label_17 = QLabel(self.systeminfo_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font8)

        self.gridLayout_2.addWidget(self.label_17, 2, 0, 1, 1)

        self.system_machine = QLabel(self.systeminfo_frame)
        self.system_machine.setObjectName(u"system_machine")
        self.system_machine.setFont(font8)

        self.gridLayout_2.addWidget(self.system_machine, 3, 1, 1, 1)

        self.label_13 = QLabel(self.systeminfo_frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)

        self.gridLayout_2.addWidget(self.label_13, 8, 0, 1, 1, Qt.AlignLeft)

        self.system_version = QLabel(self.systeminfo_frame)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setFont(font8)

        self.gridLayout_2.addWidget(self.system_version, 7, 1, 1, 1)

        self.system_time = QLabel(self.systeminfo_frame)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font8)

        self.gridLayout_2.addWidget(self.system_time, 5, 1, 1, 1)

        self.label_53 = QLabel(self.systeminfo_frame)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font4)
        self.label_53.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.gridLayout_2.addWidget(self.label_53, 0, 0, 1, 1)

        self.frame_3 = QFrame(self.systeminfo_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)

        self.gridLayout_2.addWidget(self.frame_3, 1, 2, 4, 1)

        self.label_10 = QLabel(self.systeminfo_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font8)

        self.gridLayout_2.addWidget(self.label_10, 1, 0, 1, 1)

        self.label_11 = QLabel(self.systeminfo_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font8)

        self.gridLayout_2.addWidget(self.label_11, 4, 0, 1, 1)

        self.system_release = QLabel(self.systeminfo_frame)
        self.system_release.setObjectName(u"system_release")
        self.system_release.setFont(font8)

        self.gridLayout_2.addWidget(self.system_release, 8, 1, 1, 1)

        self.system_processor = QLabel(self.systeminfo_frame)
        self.system_processor.setObjectName(u"system_processor")
        self.system_processor.setFont(font8)

        self.gridLayout_2.addWidget(self.system_processor, 2, 1, 1, 1)

        self.label_19 = QLabel(self.systeminfo_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font8)

        self.gridLayout_2.addWidget(self.label_19, 3, 0, 1, 1)

        self.system_name = QLabel(self.systeminfo_frame)
        self.system_name.setObjectName(u"system_name")
        self.system_name.setFont(font8)

        self.gridLayout_2.addWidget(self.system_name, 1, 1, 1, 1)

        self.label_18 = QLabel(self.systeminfo_frame)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font8)

        self.gridLayout_2.addWidget(self.label_18, 5, 0, 1, 1)

        self.label_21 = QLabel(self.systeminfo_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font8)

        self.gridLayout_2.addWidget(self.label_21, 6, 0, 1, 1)

        self.date_time = QLabel(self.systeminfo_frame)
        self.date_time.setObjectName(u"date_time")
        self.date_time.setFont(font8)

        self.gridLayout_2.addWidget(self.date_time, 6, 1, 1, 1, Qt.AlignLeft)


        self.verticalLayout_7.addWidget(self.systeminfo_frame)

        self.stackedWidget.addWidget(self.sysyeminfo)
        self.activity = QWidget()
        self.activity.setObjectName(u"activity")
        self.verticalLayout_9 = QVBoxLayout(self.activity)
        self.verticalLayout_9.setSpacing(0)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.activity)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_54 = QLabel(self.frame_5)
        self.label_54.setObjectName(u"label_54")
        font9 = QFont()
        font9.setPointSize(17)
        font9.setBold(True)
        font9.setWeight(75)
        self.label_54.setFont(font9)
        self.label_54.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.horizontalLayout_10.addWidget(self.label_54, 0, Qt.AlignLeft)

        self.frame_9 = QFrame(self.frame_5)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lineEdit = QLineEdit(self.frame_9)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"color: rgb(255, 255, 255);")

        self.horizontalLayout_11.addWidget(self.lineEdit, 0, Qt.AlignRight)

        self.pushButton_2 = QPushButton(self.frame_9)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setIconSize(QSize(16, 16))

        self.horizontalLayout_11.addWidget(self.pushButton_2)


        self.horizontalLayout_10.addWidget(self.frame_9)


        self.verticalLayout_9.addWidget(self.frame_5, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.activity)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.NoFrame)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.frame_7)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.tableWidget = QTableWidget(self.frame_7)
        if (self.tableWidget.columnCount() < 8):
            self.tableWidget.setColumnCount(8)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout_10.addWidget(self.tableWidget)


        self.verticalLayout_9.addWidget(self.frame_7)

        self.frame_8 = QFrame(self.activity)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.frame_8)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.brn_suspend = QPushButton(self.frame_8)
        self.brn_suspend.setObjectName(u"brn_suspend")

        self.horizontalLayout_12.addWidget(self.brn_suspend)

        self.btn_resume = QPushButton(self.frame_8)
        self.btn_resume.setObjectName(u"btn_resume")

        self.horizontalLayout_12.addWidget(self.btn_resume)

        self.btn_terminate = QPushButton(self.frame_8)
        self.btn_terminate.setObjectName(u"btn_terminate")

        self.horizontalLayout_12.addWidget(self.btn_terminate)

        self.btn_Kill = QPushButton(self.frame_8)
        self.btn_Kill.setObjectName(u"btn_Kill")

        self.horizontalLayout_12.addWidget(self.btn_Kill)


        self.verticalLayout_9.addWidget(self.frame_8, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.activity)
        self.storage = QWidget()
        self.storage.setObjectName(u"storage")
        self.verticalLayout_8 = QVBoxLayout(self.storage)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_2 = QFrame(self.storage)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayout_7 = QGridLayout(self.frame_2)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setHorizontalSpacing(0)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.storege_used = roundProgressBar(self.frame_2)
        self.storege_used.setObjectName(u"storege_used")

        self.gridLayout_7.addWidget(self.storege_used, 2, 2, 1, 1)

        self.diskused_size = QLabel(self.frame_2)
        self.diskused_size.setObjectName(u"diskused_size")

        self.gridLayout_7.addWidget(self.diskused_size, 2, 1, 1, 1)

        self.label_16 = QLabel(self.frame_2)
        self.label_16.setObjectName(u"label_16")

        self.gridLayout_7.addWidget(self.label_16, 4, 0, 1, 1)

        self.diskfree_size = QLabel(self.frame_2)
        self.diskfree_size.setObjectName(u"diskfree_size")

        self.gridLayout_7.addWidget(self.diskfree_size, 4, 1, 1, 1)

        self.label_55 = QLabel(self.frame_2)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font9)
        self.label_55.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.gridLayout_7.addWidget(self.label_55, 0, 0, 1, 2, Qt.AlignTop)

        self.storeage_free = roundProgressBar(self.frame_2)
        self.storeage_free.setObjectName(u"storeage_free")

        self.gridLayout_7.addWidget(self.storeage_free, 4, 2, 1, 1)

        self.label_14 = QLabel(self.frame_2)
        self.label_14.setObjectName(u"label_14")

        self.gridLayout_7.addWidget(self.label_14, 1, 0, 1, 1)

        self.disktotal_size = QLabel(self.frame_2)
        self.disktotal_size.setObjectName(u"disktotal_size")

        self.gridLayout_7.addWidget(self.disktotal_size, 1, 1, 1, 1)

        self.label_15 = QLabel(self.frame_2)
        self.label_15.setObjectName(u"label_15")

        self.gridLayout_7.addWidget(self.label_15, 2, 0, 1, 1)

        self.storeage_disk = roundProgressBar(self.frame_2)
        self.storeage_disk.setObjectName(u"storeage_disk")

        self.gridLayout_7.addWidget(self.storeage_disk, 1, 2, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_2)

        self.stackedWidget.addWidget(self.storage)
        self.sensors = QWidget()
        self.sensors.setObjectName(u"sensors")
        self.label_56 = QLabel(self.sensors)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setGeometry(QRect(10, 10, 454, 27))
        self.label_56.setFont(font9)
        self.label_56.setStyleSheet(u"color: rgb(224, 27, 36);")
        self.stackedWidget.addWidget(self.sensors)
        self.network = QWidget()
        self.network.setObjectName(u"network")
        self.verticalLayout_11 = QVBoxLayout(self.network)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_10 = QFrame(self.network)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_10)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.label_57 = QLabel(self.frame_10)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font9)
        self.label_57.setStyleSheet(u"color: rgb(224, 27, 36);")

        self.gridLayout_8.addWidget(self.label_57, 0, 0, 1, 1)

        self.label_22 = QLabel(self.frame_10)
        self.label_22.setObjectName(u"label_22")

        self.gridLayout_8.addWidget(self.label_22, 3, 0, 1, 1)

        self.network_ip = QLabel(self.frame_10)
        self.network_ip.setObjectName(u"network_ip")

        self.gridLayout_8.addWidget(self.network_ip, 3, 1, 1, 1)

        self.label_20 = QLabel(self.frame_10)
        self.label_20.setObjectName(u"label_20")

        self.gridLayout_8.addWidget(self.label_20, 1, 0, 1, 1)

        self.network_name = QLabel(self.frame_10)
        self.network_name.setObjectName(u"network_name")

        self.gridLayout_8.addWidget(self.network_name, 1, 1, 1, 1)

        self.label_23 = QLabel(self.frame_10)
        self.label_23.setObjectName(u"label_23")

        self.gridLayout_8.addWidget(self.label_23, 5, 0, 1, 1)

        self.label_24 = QLabel(self.frame_10)
        self.label_24.setObjectName(u"label_24")

        self.gridLayout_8.addWidget(self.label_24, 4, 0, 1, 1)

        self.up = QLabel(self.frame_10)
        self.up.setObjectName(u"up")

        self.gridLayout_8.addWidget(self.up, 4, 1, 1, 1)

        self.down = QLabel(self.frame_10)
        self.down.setObjectName(u"down")

        self.gridLayout_8.addWidget(self.down, 5, 1, 1, 1)


        self.verticalLayout_11.addWidget(self.frame_10)

        self.stackedWidget.addWidget(self.network)

        self.verticalLayout_2.addWidget(self.stackedWidget)


        self.horizontalLayout_8.addWidget(self.Menu_frame_center)

        self.bodyframe_right = QFrame(self.body_frame)
        self.bodyframe_right.setObjectName(u"bodyframe_right")
        self.bodyframe_right.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.bodyframe_right.setFrameShape(QFrame.StyledPanel)
        self.bodyframe_right.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.bodyframe_right)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)

        self.horizontalLayout_8.addWidget(self.bodyframe_right)


        self.verticalLayout.addWidget(self.body_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setStyleSheet(u"background-color: rgb(94, 92, 100);")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.footer_left_frame = QFrame(self.footer_frame)
        self.footer_left_frame.setObjectName(u"footer_left_frame")
        self.footer_left_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_left_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.footer_left_frame)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label_2 = QLabel(self.footer_left_frame)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_6.addWidget(self.label_2, 0, Qt.AlignLeft)


        self.horizontalLayout_5.addWidget(self.footer_left_frame)

        self.footer_right_frame = QFrame(self.footer_frame)
        self.footer_right_frame.setObjectName(u"footer_right_frame")
        self.footer_right_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_right_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.footer_right_frame)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.pushButton = QPushButton(self.footer_right_frame)
        self.pushButton.setObjectName(u"pushButton")

        self.horizontalLayout_7.addWidget(self.pushButton, 0, Qt.AlignRight)


        self.horizontalLayout_5.addWidget(self.footer_right_frame)

        self.frame_grip = QFrame(self.footer_frame)
        self.frame_grip.setObjectName(u"frame_grip")
        self.frame_grip.setMinimumSize(QSize(10, 10))
        self.frame_grip.setMaximumSize(QSize(10, 10))
        self.frame_grip.setFrameShape(QFrame.StyledPanel)
        self.frame_grip.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_5.addWidget(self.frame_grip)


        self.verticalLayout.addWidget(self.footer_frame, 0, Qt.AlignBottom)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(6)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"CPU iNfO", None))
        self.btn_menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Cpu Info", None))
        self.btn_cpu.setText("")
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU", None))
        self.btn_systeminfo.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.btn_activity.setText("")
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Activites", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"System info", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.btn_storage.setText("")
        self.btn_battry.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.btn_sensors.setText("")
        self.btn_network.setText("")
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Networks", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"Cpu count", None))
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"cpu main core", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"CPU info", None))
        self.cpu_main_core.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"cpu per", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.usage_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.avaliable_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Available Ram", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Ram Usage", None))
        self.Free_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Used Ram", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Free Ram", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"Total ram", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Battery info", None))
        self.battery_charge.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_status.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.battery_time_left.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.battery_plugged.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_sys.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"processor", None))
        self.system_machine.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"System info", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"system", None))
        self.system_release.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.system_processor.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"machine", None))
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"System Up-Time", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Date Time", None))
        self.date_time.setText(QCoreApplication.translate("MainWindow", u"N/A", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Activity", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search processes", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"search", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Process_id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Process_name", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Process_status", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Started", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Suspend", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Resume", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Terminate", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Kill", None));
        self.brn_suspend.setText(QCoreApplication.translate("MainWindow", u"Suspend", None))
        self.btn_resume.setText(QCoreApplication.translate("MainWindow", u"Resume", None))
        self.btn_terminate.setText(QCoreApplication.translate("MainWindow", u"Terminate", None))
        self.btn_Kill.setText(QCoreApplication.translate("MainWindow", u"Kill", None))
        self.diskused_size.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Disk Free", None))
        self.diskfree_size.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Storage", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Disk Total Size", None))
        self.disktotal_size.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Disk used", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Sensors", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Network", None))
        self.label_22.setText(QCoreApplication.translate("MainWindow", u"IP", None))
        self.network_ip.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"NetWork Card", None))
        self.network_name.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"up", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.up.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.down.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"cpu v.1.0 www.sullinux.com", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"?", None))
    # retranslateUi

