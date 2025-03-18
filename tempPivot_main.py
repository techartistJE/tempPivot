from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *

import maya.OpenMayaUI as mui
import maya.cmds as cmds
from functools import partial
import shiboken2
import sys
import os

# 패키지 경로 설정
try:
    RootDir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    pkgPath = os.path.dirname(os.path.abspath(__file__))
except:
    pkgPath = 'D:/myScript/maya/tempPivot'

# 모듈 가져오기
import tempPivot.tempPivot_func as tempPivot_func
import tempPivot.tempPivot_ui as tempPivot_ui
import tempPivot.colorpalette_ui as colorpalette_ui

# 모듈 리로드 (Python 3.7 이상)
if sys.version_info > (3, 7, 0):
    import importlib
    importlib.reload(tempPivot_func)
    importlib.reload(tempPivot_ui)
    importlib.reload(colorpalette_ui)
    print("Reloaded modules")
else:
    import imp
    imp.reload(tempPivot_func)
    imp.reload(tempPivot_ui)
    imp.reload(colorpalette_ui)

# Maya 메인 윈도우 가져오기
def getMayaWindow():
    ptr = mui.MQtUtil.mainWindow()
    return shiboken2.wrapInstance(int(ptr), QWidget)

# 메인 윈도우 클래스
class mainWin(QMainWindow):
    def __init__(self):
        super(mainWin, self).__init__(parent=getMayaWindow())
        self.setObjectName("tempPivot_win")  # Maya UI에서 찾을 수 있도록 설정
        self.setWindowTitle("Temp Pivot")
        #window size
        self.resize(400, 300)
        self.ui = tempPivot_ui.TempPivotUI()
        self.paletteWin = colorpalette_ui.colorPalette()
        self.setCentralWidget(self.ui)
        
        
        self.connectFunc()

        self.pivotDict = {}
        self.initColorID = 0
        self.initPivotLocTable()

        if not self.pivotDict:
            self.ui.editMode_btn.setEnabled(False)
        
        self.ui.pivotLocTable.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.pivotLocTable.customContextMenuRequested.connect(self.tableContextMenu)

    def inputTarget(self):
        targetList = cmds.ls(sl=True, type='transform')
        if len(targetList) == 0:
            cmds.warning("Select Target")
            return
   
    
    def createPivotLocs(self):
        # all items in listWidget
        targetList = cmds.ls(sl=True, type='transform')
        if len(targetList) == 0:
            cmds.warning("Select Target")
            return
        IsObjectSpace= self.ui.objSpace_radio.isChecked()
        for target in targetList:
            pivotLocName = target + '_pivotLoc'
            if self.pivotDict.get(target):
                cmds.warning(f'{target} already exists. Please delete it first. or edit mode on')
                continue
            self.pivotDict[target] = tempPivot_func.TempPivot(target, pivotLocName, IsObjectSpace)
            self.pivotDict[target].createInitTempPivot(self.initColorID)

            cmds.addAttr(pivotLocName, ln='pivotData', dt='string')
            noteText= "target: "+target +"\n" + 'space: ' + ('Object' if IsObjectSpace else 'World')
            cmds.setAttr(pivotLocName +'.pivotData', noteText, type='string')
            # lock attribute
            cmds.setAttr(pivotLocName+'.pivotData', lock=True)
        
        self.updatePivotLocTable()
        if not self.pivotDict:
            self.ui.editMode_btn.setEnabled(False)
        self.ui.editMode_btn.setEnabled(True)
        if self.pivotDict:
            if self.ui.editMode_btn.text() == 'Edit Mode Off':
                self.ui.editMode_btn.click()
        else:
            if self.ui.editMode_btn.text() == 'Edit Mode On':
                self.ui.editMode_btn.click()
    

    def initPivotLocTable(self):
        # when open window, check if there is any pivotLocs and update pivotLocTable
        self.pivotDict = {}
        tempPivotLocList = cmds.ls(type='locator')
        pivotLocList = []
        for pivotLoc in tempPivotLocList:
            # check shape node is locator type
            transNode = cmds.listRelatives(pivotLoc, p=True)[0]
            # check if pivotLoc has pivotData attribute
            if cmds.attributeQuery('pivotData', node=transNode, exists=True):
                pivotLocList.append(transNode)
       
        for pivotLoc in pivotLocList:
            target = cmds.getAttr(pivotLoc+'.piv otData').split('\n')[0].split(': ')[1]
            IsObjectSpace = True if cmds.getAttr(pivotLoc+'.pivotData').split('\n')[1].split(': ')[1] == 'Object' else False
            self.pivotDict[target] = tempPivot_func.TempPivot(target, pivotLoc, IsObjectSpace)
        self.updatePivotLocTable()
        if self.pivotDict:
            if self.ui.editMode_btn.text() == 'Edit Mode Off':
                self.ui.editMode_btn.click()
        else:
            if self.ui.editMode_btn.text() == 'Edit Mode On':
                self.ui.editMode_btn.click()
        

    def updatePivotLocTable(self):
        self.ui.pivotLocTable.setRowCount(len(self.pivotDict))
        row = 0
        for target, tempPivot in self.pivotDict.items():
            self.ui.pivotLocTable.setItem(row, 0, QTableWidgetItem(tempPivot.pivotLocName))
            self.ui.pivotLocTable.setItem(row, 1, QTableWidgetItem(tempPivot.target))

            # ✅ 버튼 추가 및 `functools.partial()` 사용하여 `lambda` 문제 해결
            spaceButton = QPushButton('Object' if tempPivot.objSpace else 'World')
            spaceButton.setStyleSheet('background-color: rgb(93,93,93,100); font-weight: plain;')
            self.ui.pivotLocTable.setCellWidget(row, 2, spaceButton)
            
            self.ui.spaceButtonsDict[target] = spaceButton
            spaceButton.clicked.connect(partial(self.ui.updateSpaceButtons, target))  # ✅ 수정

            row += 1

        print(self.ui.spaceButtonsDict)
        # stretch the last row
        self.ui.pivotLocTable.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)

        
    def colorPalette(self):
        # show color palette at the center of the parent widget
        self.paletteWin.move(self.x() + self.width() / 2 - self.paletteWin.width() / 2, 
                             self.y() + self.height() / 2 - self.paletteWin.height() / 2)
        self.paletteWin.show()
        if not self.paletteWin.exec_():
            # cliked color buttons in color palette
            # get current color
            colorID = self.paletteWin.currentColorID
            self.initColorID = colorID
            color = self.paletteWin.RGBColorLst[colorID]

            # color: [r, g, b]
            self.ui.color_btn.setStyleSheet(f"background-color: rgb({color[0]}, {color[1]}, {color[2]})")
            # if selected pivotLocs, change color
            locators = self.pivotDict.values()
            print(locators)
            tempSel= cmds.ls(sl=True)
            for loc in locators:
                locatorName = loc.pivotLocName
                if locatorName in tempSel:
                    print("coloriing")
                    cmds.setAttr(locatorName+'.overrideEnabled', 1)
                    # index 0: RGB, 1: intensity
                    cmds.setAttr(locatorName+'.overrideColor', colorID)

    def tableContextMenu(self, pos):
        # get locator list from selected row
        # select locator menu
        # delete locator menu
        menu = QMenu()
        deleteAction = menu.addAction('Delete')
        selectAction = menu.addAction('Select')
        action = menu.exec_(self.ui.pivotLocTable.mapToGlobal(pos))
        if action == deleteAction:
            locators = self.ui.getSelectedData(0)
            targets= self.ui.getSelectedData(1)
            for target in targets:
                self.pivotDict[target].deletePivotLoc()
            self.initPivotLocTable()
    
            
            cmds.delete(locators)
        elif action == selectAction:
            locators = self.ui.getSelectedData()
            cmds.select(locators)
    def editModeOnOff(self):
        self.ui.editModeOnOff()
        for target, tempPivot in self.pivotDict.items():
            spacebutton = self.ui.spaceButtonsDict[target]
            if spacebutton.text() == 'World':
                tempPivot.objSpace = False
                # unlock attribute
                cmds.setAttr(tempPivot.pivotLocName+'.pivotData', lock=False)
                locatorData= cmds.getAttr(tempPivot.pivotLocName+'.pivotData')
              
                locatorData= locatorData.replace('Object', 'World')
                
                cmds.setAttr(tempPivot.pivotLocName+'.pivotData', locatorData, type='string')
                # lock attribute
                cmds.setAttr(tempPivot.pivotLocName+'.pivotData', lock=True)
                
            else:
                tempPivot.objSpace = True
                # unlock attribute
                cmds.setAttr(tempPivot.pivotLocName+'.pivotData', lock=False)
                locatorData= cmds.getAttr(tempPivot.pivotLocName+'.pivotData')
                locatorData= locatorData.replace('World', 'Object')
                cmds.setAttr(tempPivot.pivotLocName+'.pivotData', locatorData, type='string')
                # lock attribute
                cmds.setAttr(tempPivot.pivotLocName+'.pivotData', lock=True)
        
            
        if self.ui.editMode_btn.text() == 'Edit Mode Off':
            for target, tempPivot in self.pivotDict.items():
                if tempPivot.objSpace:
                    # calculate offset matrix
                    # parentLocator's position (0,0,5) -> childLocator's position (0,0,0)
                    # parentLocator's roatation (0, 45, 0) -> childLocator's rotation (0, 0, 0)
                    # then, offsetMatrix = parentLocator's matrix * childLocator's matrix
                    tempPivot.offsetMatrix= tempPivot.calculateOffsetMatrix()
                else:
                    tempPivot.offsetMatrix= [0]*16
            # space button disable
            for target, spaceButton in self.ui.spaceButtonsDict.items():
                spaceButton.setEnabled(False)
        else:
            for target, spaceButton in self.ui.spaceButtonsDict.items():
                spaceButton.setEnabled(True)
            
    def tempPivotOnOff(self):
        self.ui.tempPivotOnOff()
        if self.ui.connect_btn.text() == 'Temp Pivot On':
            for target, tempPivot in self.pivotDict.items():
                
                tempPivot.connectOffsetParentMatrix()
        else:
            for target, tempPivot in self.pivotDict.items():
                tempPivot.disconnectOffsetParentMatrix()

    def connectFunc(self):
        #self.ui.inputTarget_btn.clicked.connect(self.inputTarget)
        self.ui.createPivot_btn.clicked.connect(self.createPivotLocs)
        self.ui.color_btn.clicked.connect(self.colorPalette)
        self.ui.editMode_btn.clicked.connect(self.editModeOnOff)
        self.ui.connect_btn.clicked.connect(self.tempPivotOnOff)

# 실행 함수
def run():
    # ✅ 기존 PySide2 창이 존재하는지 확인 후 삭제
    existing_win = QApplication.instance().findChild(QMainWindow, "tempPivot_win")
    
    if existing_win:
        print("Existing window detected. Deleting...")
        existing_win.close()  # 창 닫기
        existing_win.deleteLater()  # 가비지 컬렉션 정리
    
    # ✅ 기존 Maya 윈도우 삭제
    if cmds.window("tempPivot_win", q=True, exists=True):
        cmds.deleteUI("tempPivot_win")
    

    # ✅ 새 창 생성
    global win  # 변수를 글로벌로 설정해 중복 방지
    win = mainWin()
    win.show()
    return win  # Maya에서 변수로 받을 수 있도록 반환

# 실행
if __name__ == "__main__":
    run()
