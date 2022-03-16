from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from PySide2extn.RoundProgressBar import roundProgressBar


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1165, 720)
        MainWindow.setMinimumSize(QSize(1165, 720))
        font = QFont()
        font.setBold(True)
        font.setWeight(75)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"QFrame{\n"
"	background-color: rgb(36, 31, 49);\n"
"}\n"
"\n"
"QLabel{\n"
"	color: rgb(1, 255, 255);\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.system_cpu_frame = QFrame(self.centralwidget)
        self.system_cpu_frame.setObjectName(u"system_cpu_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.system_cpu_frame.sizePolicy().hasHeightForWidth())
        self.system_cpu_frame.setSizePolicy(sizePolicy)
        self.system_cpu_frame.setFrameShape(QFrame.NoFrame)
        self.system_cpu_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.system_cpu_frame)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.systeminfo_frame = QFrame(self.system_cpu_frame)
        self.systeminfo_frame.setObjectName(u"systeminfo_frame")
        self.systeminfo_frame.setFrameShape(QFrame.NoFrame)
        self.systeminfo_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.systeminfo_frame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(6)
        self.gridLayout.setVerticalSpacing(0)
        self.gridLayout.setContentsMargins(6, 0, 0, 0)
        self.system_name = QLabel(self.systeminfo_frame)
        self.system_name.setObjectName(u"system_name")
        font1 = QFont()
        font1.setFamily(u"Serif")
        font1.setPointSize(11)
        font1.setBold(True)
        font1.setWeight(75)
        self.system_name.setFont(font1)

        self.gridLayout.addWidget(self.system_name, 7, 2, 1, 1)

        self.processor_name = QLabel(self.systeminfo_frame)
        self.processor_name.setObjectName(u"processor_name")
        self.processor_name.setFont(font1)

        self.gridLayout.addWidget(self.processor_name, 3, 2, 1, 1)

        self.system_release = QLabel(self.systeminfo_frame)
        self.system_release.setObjectName(u"system_release")
        self.system_release.setFont(font1)

        self.gridLayout.addWidget(self.system_release, 4, 5, 1, 1)

        self.label_2 = QLabel(self.systeminfo_frame)
        self.label_2.setObjectName(u"label_2")
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_2.setFont(font2)
        self.label_2.setStyleSheet(u"color: rgb(250, 4, 4);")

        self.gridLayout.addWidget(self.label_2, 0, 0, 1, 6)

        self.label_10 = QLabel(self.systeminfo_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.gridLayout.addWidget(self.label_10, 4, 0, 1, 1)

        self.system_version = QLabel(self.systeminfo_frame)
        self.system_version.setObjectName(u"system_version")
        self.system_version.setFont(font1)

        self.gridLayout.addWidget(self.system_version, 3, 5, 1, 1)

        self.label_11 = QLabel(self.systeminfo_frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font)

        self.gridLayout.addWidget(self.label_11, 1, 0, 1, 1)

        self.label_9 = QLabel(self.systeminfo_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font)

        self.gridLayout.addWidget(self.label_9, 3, 0, 1, 1)

        self.system_time = QLabel(self.systeminfo_frame)
        self.system_time.setObjectName(u"system_time")
        self.system_time.setFont(font1)

        self.gridLayout.addWidget(self.system_time, 1, 5, 1, 1)

        self.machine_name = QLabel(self.systeminfo_frame)
        self.machine_name.setObjectName(u"machine_name")
        self.machine_name.setFont(font1)

        self.gridLayout.addWidget(self.machine_name, 4, 2, 1, 1)

        self.label_16 = QLabel(self.systeminfo_frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font)

        self.gridLayout.addWidget(self.label_16, 7, 0, 1, 1)

        self.sysinfo_name = QLabel(self.systeminfo_frame)
        self.sysinfo_name.setObjectName(u"sysinfo_name")
        self.sysinfo_name.setFont(font1)

        self.gridLayout.addWidget(self.sysinfo_name, 1, 2, 1, 1)

        self.label_17 = QLabel(self.systeminfo_frame)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setFont(font)

        self.gridLayout.addWidget(self.label_17, 1, 3, 1, 1)

        self.label_19 = QLabel(self.systeminfo_frame)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font)

        self.gridLayout.addWidget(self.label_19, 3, 3, 1, 1)

        self.label_21 = QLabel(self.systeminfo_frame)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font)

        self.gridLayout.addWidget(self.label_21, 4, 3, 1, 1)

        self.label = QLabel(self.systeminfo_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.gridLayout.addWidget(self.label, 7, 3, 1, 1)

        self.timesystem = QLabel(self.systeminfo_frame)
        self.timesystem.setObjectName(u"timesystem")
        font3 = QFont()
        font3.setFamily(u"Serif")
        font3.setBold(True)
        font3.setWeight(75)
        self.timesystem.setFont(font3)

        self.gridLayout.addWidget(self.timesystem, 7, 5, 1, 1)


        self.horizontalLayout.addWidget(self.systeminfo_frame)

        self.cpu_frame = QFrame(self.system_cpu_frame)
        self.cpu_frame.setObjectName(u"cpu_frame")
        self.cpu_frame.setFrameShape(QFrame.NoFrame)
        self.cpu_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.cpu_frame)
        self.gridLayout_2.setSpacing(0)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(6, 0, 0, 0)
        self.cpu_per = QLabel(self.cpu_frame)
        self.cpu_per.setObjectName(u"cpu_per")
        self.cpu_per.setFont(font1)

        self.gridLayout_2.addWidget(self.cpu_per, 2, 1, 1, 1)

        self.cpu_core = QLabel(self.cpu_frame)
        self.cpu_core.setObjectName(u"cpu_core")
        self.cpu_core.setFont(font1)

        self.gridLayout_2.addWidget(self.cpu_core, 3, 1, 1, 1)

        self.label_3 = QLabel(self.cpu_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font2)
        self.label_3.setStyleSheet(u"color: rgb(250, 4, 4);")

        self.gridLayout_2.addWidget(self.label_3, 0, 0, 1, 1)

        self.label_26 = QLabel(self.cpu_frame)
        self.label_26.setObjectName(u"label_26")
        self.label_26.setFont(font)

        self.gridLayout_2.addWidget(self.label_26, 2, 0, 1, 1)

        self.label_23 = QLabel(self.cpu_frame)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setFont(font)

        self.gridLayout_2.addWidget(self.label_23, 1, 0, 1, 1)

        self.cpu_count = QLabel(self.cpu_frame)
        self.cpu_count.setObjectName(u"cpu_count")
        self.cpu_count.setFont(font1)

        self.gridLayout_2.addWidget(self.cpu_count, 1, 1, 1, 1)

        self.label_25 = QLabel(self.cpu_frame)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font)

        self.gridLayout_2.addWidget(self.label_25, 3, 0, 1, 1)

        self.cpu_round_progbar = roundProgressBar(self.cpu_frame)
        self.cpu_round_progbar.setObjectName(u"cpu_round_progbar")
        self.cpu_round_progbar.setMaximumSize(QSize(180, 100))

        self.gridLayout_2.addWidget(self.cpu_round_progbar, 0, 2, 4, 1)


        self.horizontalLayout.addWidget(self.cpu_frame)


        self.verticalLayout.addWidget(self.system_cpu_frame)

        self.battery_frame = QFrame(self.centralwidget)
        self.battery_frame.setObjectName(u"battery_frame")
        self.battery_frame.setFrameShape(QFrame.NoFrame)
        self.battery_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.battery_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.battery_info_frame = QFrame(self.battery_frame)
        self.battery_info_frame.setObjectName(u"battery_info_frame")
        self.battery_info_frame.setFrameShape(QFrame.NoFrame)
        self.battery_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.battery_info_frame)
        self.gridLayout_5.setSpacing(0)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(6, 0, 0, 0)
        self.label_46 = QLabel(self.battery_info_frame)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font)

        self.gridLayout_5.addWidget(self.label_46, 4, 0, 1, 1)

        self.label_51 = QLabel(self.battery_info_frame)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font)

        self.gridLayout_5.addWidget(self.label_51, 7, 0, 1, 1)

        self.b_plugged = QLabel(self.battery_info_frame)
        self.b_plugged.setObjectName(u"b_plugged")
        self.b_plugged.setFont(font1)

        self.gridLayout_5.addWidget(self.b_plugged, 7, 2, 1, 1)

        self.b_charge = QLabel(self.battery_info_frame)
        self.b_charge.setObjectName(u"b_charge")
        self.b_charge.setFont(font1)

        self.gridLayout_5.addWidget(self.b_charge, 3, 2, 1, 1)

        self.label_6 = QLabel(self.battery_info_frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font2)
        self.label_6.setStyleSheet(u"color: rgb(250, 4, 4);")

        self.gridLayout_5.addWidget(self.label_6, 0, 0, 1, 5)

        self.label_49 = QLabel(self.battery_info_frame)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font)

        self.gridLayout_5.addWidget(self.label_49, 1, 0, 1, 1)

        self.b_timeleft = QLabel(self.battery_info_frame)
        self.b_timeleft.setObjectName(u"b_timeleft")
        self.b_timeleft.setFont(font1)

        self.gridLayout_5.addWidget(self.b_timeleft, 4, 2, 1, 1)

        self.label_50 = QLabel(self.battery_info_frame)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font)

        self.gridLayout_5.addWidget(self.label_50, 3, 0, 1, 1)

        self.b_status = QLabel(self.battery_info_frame)
        self.b_status.setObjectName(u"b_status")
        self.b_status.setFont(font1)

        self.gridLayout_5.addWidget(self.b_status, 1, 2, 1, 1)


        self.horizontalLayout_5.addWidget(self.battery_info_frame)

        self.battery_roundprogress_frame = QFrame(self.battery_frame)
        self.battery_roundprogress_frame.setObjectName(u"battery_roundprogress_frame")
        self.battery_roundprogress_frame.setFrameShape(QFrame.NoFrame)
        self.battery_roundprogress_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.battery_roundprogress_frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.battery_roundprogress_frame)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_8)

        self.battery_bar_widget = roundProgressBar(self.battery_roundprogress_frame)
        self.battery_bar_widget.setObjectName(u"battery_bar_widget")
        self.battery_bar_widget.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_4.addWidget(self.battery_bar_widget)

        self.frame_9 = QFrame(self.battery_roundprogress_frame)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.NoFrame)
        self.frame_9.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_4.addWidget(self.frame_9)


        self.horizontalLayout_5.addWidget(self.battery_roundprogress_frame)


        self.verticalLayout.addWidget(self.battery_frame)

        self.storage_frame = QFrame(self.centralwidget)
        self.storage_frame.setObjectName(u"storage_frame")
        self.storage_frame.setFrameShape(QFrame.NoFrame)
        self.storage_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.storage_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(6, 0, 0, 0)
        self.storage_info_frame = QFrame(self.storage_frame)
        self.storage_info_frame.setObjectName(u"storage_info_frame")
        self.storage_info_frame.setFrameShape(QFrame.NoFrame)
        self.storage_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_4 = QGridLayout(self.storage_info_frame)
        self.gridLayout_4.setSpacing(0)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_40 = QLabel(self.storage_info_frame)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font)

        self.gridLayout_4.addWidget(self.label_40, 3, 0, 1, 1)

        self.total_storage = QLabel(self.storage_info_frame)
        self.total_storage.setObjectName(u"total_storage")
        self.total_storage.setFont(font1)

        self.gridLayout_4.addWidget(self.total_storage, 1, 1, 1, 1)

        self.label_41 = QLabel(self.storage_info_frame)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font)

        self.gridLayout_4.addWidget(self.label_41, 2, 0, 1, 1)

        self.label_38 = QLabel(self.storage_info_frame)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font)

        self.gridLayout_4.addWidget(self.label_38, 1, 0, 1, 1)

        self.used_storage = QLabel(self.storage_info_frame)
        self.used_storage.setObjectName(u"used_storage")
        self.used_storage.setFont(font1)

        self.gridLayout_4.addWidget(self.used_storage, 2, 1, 1, 1)

        self.label_7 = QLabel(self.storage_info_frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font2)
        self.label_7.setStyleSheet(u"color: rgb(250, 4, 4);")

        self.gridLayout_4.addWidget(self.label_7, 0, 0, 1, 1)

        self.free_storage = QLabel(self.storage_info_frame)
        self.free_storage.setObjectName(u"free_storage")
        self.free_storage.setFont(font1)

        self.gridLayout_4.addWidget(self.free_storage, 3, 1, 1, 1)


        self.horizontalLayout_2.addWidget(self.storage_info_frame, 0, Qt.AlignLeft)

        self.progress_storage_frame = QFrame(self.storage_frame)
        self.progress_storage_frame.setObjectName(u"progress_storage_frame")
        self.progress_storage_frame.setFrameShape(QFrame.NoFrame)
        self.progress_storage_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.progress_storage_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.totalstorage_bar = roundProgressBar(self.progress_storage_frame)
        self.totalstorage_bar.setObjectName(u"totalstorage_bar")
        self.totalstorage_bar.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_3.addWidget(self.totalstorage_bar)

        self.used_storage_bar = roundProgressBar(self.progress_storage_frame)
        self.used_storage_bar.setObjectName(u"used_storage_bar")
        self.used_storage_bar.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_3.addWidget(self.used_storage_bar)

        self.Free_storage_bar = roundProgressBar(self.progress_storage_frame)
        self.Free_storage_bar.setObjectName(u"Free_storage_bar")
        self.Free_storage_bar.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_3.addWidget(self.Free_storage_bar)


        self.horizontalLayout_2.addWidget(self.progress_storage_frame)


        self.verticalLayout.addWidget(self.storage_frame)

        self.memory_info_frame = QFrame(self.centralwidget)
        self.memory_info_frame.setObjectName(u"memory_info_frame")
        sizePolicy.setHeightForWidth(self.memory_info_frame.sizePolicy().hasHeightForWidth())
        self.memory_info_frame.setSizePolicy(sizePolicy)
        self.memory_info_frame.setFrameShape(QFrame.NoFrame)
        self.memory_info_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.memory_info_frame)
        self.horizontalLayout_7.setSpacing(0)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(6, 0, 0, 0)
        self.Ram_info_frame = QFrame(self.memory_info_frame)
        self.Ram_info_frame.setObjectName(u"Ram_info_frame")
        self.Ram_info_frame.setFrameShape(QFrame.NoFrame)
        self.Ram_info_frame.setFrameShadow(QFrame.Raised)
        self.gridLayout_6 = QGridLayout(self.Ram_info_frame)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setHorizontalSpacing(6)
        self.gridLayout_6.setVerticalSpacing(0)
        self.gridLayout_6.setContentsMargins(6, 0, 0, 0)
        self.label_54 = QLabel(self.Ram_info_frame)
        self.label_54.setObjectName(u"label_54")
        self.label_54.setFont(font)

        self.gridLayout_6.addWidget(self.label_54, 4, 0, 1, 1)

        self.free_ram = QLabel(self.Ram_info_frame)
        self.free_ram.setObjectName(u"free_ram")
        self.free_ram.setFont(font1)

        self.gridLayout_6.addWidget(self.free_ram, 7, 2, 1, 1)

        self.label_58 = QLabel(self.Ram_info_frame)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font)

        self.gridLayout_6.addWidget(self.label_58, 3, 0, 1, 1)

        self.label_4 = QLabel(self.Ram_info_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font2)
        self.label_4.setStyleSheet(u"color: rgb(250, 4, 4);")

        self.gridLayout_6.addWidget(self.label_4, 0, 0, 1, 5)

        self.available_ram = QLabel(self.Ram_info_frame)
        self.available_ram.setObjectName(u"available_ram")
        self.available_ram.setFont(font1)

        self.gridLayout_6.addWidget(self.available_ram, 3, 2, 1, 1)

        self.used_ram = QLabel(self.Ram_info_frame)
        self.used_ram.setObjectName(u"used_ram")
        self.used_ram.setFont(font1)

        self.gridLayout_6.addWidget(self.used_ram, 4, 2, 1, 1)

        self.total_ram = QLabel(self.Ram_info_frame)
        self.total_ram.setObjectName(u"total_ram")
        self.total_ram.setFont(font1)

        self.gridLayout_6.addWidget(self.total_ram, 1, 2, 1, 1)

        self.label_57 = QLabel(self.Ram_info_frame)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font)

        self.gridLayout_6.addWidget(self.label_57, 1, 0, 1, 1)

        self.label_59 = QLabel(self.Ram_info_frame)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font)

        self.gridLayout_6.addWidget(self.label_59, 7, 0, 1, 1)


        self.horizontalLayout_7.addWidget(self.Ram_info_frame)

        self.progress_ram_frame = QFrame(self.memory_info_frame)
        self.progress_ram_frame.setObjectName(u"progress_ram_frame")
        self.progress_ram_frame.setFrameShape(QFrame.NoFrame)
        self.progress_ram_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.progress_ram_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.Total_ram_bar = roundProgressBar(self.progress_ram_frame)
        self.Total_ram_bar.setObjectName(u"Total_ram_bar")
        self.Total_ram_bar.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_6.addWidget(self.Total_ram_bar)

        self.Used_ram_bar = roundProgressBar(self.progress_ram_frame)
        self.Used_ram_bar.setObjectName(u"Used_ram_bar")
        self.Used_ram_bar.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_6.addWidget(self.Used_ram_bar)

        self.Free_ram_bar = roundProgressBar(self.progress_ram_frame)
        self.Free_ram_bar.setObjectName(u"Free_ram_bar")
        self.Free_ram_bar.setMaximumSize(QSize(180, 100))

        self.horizontalLayout_6.addWidget(self.Free_ram_bar)


        self.horizontalLayout_7.addWidget(self.progress_ram_frame)


        self.verticalLayout.addWidget(self.memory_info_frame)

        self.footer_frame = QFrame(self.centralwidget)
        self.footer_frame.setObjectName(u"footer_frame")
        self.footer_frame.setFrameShape(QFrame.NoFrame)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.footer_frame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.network_frame_info = QFrame(self.footer_frame)
        self.network_frame_info.setObjectName(u"network_frame_info")
        self.network_frame_info.setFrameShape(QFrame.NoFrame)
        self.network_frame_info.setFrameShadow(QFrame.Raised)
        self.gridLayout_3 = QGridLayout(self.network_frame_info)
        self.gridLayout_3.setSpacing(0)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(6, 0, 0, 0)
        self.network_card = QLabel(self.network_frame_info)
        self.network_card.setObjectName(u"network_card")
        self.network_card.setFont(font1)

        self.gridLayout_3.addWidget(self.network_card, 1, 2, 1, 1)

        self.label_31 = QLabel(self.network_frame_info)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)
        self.label_31.setStyleSheet(u"color: rgb(250, 4, 4);")

        self.gridLayout_3.addWidget(self.label_31, 0, 0, 1, 6)

        self.network_down = QLabel(self.network_frame_info)
        self.network_down.setObjectName(u"network_down")
        self.network_down.setFont(font1)

        self.gridLayout_3.addWidget(self.network_down, 3, 5, 1, 1)

        self.label_35 = QLabel(self.network_frame_info)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setFont(font)

        self.gridLayout_3.addWidget(self.label_35, 1, 0, 1, 1)

        self.label_32 = QLabel(self.network_frame_info)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font)

        self.gridLayout_3.addWidget(self.label_32, 1, 3, 1, 1)

        self.label_36 = QLabel(self.network_frame_info)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font)

        self.gridLayout_3.addWidget(self.label_36, 3, 0, 1, 1)

        self.network_ip = QLabel(self.network_frame_info)
        self.network_ip.setObjectName(u"network_ip")
        self.network_ip.setFont(font1)

        self.gridLayout_3.addWidget(self.network_ip, 3, 2, 1, 1)

        self.label_37 = QLabel(self.network_frame_info)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font)

        self.gridLayout_3.addWidget(self.label_37, 3, 3, 1, 1)

        self.network_up = QLabel(self.network_frame_info)
        self.network_up.setObjectName(u"network_up")
        self.network_up.setFont(font1)

        self.gridLayout_3.addWidget(self.network_up, 1, 5, 1, 1)

        self.label_5 = QLabel(self.network_frame_info)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_3.addWidget(self.label_5, 1, 6, 1, 1)


        self.horizontalLayout_8.addWidget(self.network_frame_info)

        self.label_8 = QLabel(self.footer_frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font)

        self.horizontalLayout_8.addWidget(self.label_8, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout.addWidget(self.footer_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"System  Info", None))
        self.system_name.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.processor_name.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.system_release.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"System Info", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Machine", None))
        self.system_version.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Processor", None))
        self.system_time.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.machine_name.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"System", None))
        self.sysinfo_name.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Date", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"Version", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Release", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Time", None))
        self.timesystem.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.cpu_per.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.cpu_core.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"CPU Info", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"CPU per", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"CPU count", None))
        self.cpu_count.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_25.setText(QCoreApplication.translate("MainWindow", u"CPU Core", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Time Left", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"Plugged In", None))
        self.b_plugged.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.b_charge.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Battery", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"Status", None))
        self.b_timeleft.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Charge", None))
        self.b_status.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"Free", None))
        self.total_storage.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.used_storage.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Storage ", None))
        self.free_storage.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Used", None))
        self.free_ram.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Available", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Virtual Memory", None))
        self.available_ram.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.used_ram.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.total_ram.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Free", None))
        self.network_card.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"NetWork info", None))
        self.network_down.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u" Network", None))
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"Up", None))
        self.label_36.setText(QCoreApplication.translate("MainWindow", u" IP", None))
        self.network_ip.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Down", None))
        self.network_up.setText(QCoreApplication.translate("MainWindow", u"n/a", None))
        self.label_5.setText("")
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"For more info .. Visit www.sullinux.com", None))
    # retranslateUi

