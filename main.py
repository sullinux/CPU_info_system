import threading
import sys
import os
from PySide2 import *
import PySide2
from PySide2extn import *
from qt_material import *
from ui_info import *
from multiprocessing import cpu_count
import psutil
import netifaces as ni
from datetime import datetime
import datetime
import time
import threading
from time import sleep

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.show()
        self.SysInfo()
        self.disks_Storage()
        self.battery()
        self.ram_usage()
        self.get_ip()
        self.speed_net()

    def speed_net(self):

        count = 0
        qry = ""

        ul = 0.00
        dl = 0.00
        t0 = time.time()
        upload = psutil.net_io_counters(pernic=True)["wlp3s0"][0]
        download = psutil.net_io_counters(pernic=True)["wlp3s0"][1]
        up_down = (upload, download)

    def get_ip(self):
        for nic in psutil.net_if_addrs():
            print(type(nic))
            self.ui.network_card.setText(nic)
            try:
                ip = ni.ifaddresses(nic)[ni.AF_INET][0]['addr']
                if ip not in ["127.0.0.1"]:
                    self.ui.network_ip.setText(ip)
            except KeyError as err:
                pass
    def ram_usage(self):

        totalRam = 1.0
        totalRam = psutil.virtual_memory()[0] * totalRam
        totalRam = totalRam /(1024*1024*1024)
        Ramm = psutil.virtual_memory()
        self.ui.total_ram.setText(str(round(psutil.virtual_memory().total/1000000000, 0)) + ' GB')
        self.ui.available_ram.setText(str(round(psutil.virtual_memory().available/1000000000, 0)) + ' GB')
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
        self.ui.free_ram.setText(str("{:.4f}".format(ramFree)) + ' GB')
        self.ui.cpu_count.setText(str(psutil.cpu_count()))
        self.ui.cpu_per.setText(str(psutil.cpu_percent())+' %')
        self.ui.cpu_core.setText(str(psutil.cpu_count(logical=False)))
        self.ui.cpu_round_progbar.rpb_setMaximum(100)
        self.ui.cpu_round_progbar.rpb_setValue(Ramm.percent)
        self.ui.cpu_round_progbar.rpb_setDirection('Clockwise')

        # self.ui.Free_ram_bar.rpb_setValue(ramFree.percent)
        # self.ui.Free_ram_bar.rpb_setDirection('Clockwise')



    def secs2hours(self,secs):
        mm, ss = divmod(secs, 60)
        hh, mm = divmod(mm, 60)
        return "%d:%02d:%02d" % (hh, mm, ss)

    def battery(self):

        batt = psutil.sensors_battery()
        if not hasattr(psutil, "sensors_battery"):
            self.ui.b_status.setText("Platform not supported")
        if batt is None:
            self.ui.b_status.setText("No battery installed")
        if batt.power_plugged:
            self.ui.b_charge.setText(str(round(batt.percent, 2)) + "%")
            self.ui.b_timeleft.setText("N/A")
            if batt.percent < 100:
                self.ui.b_status.setText("Charging")
            else:
                self.ui.b_status.setText("Fully Charge")
            self.ui.b_plugged.setText("yes")
        else:
            self.ui.b_charge.setText(str(round(batt.percent, 2)) + "%")
            self.ui.b_timeleft.setText(self.secs2hours(batt.secsleft))
            if batt.percent < 100:
                self.ui.b_status.setText("Discharging")
            else:
                self.ui.b_status.setText("Fully Charged")
            self.ui.b_plugged.setText("No")
        self.ui.battery_bar_widget.rpb_setMaximum(100)
        self.ui.battery_bar_widget.rpb_setValue(batt.percent)
        self.ui.battery_bar_widget.rpb_setBarStyle('Hybrid1')
        self.ui.battery_bar_widget.rpb_setPathWidth(2)
        self.ui.battery_bar_widget.rpb_setTextColor((102,204,0))
        self.ui.battery_bar_widget.rpb_setLineColor((102,204,0))


        # self.ui.battery_bar_widget.rpb_setLineWidth(5)
        # self.ui.battery_bar_widget.rpb_setPathWidth(1)




    def SysInfo(self):
        self.ui.sysinfo_name.setText(platform.node())
        self.ui.system_name.setText(platform.system())
        self.ui.machine_name.setText(platform.machine())
        self.ui.processor_name.setText(platform.processor())
        self.ui.system_version.setText(platform.version())
        self.ui.system_release.setText(platform.release())
        times = datetime.datetime.now().strftime("%I:%M:%S:%P")
        date = datetime.datetime.now().strftime("%Y-%m-%d")
        self.ui.timesystem.setText(str(times))
        self.ui.system_time.setText(str(date))
        # while True:
        #     times = datetime.datetime.now().strftime("%I:%M:%S:%P")
        #     date = datetime.datetime.now().strftime("%Y-%m-%d")
        #     try:
        #         self.ui.timesystem.setText(str(times))
        #         self.ui.system_time.setText(str(date))
        #         # time.sleep(0.75)
        #         QApplication.processEvents()
        #     except Exception as e:
        #         print(e)
    def disks_Storage(self):
        totaldisk = psutil.disk_usage("/")
        totaldiskleft = (round((totaldisk[0]-totaldisk[1]) /1000000000,2))
        useddiskleft = (round((totaldisk[0]-totaldisk[2]) /1000000000,2))
        freestorage = psutil.disk_usage('/').free /1000000000
        freestorage= round(freestorage,2)
        total_size = totaldiskleft - useddiskleft
        self.ui.total_storage.setText(str(round(psutil.disk_usage('/').total / 1000000000, 2))+' GB')
        self.ui.used_storage.setText(str(round(psutil.disk_usage('/').used / 1000000000, 2))+' GB')
        self.ui.free_storage.setText(str(round(psutil.disk_usage('/').free / 1000000000, 2, ))+' GB')
        self.ui.totalstorage_bar.rpb_setMaximum(100)
        self.ui.totalstorage_bar.rpb_setTextColor((255,0,0))
        self.ui.totalstorage_bar.rpb_setLineColor((204,0,0))
        self.ui.totalstorage_bar.rpb_setBarStyle('Pie')
        self.ui.totalstorage_bar.rpb_setValue(total_size)
        self.ui.totalstorage_bar.rpb_setDirection('Clockwise')
        self.ui.used_storage_bar.rpb_setMaximum(100)
        self.ui.used_storage_bar.rpb_setValue(useddiskleft)
        self.ui.used_storage_bar.rpb_setTextColor((255,0,0))
        self.ui.used_storage_bar.rpb_setLineColor((204,0,0))
        self.ui.used_storage_bar.rpb_setBarStyle('Pizza')
        self.ui.Free_storage_bar.rpb_setMaximum(100)
        self.ui.Free_storage_bar.rpb_setValue(freestorage)
        self.ui.Free_storage_bar.rpb_setDirection('Clockwise')
        self.ui.Free_storage_bar.rpb_setTextColor((255,0,0))
        self.ui.Free_storage_bar.rpb_setLineColor((204,0,0))
        self.ui.Free_storage_bar.rpb_setBarStyle('Hybrid1')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
