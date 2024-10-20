from PySide6 import QtWidgets
from PySide6.QtGui import QIcon, QAction


class NetworkSpeed(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.network_speed = 0
        self.xInitUI()

    def xInitUI(self):
        layout = QtWidgets.QHBoxLayout(self)
        self.name = QtWidgets.QLabel("Network Speed", self)
        self.data = QtWidgets.QTextEdit(self.set_speed(self.network_speed), self)
        self.button = QtWidgets.QPushButton("Refresh", self)
        self.button.clicked.connect(self.button_clicked)
        layout.addWidget(self.name)
        layout.addWidget(self.data)
        layout.addWidget(self.button)
        self.setLayout(layout)

    def set_speed(self, speed: float, unit="KB/s"):
        return f"{speed:.2f} {unit}"

    def set_data(self, data):
        self.data.setText(self.set_speed(data))

    def button_clicked(self):
        self.network_speed += 1
        if self.network_speed > 10:
            self.network_speed = 0
        self.set_data(self.network_speed)


class NetworkMonitorUI(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.xInitUI()

    def xInitUI(self):
        layout = QtWidgets.QHBoxLayout(self)
        self.net_speed = NetworkSpeed()
        layout.addWidget(self.net_speed)
        self.setLayout(layout)
