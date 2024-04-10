import sys
from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCharts import QChart, QChartView, QBarSet, QBarSeries, QBarCategoryAxis, QValueAxis
from PySide6.QtCore import Qt

class BarChartExample(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bar Chart Example with Values")

        # Dataset
        data = {
            "Mon": {"Complete": 5, "Injection": 2, "Blow": 0},
            "Tue": {"Complete": 4, "Injection": 0, "Blow": 1},
            "Wed": {"Complete": 8, "Injection": 4, "Blow": 0},
            "Thu": {"Complete": 4, "Injection": 0, "Blow": 8},
            "Fri": {"Complete": 0, "Injection": 8, "Blow": 4}
        }
        # data = {
        #     "W1": {"Entry": 5, "Issued": 2},
        #     "W2": {"Entry": 4, "Issued": 0},
        #     "W3": {"Entry": 8, "Issued": 4},
        #     "W4": {"Entry": 4, "Issued": 0},
        #     "W5": {"Entry": 0, "Issued": 8}
        # }

        # Initialize QBarSet objects
        complete_set = QBarSet("Complete")
        injection_set = QBarSet("Injection")
        blow_set = QBarSet("Blow")

        # Populate QBarSet objects with data
        for day in data:
            complete_set << data[day]["Complete"]
            injection_set << data[day]["Injection"]
            blow_set << data[day]["Blow"]

        # Create a QBarSeries and add the sets
        series = QBarSeries()
        series.append(complete_set)
        series.append(injection_set)
        series.append(blow_set)

        # Make the bar values visible
        series.setLabelsVisible(True)

        # Create a chart and add the series
        chart = QChart()
        chart.addSeries(series)
        chart.setTitle("Weekly Process Overview")
        chart.setAnimationOptions(QChart.SeriesAnimations)

        # Set up category axis for the x-axis
        categories = list(data.keys())
        axisX = QBarCategoryAxis()
        axisX.append(categories)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        # Set up value axis for the y-axis
        axisY = QValueAxis()
        max_value = max(max(d.values()) for d in data.values()) + 1  # Find the max value and add a buffer
        axisY.setRange(0, max_value)
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        # Create the chart view and set it as the central widget
        chart_view = QChartView(chart)
        self.setCentralWidget(chart_view)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BarChartExample()
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec())
