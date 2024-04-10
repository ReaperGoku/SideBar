# PieChart.py
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCharts import QChart, QChartView, QPieSeries
from PySide6.QtGui import QPainter
from PySide6.QtCore import Qt
# main.py
import sys
from PySide6.QtWidgets import QApplication, QMainWindow
# from PieChart import PieChartWidget

class PieChartWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Create a pie series
        series = QPieSeries()
        series.append("Complete", 12)
        series.append("Injection", 8)
        series.append("Blow", 17)

        # Creating the chart
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Process Overview")
        chart.legend().setVisible(True)
        chart.legend().setAlignment(Qt.AlignBottom)

        # Create a chart view
        chart_view = QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)  # For smooth rendering

        # Create a layout
        layout = QVBoxLayout()
        layout.addWidget(chart_view)

        # Set the layout to the QWidget
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Pie Chart Example with PySide6")
        # Initialize the PieChartWidget and set it as the central widget
        self.setCentralWidget(PieChartWidget())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.resize(400, 300)
    mainWindow.show()
    sys.exit(app.exec())
