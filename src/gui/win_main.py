from models.list_model import ListModel
from win_main_ui import Ui_MainWindow
from PySide6.QtWidgets import QMainWindow, QWidget

class WinMain(QMainWindow):
    """
    Main Window class for the To-Do application.

    This class:
    - Initializes the UI from the Qt Designer-generated Ui_MainWindow
    - Creates a custom ListModel to manage tasks
    - Populates the model with initial tasks
    - Connects the model to the QListView in the UI
    """

    def __init__(self, aParent: QWidget = None):
        """
        Initialize the main window.
        
        :param aParent: Optional parent QWidget
        """
        super().__init__(aParent)

        # Initialize the UI (setup all widgets, layouts, signals, etc.)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Create an instance of the custom ListModel
        # This model will hold the list of tasks and expose them to the QListView
        self.model = ListModel(self)

        # Set the model for the QListView in the UI
        # This tells the QListView where to get the data from
        self.ui.listView.setModel(self.model)

        # Sample list of tasks to populate the model initially
        # Each task is a dictionary with:
        #   "name" → the text of the task
        #   "done" → whether the task is completed (True/False)
        tasks = [
            {"name": "Do any this", "done": False},
            {"name": "Do any this", "done": False},
            {"name": "Do any this", "done": False},
            {"name": "Do any this", "done": False},
            {"name": "Do any this", "done": True}  # Completed task
        ]

        # Populate the ListModel with the initial tasks
        # buildModel() will reset the model and notify the QListView to update
        self.model.buildModel(tasks)
