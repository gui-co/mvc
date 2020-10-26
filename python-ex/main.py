import sys

from qtpy.QtWidgets import QApplication

from View import View


qApp = QApplication(sys.argv)
v = View()
v.show()
qApp.exec_()

