from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class tempPivot_UI(QWidget):
    def __init__(self):
        super(tempPivot_UI, self).__init__()
        self.setObjectName('tempPivot_UI')
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle('Temp Pivot')
        self.setGeometry(300, 300, 300, 200)
        
        
        self.createUI()
    
    def createUI(self):
        """UI 생성"""
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)
        
        self.createPivotLoc_btn = QPushButton('Create Pivot Loc')
        self.layout.addWidget(self.createPivotLoc_btn)
        
        self.connectOffsetParentMatrix_btn = QPushButton('Connect OffsetParentMatrix')
        self.layout.addWidget(self.connectOffsetParentMatrix_btn)
        
        self.disconnectOffsetParentMatrix_btn = QPushButton('Disconnect OffsetParentMatrix')
        self.layout.addWidget(self.disconnectOffsetParentMatrix_btn)
        
        self.resetOffsetParentMatrix_btn = QPushButton('Reset OffsetParentMatrix')
        self.layout.addWidget(self.resetOffsetParentMatrix_btn)
        
        self.layout.addStretch()
        
        self.show()