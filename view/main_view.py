from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtCore import pyqtSlot
from view.main_view_ui import Ui_MainWindow


class MainView(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

