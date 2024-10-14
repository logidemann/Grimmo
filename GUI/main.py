from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from main_application import main_application

app = QApplication(sys.argv)

window = main_application()

window.show()
app.exec()