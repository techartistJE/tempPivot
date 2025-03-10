from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.OpenMayaUI as mui
import maya.cmds as mc


import shiboken2
import sys
import os

try:
    RootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pkgPath = os.path.dirname(os.path.abspath(__file__))

except:
    pkgPath = 'D:/myScript/maya/tempPivot'



import tempPivot.tempPivot_func as tempPivot_func
import tempPivot.tempPivot_ui as tempPivot_ui


if sys.version_info > (3, 7, 0):
    import importlib
    importlib.reload(tempPivot_func)
    importlib.reload(tempPivot_ui)

else:
    import imp
    imp.reload(tempPivot_func)
    imp.reload(tempPivot_ui)



def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    if sys.version_info >= (3, 0):
        return shiboken2.wrapInstance(int(ptr), QWidget)
    else:
        return shiboken2.wrapInstance(long(ptr), QWidget)
  
class mainWin(QMainWindow):
    def __init__(self):
        super(mainWin, self).__init__(parent =getMayaWindow() )
        self.setObjectName("tempPivot_win")
        self.setWindowTitle("Temp Pivot")

        self.ui= tempPivot_ui.tempPivot_UI()
        self.setCentralWidget(self.ui)


def run():
    win = mainWin()
    win.show()

if __name__ == "__main__":
    try:
        mainWin.close()
    except:
        pass
    mainWin = mainWin()
    mainWin.show()