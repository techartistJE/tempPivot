from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class TempPivotUI(QWidget):
    def __init__(self):
        super(TempPivotUI, self).__init__()
        self.setObjectName('TempPivotUI')
        self.initUI()

        self.spaceButtonsDict ={}
    
    def initUI(self):
        self.setWindowTitle('Temp Pivot')
        self.setGeometry(300, 300, 300, 200)
        self.createUI()

    def createUI(self):
        """UI 생성"""
        self.mainLayout = QVBoxLayout()
        self.setLayout(self.mainLayout)

        # radio button ( object, world space)
        self.radioLayout = QHBoxLayout()
        self.worldSpace_radio = QRadioButton('World Space')
        self.objSpace_radio = QRadioButton('Object Space')
        self.worldSpace_radio.setChecked(True)
        self.radioLayout.addWidget(self.worldSpace_radio)
        self.radioLayout.addWidget(self.objSpace_radio)
        
        #self.getMatrix_btn = QPushButton('Get Matrix')
        self.color_btn = QPushButton('Color')
        self.color_btn.setStyleSheet('font-weight: bold; font-size: 11px; color: white;')
        self.createPivot_btn = QPushButton('Create PivotLoc')
        # set orange color and bold text and font size 12 font color white
        self.createPivot_btn.setStyleSheet('background-color: orange; font-weight: bold; font-size: 14px; color: white')
        self.pivotLocTable = QTableWidget()
        self.pivotLocTable.setColumnCount(3)
        # column 0 pivotLoc name
        # column 1 target name
        self.pivotLocTable.setHorizontalHeaderLabels(['PivotLoc', 'Target','Space'])
        self.pivotLocTable.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.pivotLocTable.verticalHeader().setVisible(False)
        # multi selection and row selection
        self.pivotLocTable.setSelectionMode(QAbstractItemView.MultiSelection)
        self.pivotLocTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.pivotLocTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        
        # manage pivotLoc buttons
        self.editMode_btn = QPushButton('Edit Mode Off')
        self.editMode_btn.setStyleSheet('background-color: rgb(93,93,93,255); font-weight: plain;' )
        #self.pivotBtn_layout = QHBoxLayout()
        self.connect_btn = QPushButton('Temp Pivot Off')
        #self.matrix_reset_btn = QPushButton('Reset Matrix')
        #self.pivotBtn_layout.addWidget(self.connect_btn)
        #self.pivotBtn_layout.addWidget(self.matrix_reset_btn)

        self.animKey_btn = QPushButton('Anim Key')

        self.mainLayout.addLayout(self.radioLayout)
        self.mainLayout.addWidget(self.color_btn)
        self.mainLayout.addWidget(self.createPivot_btn)
        self.mainLayout.addWidget(self.pivotLocTable)
        self.mainLayout.addWidget(self.editMode_btn)
        self.mainLayout.addWidget(self.connect_btn)
        #self.mainLayout.addLayout(self.pivotBtn_layout)
        self.mainLayout.addWidget(self.animKey_btn)

    def updateSpaceButtons(self, target):
        buttonUI = self.spaceButtonsDict[target]
        if buttonUI.text() == 'World':
            buttonUI.setText('Object')
        else:
            buttonUI.setText('World')
        
    def editModeOnOff(self):
        currentText = self.editMode_btn.text()
        if currentText == 'Edit Mode Off':
            self.editMode_btn.setText('Edit Mode On')
            self.editMode_btn.setStyleSheet('background-color: red; font-weight: bold;' )
            for button in self.spaceButtonsDict.values():
                button.enabled = True
        else:
            self.editMode_btn.setText('Edit Mode Off') 
            # font weight: plain
            self.editMode_btn.setStyleSheet('background-color: rgb(93,93,93,255); font-weight: plain;' )
            for button in self.spaceButtonsDict.values():
                # can't click
                button.enabled = False
    def tempPivotOnOff(self):
        currentText = self.connect_btn.text()
        if currentText == 'Temp Pivot Off':
            self.connect_btn.setText('Temp Pivot On')
            self.connect_btn.setStyleSheet('background-color: green; font-weight: bold;' )
           
        else:
            self.connect_btn.setText('Temp Pivot Off') 
            # font weight: plain
            self.connect_btn.setStyleSheet('background-color: rgb(93,93,93,255); font-weight: plain;' )
            
    def getSelectedData(self, colID=0):
        """선택된 row와 column의 데이터를 반환"""
        selectedItems = self.pivotLocTable.selectedItems()
        selectedData = []
        
        for item in selectedItems:
            row = item.row()
            col = item.column()
            if col == colID:
                selectedData.append(item.text())
        return selectedData
        
