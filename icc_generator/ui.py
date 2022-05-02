# -*- coding: utf-8 -*-

from icc_generator import __version__


class UI(object):
    """The UI
    """
    pass


class MainWindow(QtWidgets.QMainWindow):
    """
    """

    __company_name__ = 'Erkan Ozgur Yilmaz'
    __app_name__ = 'ICC Generator'
    __version__ = __version__

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent=parent)
        self.setup_ui()

    def setup_ui(self):
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
        file_menu = self.menuBar().addMenu(self.tr(b"&File"))

        file_menu.addSeparator()

    def create_toolbars(self):
        """creates the toolbars
        """
        file_toolbar = self.addToolBar(self.tr(b"File"))
        file_toolbar.setObjectName('file_toolbar')
        create_project_action = file_toolbar.addAction('Create Project')

    def create_dock_widgets(self):
        """creates the dock widgets
        """
        pass