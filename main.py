import sys
import PySide6.QtCore
from PySide6.QtWidgets import QApplication

from modules import ui
from modules.ui.network_monitor.network_monitor import NetworkMonitorUI


# Prints PySide6 version
print(PySide6.__version__)

# Prints the Qt version used to compile PySide6
print(PySide6.QtCore.__version__)

def main():
    app = QApplication(sys.argv)
    window = ui.NetworkMonitorUI()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
