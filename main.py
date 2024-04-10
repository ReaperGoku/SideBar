from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys

class MySideBar(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("SideBar Menu")

        self.icon_name_widget.setHidden(True)

        self.dashboard_1.clicked.connect(self.swich_to_dashboardPage)
        self.dashboard_2.clicked.connect(self.swich_to_dashboardPage)

    def swich_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)

    def swich_to_dashboardPage(self):
        self.stackedWidget.setCurrentIndex(0)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = MySideBar()
    sys.exit(app.exec())