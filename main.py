import threading
import time
import traceback
import netifaces as ni
import sys
import os
from PySide2 import *
import PySide2
from PySide2extn import *
from qt_material import *
from ui_sysinfo import *
from multiprocessing import cpu_count
import shutil
import psutil
import datetime
import platform
from time import sleep
platforms = {
    'linux': 'Linux',
    'linux1': 'Linux',
    'linux2': 'Linux',
    'win32': 'Windows',
    'darwin': 'OS X'
}
class WorkerSignals(QObject):
    finished = Signal()
    error = Signal(tuple)
    result = Signal(object)
    progress = Signal(int)


class Worker(QRunnable):
    def __init__(self, fn, *args,**kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()
        self.kwargs['progress_callback'] = self.signals.progress
    @Slot()
    def run(self):
        try:
            result = self.fn(*self.args, **self.kwargs)
        except:
            traceback.print_exc()
            exctype, value = sys.exc_info()[:2]
            self.signals.error.emit((exctype,value,traceback.format_exc()))
        else:
            self.signals.result.emit(result)
        finally:
            self.signals.finished.emit()




class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.threadpool = QThreadPool()
        self.show()
        self.UI_()
        # self.battery()
        # self.ram_usage()
        self.NetWork()
        self.disks_Storage()
        self.SysInfo()
        self.Process_Activity()
        self.psutil_thread()
        self.get_ip()
        # self.speed_net()


        # apply_stylesheet(app, theme='dark_yellow.xml')
    def psutil_thread(self):
        worker = Worker(self.ram_usage)
        worker.signals.result.connect(self.print_output)
        worker.signals.finished.connect(self.thread_complete)
        worker.signals.progress.connect(self.progress_fn)
        worker.signals.progress.connect(self.speed_up_down)
        self.threadpool.start(worker)
        battery_worker = Worker(self.battery)
        battery_worker.signals.result.connect(self.speed_up_down)
        battery_worker.signals.result.connect(self.print_output)
        battery_worker.signals.finished.connect(self.thread_complete)
        battery_worker.signals.progress.connect(self.progress_fn)
        self.threadpool.start(battery_worker)

        speedUD = Worker(self.speed_net)
        speedUD.signals.result.connect(self.speed_up_down)
        speedUD.signals.result.connect(self.print_output)
        speedUD.signals.finished.connect(self.thread_complete)
        speedUD.signals.progress.connect(self.progress_fn)
        self.threadpool.start(speedUD)

    def speed_up_down(self):
        print("done")
    def print_output(self, s):
        print(s)
    def thread_complete(self):
        print("THREAD COMPLETE")
    def progress_fn(self, n):
        print("%d%% done"% n)

    def speed_net(self,progress_callback):

        count = 0
        qry = ""

        ul = 0.00
        dl = 0.00
        t0 = time.time()
        upload = psutil.net_io_counters(pernic=True)["wlp3s0"][0]
        download = psutil.net_io_counters(pernic=True)["wlp3s0"][1]
        up_down = (upload, download)

        while True:
            last_up_down = up_down
            upload = psutil.net_io_counters(pernic=True)["wlp3s0"][0]
            download = psutil.net_io_counters(pernic=True)["wlp3s0"][1]
            t1 = time.time()
            up_down = (upload, download)
            try:
                ul, dl = [
                    (now - last) / (t1 - t0) / 1024.0
                    for now, last in zip(up_down, last_up_down)
                ]
                t0 = time.time()
                # sleep(1)
            except:
                pass
            if dl > 0.1 or ul >= 0.1:
                sleep(0.75)
                # os.system("cls")
                self.ui.up.setText(str("{:0.2f} kB/s".format(ul)))
                self.ui.down.setText(str("{:0.2f} kB/s".format(dl)))
                # print("UL: {:0.2f} kB/s \n".format(ul) + "DL: {:0.2f} kB/s".format(dl))

        v = input()
    def get_ip(self):
        for nic in psutil.net_if_addrs():
            self.ui.network_name.setText(nic)
            try:
                ip = ni.ifaddresses(nic)[ni.AF_INET][0]['addr']
                if ip not in ["127.0.0.1"]:
                    self.ui.network_ip.setText(ip)
            except KeyError as err:
                pass
    def UI_(self):
        self.ui.btn_cpu.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.cpu))
        self.ui.btn_battry.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.battery))
        self.ui.btn_sensors.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sensors))
        self.ui.btn_storage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        self.ui.btn_systeminfo.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sysyeminfo))
        self.ui.btn_storage.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.storage))
        self.ui.btn_network.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.network))
        self.ui.btn_activity.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.activity))
        self.ui.btn_menu.clicked.connect(lambda: self.slideLeftMenu())
    def secs2hours(self,secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    def battery(self, progress_callback):
        while True:
            batt = psutil.sensors_battery()
            if not hasattr(psutil,"sensors_battery"):
                self.ui.battery_status.setText("Platform not supported")
            if batt is None:
                self.ui.battery_status.setText("No battery installed")
            if batt.power_plugged:
                self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
                self.ui.battery_time_left.setText("N/A")
                if batt.percent < 100:
                    self.ui.battery_status.setText("Charging")
                else:
                    self.ui.battery_status.setText("Fully Charge")
                self.ui.battery_plugged.setText("yes")
            else:
                self.ui.battery_charge.setText(str(round(batt.percent, 2))+"%")
                self.ui.battery_time_left.setText(self.secs2hours(batt.secsleft))
                if batt.percent < 100:
                    self.ui.battery_status.setText("Discharging")
                else:
                    self.ui.battery_status.setText("Fully Charged")
                self.ui.battery_plugged.setText("No")
            self.ui.battery_usage.rpb_setMaximum(100)
            self.ui.battery_usage.rpb_setValue(batt.percent)
            self.ui.battery_usage.rpb_setBarStyle('Hybrid2')
            self.ui.battery_usage.rpb_setLineColor((255, 30, 99))
            self.ui.battery_usage.rpb_setTextColor((255, 0, 0))
            self.ui.battery_usage.rpb_setInitialPos('North')
            self.ui.battery_usage.rpb_setTextFormat('Percentage')
            self.ui.battery_usage.rpb_setLineWidth(3)
            self.ui.battery_usage.rpb_setPathWidth(10)
            self.ui.battery_usage.rpb_setLineCap('RoundCap')
            ##### sleep 1 second
            sleep(1)


    def ram_usage(self,progress_callback):
        while True:
            totalRam = 1.0
            totalRam = psutil.virtual_memory()[0] * totalRam
            totalRam = totalRam /(1024*1024*1024)
            Ramm = psutil.virtual_memory()
            self.ui.total_ram.setText(str(round(psutil.virtual_memory().total/1000000000, 0)) + ' GB')
            self.ui.avaliable_ram.setText(str(round(psutil.virtual_memory().available/1000000000, 0)) + ' GB')
            self.ui.used_ram.setText(str(round(psutil.virtual_memory().used/1000000000, 0)) + ' GB')
            ramFree = 1.0
            ramFree = psutil.virtual_memory()[4]*ramFree
            ramFree = ramFree / (1024*1024*1024)
            availRam = 1.0
            availRam= psutil.virtual_memory()[1] * availRam
            availRam = availRam / (1024*1024*1024)
            UsedRam = 1.0
            UsedRam= psutil.virtual_memory()[3] * UsedRam
            UsedRam = UsedRam / (1024*1024*1024)
            self.ui.Free_ram.setText(str("{:.4f}".format(ramFree)) + ' GB')
            self.ui.cpu_count.setText(str(psutil.cpu_count()))
            self.ui.cpu_per.setText(str(psutil.cpu_percent())+' %')
            self.ui.cpu_main_core.setText(str(psutil.cpu_count(logical=False)))
            self.ui.cpu_usage.rpb_setMaximum(100)
            self.ui.cpu_usage.rpb_setMinimumSize(200,200)
            self.ui.cpu_usage.rpb_setValue(Ramm.percent)
            self.ui.cpu_usage.rpb_setDirection('Clockwise')
            colorTuple = ((0, 125, 125), (125, 0, 125), (125, 255, 0))

            self.ui.ram_usage_percent.spb_lineColor(colorTuple)
            self.ui.ram_usage_percent.spb_setMinimumSize(200,200)
            self.ui.ram_usage_percent.spb_setMinimum((0,0,0))
            self.ui.ram_usage_percent.spb_setMaximum((totalRam,totalRam,totalRam))
            self.ui.ram_usage_percent.spb_setValue((availRam,ramFree,UsedRam))
            sleep(1)

    def disks_Storage(self):

        totaldisk = psutil.disk_usage("/")
        # print(totaldisk)
        totaldiskleft = (round((totaldisk[0] - totaldisk[1]) / 1000000000, 2))
        # print(totaldiskleft)
        useddiskleft = (round((totaldisk[0] - totaldisk[2]) / 1000000000, 2))
        # print(useddiskleft)
        free_storge = totaldiskleft - useddiskleft
        # print(free_storge)
        self.ui.disktotal_size.setText(str(round(psutil.disk_usage('/').total / 1000000000, 2)) + ' GB')
        self.ui.diskused_size.setText(str(round(psutil.disk_usage('/').used / 1000000000, 2)) + ' GB')
        self.ui.diskfree_size.setText(str(round(psutil.disk_usage('/').free / 1000000000, 2, )) + ' GB')
        self.ui.storeage_disk.rpb_setMaximum(100)
        self.ui.storeage_disk.rpb_setTextColor((255, 0, 0))
        self.ui.storeage_disk.rpb_setLineColor((204, 0, 0))
        self.ui.storeage_disk.rpb_setBarStyle('Pie')
        self.ui.storeage_disk.rpb_setValue(totaldiskleft)
        self.ui.storege_used.rpb_setMaximum(100)
        self.ui.storege_used.rpb_setValue(useddiskleft)
        self.ui.storege_used.rpb_setTextColor((255, 0, 0))
        self.ui.storege_used.rpb_setLineColor((204, 0, 0))
        self.ui.storege_used.rpb_setBarStyle('Pizza')
        self.ui.storeage_free.rpb_setMaximum(100)
        self.ui.storeage_free.rpb_setValue(free_storge)
        self.ui.storeage_free.rpb_setTextColor((255, 0, 0))
        self.ui.storeage_free.rpb_setLineColor((204, 0, 0))
        self.ui.storeage_free.rpb_setBarStyle('Hybrid1')

    def SysInfo(self):
        self.ui.system_name.setText(platform.node())
        self.ui.system_sys.setText(platform.system())
        self.ui.system_machine.setText(platform.machine())
        self.ui.system_processor.setText(platform.processor())
        self.ui.system_version.setText(platform.version())
        self.ui.system_release.setText(platform.release())
        times = datetime.datetime.now().strftime("%I.%M.%S  %P")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.system_time.setText(str(times))
        self.ui.date_time.setText(str(date))

    def create_table_widget(self, rowPosition,columnPosition,text,tableName):
        qtablewidgetitem = QTableWidgetItem()
        getattr(self.ui,tableName).setItem(rowPosition,columnPosition,qtablewidgetitem)
        qtablewidgetitem = getattr(self.ui,tableName).item(rowPosition,columnPosition)
        qtablewidgetitem.setText(text);
    def NetWork(self):
        pass
    def Process_Activity(self):
        for x in psutil.pids():
            rowPosition = self.ui.tableWidget.rowCount()
            self.ui.tableWidget.insertRow(rowPosition)
            try:
                process = psutil.Process(x)
                self.create_table_widget(rowPosition,0,str(process.pid),"tableWidget")
                self.create_table_widget(rowPosition,1,str(process.name()),"tableWidget")
                self.create_table_widget(rowPosition,2,str(process.status()),"tableWidget")
                self.create_table_widget(rowPosition,3,str(datetime.datetime.utcfromtimestamp(process.create_time()).strftime('%Y-%m-%d %H:%M:%S'))
                        , "tableWidget")
                btn_suspend = QPushButton(self.ui.tableWidget)
                btn_suspend.setText("Suspend")
                btn_suspend.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition,4,btn_suspend)
                btn_resume = QPushButton(self.ui.tableWidget)
                btn_resume.setText("Resume")
                btn_resume.setStyleSheet("color: Yellow")
                self.ui.tableWidget.setCellWidget(rowPosition,5,btn_resume)
                btn_terminate = QPushButton(self.ui.tableWidget)
                btn_terminate.setText("terminate")
                btn_terminate.setStyleSheet("color: green")
                self.ui.tableWidget.setCellWidget(rowPosition,6,btn_terminate)
                btn_kill = QPushButton(self.ui.tableWidget)
                btn_kill.setText("Kill")
                btn_kill.setStyleSheet("color: red")
                self.ui.tableWidget.setCellWidget(rowPosition,7,btn_kill)
            except Exception as e:
                print(e)
        self.ui.lineEdit.textChanged.connect(self.findName)
    def findName(self):
        name = self.ui.lineEdit.text().lower()
        for row in range(self.ui.tableWidget.rowCount()):
            item = self.ui.tableWidget.item(row,1)
            self.ui.tableWidget.setRowHidden(row,name not in item.text().lower())



    def slideLeftMenu(self):
        width = self.ui.menu_frame_left.width()
        if width == 40:
            newWidth = 150
        else:
            newWidth = 40
        self.animation = QPropertyAnimation(self.ui.menu_frame_left, b"minimumWidth")
        self.animation.setDuration(200)
        self.animation.setStartValue(width)
        self.animation.setEndValue(newWidth)
        # inout = PySide2.QtCore.QEasingCurve.InOutQuart
        self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
        self.animation.start()






if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
