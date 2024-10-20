from PySide6.QtWidgets import  QMainWindow
from PySide6.QtGui import QIcon, QAction


class XMainWindow(QMainWindow):
    """
    基本UI类，用于分离UI代码和业务代码
    
    函数均以 x 为前缀，用于和 Qt 的函数区分
    """
    def __init__(self):
        super().__init__()
        self.xInitUI()
        
    def xInitUI(self):
        """
        自定义UI初始化, 用于子类重写
        
        该函数仅用于调用其他函数，不应该包含任何具体的UI代码
        """
        self.xInitWindow()
        self.xInitStatusBar()
        self.xInitMenuBar()
        
    def xInitStatusBar(self):
        """
        初始化状态栏
        """
        self.statusBar().showMessage("Ready")
    
    def xInitMenuBar(self):
        """
        初始化菜单栏
        """
        # exitAct = QAction(QIcon("exit.png"), "&Exit", self)
        # exitAct.setShortcut("Ctrl+Q")
        # exitAct.setStatusTip("Exit application")
        # exitAct.triggered.connect(QApplication.instance().quit)

        menubar = self.menuBar()
        # fileMenu = menubar.addMenu("&File")
        # fileMenu.addAction(exitAct)
        
    def xInitWindow(self):
        """
        初始化窗口
        """
        self.setGeometry(300, 300, 350, 250)
        self.setWindowTitle("Simple menu")
        self.show()
