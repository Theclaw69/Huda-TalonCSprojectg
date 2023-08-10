import os
from PyQt6.QtWidgets import *
from PyQt6.QtGui import QPixmap
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.power_button.clicked.connect(self.toggle_power)
        self.channel_up.clicked.connect(self.change_channel_up)
        self.channel_down.clicked.connect(self.change_channel_down)
        self.volume_up.clicked.connect(self.turn_volume_up)
        self.volume_down.clicked.connect(self.turn_volume_down)
        self.is_tv_on = False
        self.current_channel = 1
        self.current_volume = 1
        self.volume_bar.setMinimum(0)
        self.volume_bar.setMaximum(5)

        self.channel_images = self.load_channel_images()
        self.update_channel_image()




    def load_channel_images(self):
        channel_images = {}
        for i in range(1, 4):
            file_path = os.path.join("channel_images", f"channel_{i}.png")
            if os.path.exists(file_path):
                channel_images[i] = QPixmap(file_path)
        return channel_images

    def update_channel_image(self):
        if self.is_tv_on and self.current_channel in self.channel_images:
            pixmap = self.channel_images[self.current_channel]
            self.graphicsView.setScene(QtWidgets.QGraphicsScene())
            self.graphicsView.scene().addPixmap(pixmap)
            self.graphicsView.fitInView(pixmap.rect(), QtCore.Qt.AspectRatioMode.KeepAspectRatio)

    def toggle_power(self):
        self.is_tv_on = not self.is_tv_on
        if self.is_tv_on:
            self.power_button.setText("Power OFF")
            self.update_channel_image()
            self.volume_bar.setValue(self.current_volume)
            self.lcdNumber.display(self.current_channel)

        else:
            self.power_button.setText("Power ON")
            self.graphicsView.setScene(QtWidgets.QGraphicsScene())
            self.volume_bar.setValue(0)
            self.lcdNumber.display(0)

    def change_channel_up(self):
        if self.is_tv_on:
            self.current_channel += 1
            self.lcdNumber.display(self.current_channel)
            if self.current_channel > 3:
                self.current_channel = 1
                self.lcdNumber.display(self.current_channel)
            self.update_channel_image()

    def change_channel_down(self):
        if self.is_tv_on:
            self.current_channel -= 1
            self.lcdNumber.display(self.current_channel)
            if self.current_channel < 2:
                self.current_channel = 4
        self.update_channel_image()

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



