from PySide6.QtCore import (
    QAbstractListModel, 
    QModelIndex, 
    QObject,
    Qt

)

class ListModel( QAbstractListModel ):
    __mList = []

    def __init__(self, aParent: QObject = None ):
        super().__init__( aParent )
        self.__mList = []



    def rowCount( self, aParent: QModelIndex = QModelIndex()):
        # if not aParent.isValid(): return 0

        return len(self.__mList)
    
    def data( self, aIndex: QModelIndex, aRole: int ):
        if not aIndex.isValid(): return None

        item = self.__mList[aIndex.row()]
        if Qt.ItemDataRole.DisplayRole == aRole:
            return item["name"]
        
        if Qt.ItemDataRole.CheckStateRole == aRole:
            return Qt.CheckState.Checked \
                if item["done"] else Qt.CheckState.Unchecked
    
    def setData( self, aIndex: QModelIndex, aValue: dict, aRole: int ):
        if not aIndex.isValid(): return False

        item = self.__mList[aIndex.row()]
        
        if Qt.ItemDataRole.DisplayRole == aRole:
            item["name"] = aValue["name"]
            self.dataChanged.emit( aIndex, aIndex, aRole )
            return True
        
        if Qt.ItemDataRole.CheckStateRole == aRole:
            print( "Here ")
            print( aValue, Qt.CheckState.Checked.value )
            item["done"] = aValue == Qt.CheckState.Checked.value
            self.dataChanged.emit( aIndex, aIndex, aRole )
            # self.dataChanged.emit()
            return True
        
        return False
        
    def flags(self, aIndex: QModelIndex):
        return (
            Qt.ItemIsEnabled
            | Qt.ItemIsSelectable
            | Qt.ItemIsEditable
            | Qt.ItemIsUserCheckable
        )

    def buildModel( self, aTasks: list[dict] ):
        self.beginResetModel()
        self.__mList = aTasks
        self.endResetModel()

    def addTask( self, aTask: dict ):
        self.beginInsertRows( QModelIndex(), len( self.__mList), len(self.__mList))
        self.__mList.append( aTask )
        self.endInsertRows()

    




