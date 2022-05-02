# -*- coding: utf-8 -*-
import sys

import icc_generator
from PySide2 import QtCore, QtGui, QtWidgets


def ui_caller(app_in, executor, ui_class, **kwargs):
    global app
    global ui_instance
    self_quit = False
    try:
        app = QtWidgets.QApplication.instance()
    except TypeError:
        app = None
    if app is None:
        if not app_in:
            try:
                app = QtWidgets.QApplication(sys.argv)
            except (TypeError, AttributeError):  # sys.argv gives argv.error or
                                                 # Qt gives TypeError
                app = QtWidgets.QApplication([])
        else:
            app = app_in
        self_quit = True

    ui_instance = ui_class(**kwargs)
    ui_instance.show()
    if executor is None:
        app.exec_()
        if self_quit:
            app.connect(
                app,
                QtCore.SIGNAL("lastWindowClosed()"),
                app,
                QtCore.SLOT("quit()")
            )
    else:
        executor.exec_(app, ui_instance)
    return ui_instance


class MainWindow(QtWidgets.QMainWindow):
    """The main window
    """

    __company_name__ = 'Erkan Ozgur Yilmaz'
    __app_name__ = 'ICC Generator'
    __version__ = icc_generator.__version__

    def __init__(self, parent=None, *args, **kwargs):
        super(MainWindow, self).__init__(parent=parent, *args, **kwargs)

        self.central_widget = None
        self.open_action = None
        self.save_action = None
        self.save_as_action = None
        self.create_icc_profile_tab_widget = None

        self.settings = QtCore.QSettings(
            self.__company_name__,
            self.__app_name__
        )
        self.setup_ui()

    def setup_ui(self):
        """creates the UI widgets
        """
        self.setWindowTitle("%s v%s" % (self.__app_name__, self.__version__))

        self.create_main_menu()
        self.create_toolbars()
        self.create_dock_widgets()

        self.read_settings()

    def write_settings(self):
        """stores the settings to persistent storage
        """
        self.settings.beginGroup("MainWindow")

        self.settings.setValue("size", self.size())
        self.settings.setValue("pos", self.pos())
        self.settings.setValue("windowState", self.saveState())

        self.settings.endGroup()

    def read_settings(self):
        """read settings from persistent storage
        """
        self.settings.beginGroup('MainWindow')

        self.resize(self.settings.value('size', QtCore.QSize(800, 600)))
        self.move(self.settings.value('pos', QtCore.QPoint(100, 100)))
        self.restoreState(self.settings.value('windowState'))

        self.settings.endGroup()

    def reset_window_state(self):
        """reset window states
        """
        self.project_dock_widget.setVisible(True)

    def create_main_menu(self):
        """creates the main application menu
        """
        file_menu = self.menuBar().addMenu(self.tr("&File"))

        self.open_action = file_menu.addAction("&Open...")
        self.save_action = file_menu.addAction("&Save")
        self.save_as_action = file_menu.addAction("&Save As")

    def create_toolbars(self):
        """creates the toolbars
        """
        file_toolbar = self.addToolBar(self.tr("File"))
        file_toolbar.setObjectName('file_toolbar')
        open_action = file_toolbar.addAction('Create Project')

        # Create signals
        # QtCore.QObject.connect(
        #     open_action,
        #     QtCore.SIGNAL('triggered()'),
        #     self.create_project_action_clicked
        # )

    def create_dock_widgets(self):
        """creates the dock widgets
        """
        # ----------------------------------------
        # create the Project Dock Widget

        # ----------------------------------------
        # create the Central Widget
        self.central_widget = ICCProfileTabWidget(parent=self)
        self.setCentralWidget(self.central_widget)

    def show_and_raise(self):
        """
        """
        self.show()
        self.raise_()

    def closeEvent(self, event):
        """The overridden close event
        """
        self.write_settings()
        event.accept()


class ICCProfileTabWidget(QtWidgets.QTabWidget):
    """contains the widgets to create a new ICC profile
    """

    def __init__(self, *args, **kwargs):
        super(ICCProfileTabWidget, self).__init__(*args, **kwargs)
        self.create_icc_profile_tab = None
        self.color_correct_image_tab = None
        self.setup_ui()

    def setup_ui(self):
        """sets the ui up
        """
        self.create_icc_profile_tab = QtWidgets.QWidget(self)
        self.color_correct_image_tab = QtWidgets.QWidget(self)
        self.addTab(self.create_icc_profile_tab, "Create ICC Profile")
        self.addTab(self.color_correct_image_tab, "Color Correct Image")


if __name__ == "__main__":
    ui_caller(None, None, MainWindow)
