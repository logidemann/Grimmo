from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from agenda_responsable import agenda_responsable

app = QApplication(sys.argv)

window = agenda_responsable()

window.show()
app.exec()