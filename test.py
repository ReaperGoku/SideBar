import sys
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt

class MoldStatusWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        grid = QGridLayout()

        # Set the font for the titles
        title_font = QFont()
        title_font.setPointSize(16)
        title_font.setBold(True)

        # Set the font for the values
        value_font = QFont()
        value_font.setPointSize(14)

        # Title
        title = QLabel("New & WIP Mold's")
        title.setFont(title_font)
        title.setAlignment(Qt.AlignCenter)
        grid.addWidget(title, 0, 0, 1, 2)

        # Create labels for the stats
        labels = ["Total", "Complete", "Injection", "Blow"]
        for i, label_text in enumerate(labels):
            label = QLabel(f"34\n{label_text}")
            label.setAlignment(Qt.AlignCenter)
            label.setFont(value_font)
            label.setStyleSheet("background-color: #3498db; color: white; padding: 15px; border-radius: 10px;")
            grid.addWidget(label, i + 1, 0)

        # Create labels for the details
        details_text = (
            "Hot Runner : 20\n"
            "HQ Change Note : 10\n"
            "AI Change Note : 10\n"
            "POS Revision : 12\n"
            "New Entry : 12\n"
            "HQ In-charge : 3\n"
            "Translation : 12"
        )

        details_label = QLabel(details_text)
        details_label.setAlignment(Qt.AlignCenter | Qt.AlignTop)
        details_label.setFont(value_font)
        details_label.setStyleSheet("background-color: #3498db; color: white; padding: 15px; border-radius: 10px;")
        grid.addWidget(details_label, 1, 1, 6, 1)  # Span across 6 rows

        self.setLayout(grid)
        self.setWindowTitle('Mold Status')
        self.setStyleSheet("background-color: #ecf0f1;")
        self.resize(300, 400)

# Run the application
app = QApplication(sys.argv)
window = MoldStatusWindow()
window.show()
sys.exit(app.exec_())
