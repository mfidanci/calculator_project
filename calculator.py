import sys

from PyQt6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setObjectName("light")    # Default theme

        self.initializeUI()     # Set up UI components

    def initializeUI(self):
        self.setWindowTitle("Calculator")
        self.setGeometry(100, 100, 400, 500)  # Set the initial position and size
        self.setMinimumSize(400, 500)
        self.setMaximumSize(600, 700)

        # Create a central widget and set it as the central widget
        self.container = QWidget()
        self.setCentralWidget(self.container)

        # Create a QVBoxLayout and set it for the container
        self.layout = QVBoxLayout()
        self.container.setLayout(self.layout)


app = QApplication(sys.argv)
window = CalculatorApp()
window.show()
sys.exit(app.exec())


