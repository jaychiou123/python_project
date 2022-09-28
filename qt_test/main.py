import sys
from PyQt5.QtWidgets import *  # QApplication, QWidget, QLabel
from test import Ui_MainWindow
from PyQt5.QtCore import *

import numpy as np
import pyrealsense2 as rs
import time
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas, \
    NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# matplotlib.use('QT5Agg')
# matplotlib.rcParams["axes.unicode_minus"] = False  # 正常顯示負號用


class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        self.axes.autoscale(True)
        super(MplCanvas, self).__init__(fig)


class Analysis():
    def __init__(self):
        fig, self.axes = plt.subplots(nrows=2, sharex=False, figsize=(6, 6), dpi=200)
        fig.subplots_adjust(hspace=0.3)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.updateTime = 0
        self.color = "k"
        self.stop_draw = False
        self.resume = False
        self.normalize_flag = False
        self.gravity_got = False
        self.stop_plot_time = 0
        self.resume_time = 0
        self.stopped_data = []
        self.record_data = []
        self.still_data = []
        self.record_flag = False
        self.record_time = 0
        self.stop_record_time = 0
        self.gravity = 0
        self.record_duration = 0
        self.t_record_segment = []

        ### window setting ###
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle("My Window~~~")
        self.resize(1000, 800)

        ### canvas ###
        self.sc = MplCanvas(self, width=5, height=4, dpi=100)
        self.ui.gridLayout.addWidget(self.sc, 2, 1, 1, 1)

        ### toolbar ###
        self.toolbar = NavigationToolbar(self.sc, self)
        self.ui.gridLayout.addWidget(self.toolbar, 3, 1, 1, 1)

        ### data retrieve ###
        self.fps = 100
        self.pipeline = rs.pipeline()
        self.config = rs.config()
        self.config.enable_stream(rs.stream.accel, rs.format.motion_xyz32f, self.fps)  # acceleration
        self.pipeline.start(self.config)
        self.motion_data = []
        self.timer = None
        self.plot_animation()

        ### Pushbutton
        self.ui.pushButton_2.setText("Record")
        self.ui.pushButton_2.clicked.connect(self.record)
        self.ui.pushButton.setText("Stop record")
        self.ui.pushButton.clicked.connect(self.stop_record)
        self.ui.pushButton_1.setText("Export")
        self.ui.pushButton_1.clicked.connect(self.export_csv)
        self.ui.pushButton_3.setText("Stop")
        self.ui.pushButton_3.clicked.connect(self.stop_plot)
        self.ui.pushButton_4.setText("Resume")
        self.ui.pushButton_4.clicked.connect(self.resume_record)
        self.ui.pushButton_5.setText("Normalize")
        self.ui.pushButton_5.clicked.connect(self.normal_trigger)

    def record(self):
        self.color = "r"
        self.record_flag = True
        self.record_time = self.updateTime
        self.ui.pushButton.setEnabled(True)

    def stop_record(self):
        self.color = "k"
        self.record_flag = False
        self.stop_record_time = self.updateTime
        self.ui.pushButton.setEnabled(False)

        ### time elapsed ###
        self.record_duration = self.stop_record_time - self.record_time + 1
        self.t_record_segment = np.linspace(self.record_time, self.stop_record_time, self.record_duration)

        ### create fig and draw analysis ###
        self.new_fig = Analysis()
        self.analysis_time()
        self.analysis_freq()

    def analysis_time(self):
        ### rms ###
        rms = np.sqrt(np.mean(np.array(self.record_data[-self.record_duration:]) ** 2))
        rms_data = np.full(self.record_duration, rms)

        ### axis params ###
        bottom, top = self.new_fig.axes[0].get_ylim()
        self.new_fig.axes[0].set_title("Vibration Analysis", fontsize=10, fontweight="bold")
        self.new_fig.axes[0].set_xlabel("Time[sec]", fontsize=8)
        self.new_fig.axes[0].set_ylabel("Amplitude[m/s^2]", fontsize=8)
        self.new_fig.axes[0].set_ylim(np.min(self.record_data), np.max(self.record_data))
        self.new_fig.axes[0].tick_params(axis='both', which='major', labelsize=5)
        self.new_fig.axes[0].annotate(f'{round(rms,4)}\n RMS', xy=(1, (rms-bottom)/(top - bottom) - 0.1),
                                      xycoords='axes fraction', fontsize=8, color="r",
                                      horizontalalignment='left', verticalalignment='bottom')
        self.new_fig.axes[0].plot(self.t_record_segment, self.record_data[-self.record_duration:], "k", self.t_record_segment, rms_data, "r")

    def analysis_freq(self):
        ### frequency domain ###
        N = len(self.record_data)
        T = 0.01
        x = np.linspace(0, N*T, N)
        yf = np.fft.fft(self.record_data)
        xf = np.linspace(0, 1/2/T, N//2)
        self.new_fig.axes[1].plot(xf, 2/N*abs(yf[:N//2]), "b")

        # ### axis params ###
        self.new_fig.axes[1].tick_params(axis='both', which='major', labelsize=5)
        self.new_fig.axes[1].set_xlabel("Frequency[Hz]", fontsize=8)
        self.new_fig.axes[1].set_ylabel("Amplitude[m/s^2]", fontsize=8)

        plt.show()

    def export_csv(self):
        pass

    def normal_trigger(self):
        self.normalize_flag = True
        timer = QTimer(self)
        timer.setSingleShot(True)
        timer.timeout.connect(self.subtract_g)
        timer.start(5000)

    def subtract_g(self):
        self.normalize_flag = False
        self.gravity = np.mean(self.still_data)
        self.gravity_got = True

    def stop_plot(self):
        self.stop_plot_time = self.updateTime
        self.stop_draw = True
        self.ui.pushButton_3.setEnabled(False)

    def resume_record(self):
        self.stop_draw = False
        self.resume_time = self.updateTime
        self.resume = True
        self.ui.pushButton_3.setEnabled(True)

    def plot_animation(self):
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update_animation)
        self.timer.start(50)

    def update_animation(self):
        data = []
        shift = 5
        if self.gravity_got:
            self.sc.axes.cla()
            time.sleep(0.1)
            self.gravity_got = False

        ### data to be drawn ###
        self.plotdata = np.array(self.motion_data[-shift:])
        self.xdata = np.linspace(self.updateTime, self.updateTime + 5, shift)

        ### label ###
        self.sc.axes.set_xlabel("Time[sec]", fontsize=12)
        self.sc.axes.set_ylabel("Amplitude[m/s^2]", fontsize=12)
        self.sc.axes.set_xlim(xmin=self.updateTime - 400, xmax=self.updateTime + 5)

        if not self.stop_draw:
            if self.resume:                                     ### resume ###
                total_time = self.resume_time - self.stop_plot_time + 1
                time_elapse = np.linspace(self.stop_plot_time, self.resume_time, total_time)
                self.sc.axes.plot(time_elapse, self.stopped_data[-total_time:], self.color)
                self.resume = not self.resume
            else:                                              ### normal situation ###
                self.sc.axes.plot(self.xdata, self.plotdata, self.color)
            self.sc.draw()
        self.updateTime = self.updateTime + 5

    def grab_data(self):
        while 1:
            frames = self.pipeline.wait_for_frames()
            for frame in frames:
                if self.stop_draw:
                    self.stopped_data.append(frame.as_motion_frame().get_motion_data().z - self.gravity)
                if self.record_flag:
                    self.record_data.append(frame.as_motion_frame().get_motion_data().z - self.gravity)
                if self.normalize_flag:
                    self.still_data.append(frame.as_motion_frame().get_motion_data().z)
                self.motion_data.append(frame.as_motion_frame().get_motion_data().z - self.gravity)
                # print(len(self.record_data))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    thread_data = QThread()
    thread_data.run = w.grab_data
    thread_data.start()
    w.show()
    # w.stop_plot()
    sys.exit(app.exec_())
