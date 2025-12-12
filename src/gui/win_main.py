from models.list_model import ListModel

from win_main_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget

class WinMain( QMainWindow ):
    def __init__( self, aParent: QWidget = None ):
        super().__init__( aParent )

        self.ui = Ui_MainWindow()
        self.ui.setupUi( self )

        self.model = ListModel( self )
        self.ui.listView.setModel( self.model )

        tasks = [
            {
                "name": "Do any this",
                "done": False
            },
            {
                "name": "Do any this",
                "done": False
            },
            {
                "name": "Do any this",
                "done": False
            },
            {
                "name": "Do any this",
                "done": False
            },
            {
                "name": "Do any this",
                "done": True
            }
        ]

        self.model.buildModel( tasks )



