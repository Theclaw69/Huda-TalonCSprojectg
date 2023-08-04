from PyQt6.QtWidgets import *
from gui import *


class Logic(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        
        self.power_button.clicked.connect(self.toggle_power)
        self.channel_up.clicked.connect(self.change_channel_up)
        self.channel_down.clicked.connect(self.change_channel_down)

        self.is_tv_on = False
        self.current_channel = 1

    def toggle_power(self):
        self.is_tv_on = not self.is_tv_on
        if self.is_tv_on:
            self.power_button.setText("Power OFF")
        else:
            self.power_button.setText("Power ON")

    def change_channel_up(self):
        if self.is_tv_on:
            self.current_channel += 1
            self.label.setText("Channel: " + str(self.current_channel))

    def change_channel_down(self):
        if self.is_tv_on:
            self.current_channel -= 1
            if self.current_channel < 1:
                self.current_channel = 1
            self.label.setText("Channel: " + str(self.current_channel))
