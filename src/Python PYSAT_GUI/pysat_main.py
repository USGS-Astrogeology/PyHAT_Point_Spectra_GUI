from PyQt4.QtGui import *
from PyQt4.QtCore import *
import sys, time
from pysat_ui import *


class Main(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self, parent)
        self.runningFunctions(self)
        self.org_name = "USGS"
        self.app_name = "PYSAT"

    def closeEvent(self):
        self.saveworkflow()

    def runningFunctions(self, MainWindow):
        pysat = pysat_ui()
        pysat.mainframe(MainWindow)  # Set up the mainwindow. This is the backbone of the UI it IS REQUIRED
        pysat.menu_item_shortcuts()  # The shortcuts for making things happen in the UI
        pysat.menu_item_functions(MainWindow)  # These are the various functions that make the UI work

        #### These are the triggers for exit and new
        pysat.actionExit.triggered.connect(lambda: self.exit())  # Exit out of the current workflow
        pysat.actionCreate_New_Workflow.triggered.connect(lambda: self.new())  # Create a new window. It will be blank
        pysat.actionOpen_Workflow.triggered.connect(lambda: self.openworkflow())  # trigger the loading of workflow.
        pysat.actionSave_Current_Workflow.triggered.connect(lambda: self.closeEvent())

    def openworkflow(self):
        settings = QtCore.QSettings(self.org_name, self.app_name)
        main_window.restoreGeometry(settings.value('geometry'))
        main_window.restoreState(settings.value('state'))
        main_window._ui.dockWin.setFloating(settings.value('dockWin/isFloating') == 'true')

    def saveworkflow(self):
        settings = QtCore.QSettings(self.org_name, self.app_name)
        is_floating = main_window._ui.dockWin.isFloating()
        settings.setValue('dockWin/isFloating', is_floating)
        main_window._ui.dockWin.setFloating(True)
        settings.setValue('geometry', main_window.saveGeometry())
        settings.setValue('state', main_window.saveState())



    def new(self):
        # TODO create a new window to work in. The old window does not disappear
        window = Main(self)
        window.show()

    def exit(self):
        # TODO close the current window
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash_pix = QPixmap('splash.png')
    splash = QSplashScreen(splash_pix, Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    time.sleep(1)
    app.processEvents()

    main_window = Main()
    main_window.show()
    splash.finish(main_window)
    app.exec_()
