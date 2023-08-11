from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.__status = False
        self.setupUi(self)
        self.clicker('black')
        self.power_button.clicked.connect(self.toggle_power)
        self.channel_up.clicked.connect(self.change_channel_up)
        self.channel_down.clicked.connect(self.change_channel_down)
        self.volume_up.clicked.connect(self.turn_volume_up)
        self.volume_down.clicked.connect(self.turn_volume_down)
        self.mute_button.clicked.connect(self.mute)
        self.is_tv_on = False
        self.current_channel = 1
        self.current_volume = 1
        self.volume_bar.setMinimum(0)
        self.volume_bar.setMaximum(5)

    def clicker(self, i):
        qpixmap = QPixmap(f'channel_images\\channel_{i}')
        self.label.setPixmap(qpixmap)

    def toggle_power(self):
        self.is_tv_on = not self.is_tv_on
        if self.is_tv_on:
            self.clicker(self.current_channel)
            self.power_button.setText("Power OFF")
            self.volume_bar.setValue(self.current_volume)
            self.lcdNumber.display(self.current_channel)

        else:
            self.power_button.setText("Power ON")
            self.volume_bar.setValue(0)
            self.lcdNumber.display(0)
            self.clicker("black")

    def change_channel_up(self):
        if self.is_tv_on:
            self.current_channel += 1
            self.lcdNumber.display(self.current_channel)
            self.clicker(self.current_channel)
            if self.current_channel > 3:
                self.current_channel = 1
                self.lcdNumber.display(self.current_channel)
                self.clicker(self.current_channel)

    def change_channel_down(self):
        if self.is_tv_on:
            self.current_channel -= 1
            self.lcdNumber.display(self.current_channel)
            self.clicker(self.current_channel)
            if self.current_channel == 0:
                self.current_channel = 4
                self.clicker('black')
            if self.current_channel < 1:
                self.current_channel = 4
                self.clicker(self.current_channel)

    def turn_volume_up(self):
        if self.is_tv_on:
            self.current_volume += 1
            for i in range(6):
                if self.current_volume == i:
                    self.volume_bar.setValue(i)
            if self.current_volume >= 5:
                self.current_volume = 5

    def turn_volume_down(self):
        if self.is_tv_on:
            self.current_volume -= 1
            for i in range(6):
                if self.current_volume == i:
                    self.volume_bar.setValue(i)
            if self.current_volume < 0:
                self.current_volume = 0

    def mute(self):
        if self.is_tv_on:
            self.__status = not self.__status
            if self.__status:
                self.volume_bar.setValue(0)
            else:
                self.volume_bar.setValue(self.current_volume)
        else:
            self.volume_bar.setValue(0)

