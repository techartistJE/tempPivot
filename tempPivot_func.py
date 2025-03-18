import maya.cmds as cmds
import maya.api.OpenMaya as om


class TempPivot:
    def __init__(self, target, pivotLocName, objSpace=True):
        self.pivotLocName = pivotLocName
        self.target = target
        self.objSpace = objSpace
        self.offsetMatrix= self.calculateOffsetMatrix()
        self.multMatrixNode= self.pivotLocName+'_multMatrix'
        self.createInitTempPivot()

    
    def createInitTempPivot(self, colorID=0):
        """임시 피벗 생성"""
        if not cmds.objExists(self.pivotLocName):
            cmds.spaceLocator(n=self.pivotLocName)
        if not cmds.objExists(self.multMatrixNode):
            cmds.createNode('multMatrix', n=self.multMatrixNode)
        self.copyMatrix(self.target, self.pivotLocName)
        # set pivotLoc's color red
        if not colorID == 0:
            cmds.setAttr(self.pivotLocName+'.overrideEnabled', 1)
            cmds.setAttr(self.pivotLocName+'.overrideColor', colorID)

    def copyMatrix(self, source, target, T=True, R=True, S=True):
        """source에서 target으로 변환 행렬 복사"""
        matrix = cmds.xform(source, q=True, ws=True, m=True)
        scale = cmds.xform(source, q=True, ws=True, s=True)  # 스케일도 따로 저장
        translate = matrix[12:15]
        rotation = cmds.xform(source, q=True, ws=True, ro=True)

        if T:
            cmds.xform(target, ws=True, t=translate)
        if R:
            cmds.xform(target, ws=True, ro=rotation)
        if S:
            cmds.xform(target, ws=True, s=scale)

    def connectOffsetParentMatrix(self):
        # undo block
        cmds.undoInfo(openChunk=True)
        # reset offsetParentMatrix of target
        self.resetOffsetParentMatrix()
        if self.objSpace:
            targetMatrix = cmds.xform(self.target, q=True, ws=True, m=True)
            targetOMMatrix = om.MMatrix(targetMatrix)
            loc_objSpaceMatrix = self.offsetMatrix * targetOMMatrix

            cmds.xform(self.pivotLocName, ws=True, m=loc_objSpaceMatrix)
        """offsetParentMatrix를 적용하면서 현재 위치 유지"""
        locatorCurrentInverseMatrix = cmds.getAttr(self.pivotLocName+'.worldInverseMatrix[0]')
        cmds.setAttr(self.multMatrixNode+'.matrixIn[0]', locatorCurrentInverseMatrix, type='matrix')
        cmds.connectAttr(self.pivotLocName+'.worldMatrix[0]', self.multMatrixNode+'.matrixIn[1]', f=True)
        cmds.connectAttr(self.multMatrixNode +'.matrixSum', self.target+'.offsetParentMatrix', f=True)

        # undo block close
        cmds.undoInfo(closeChunk=True)
        
    def disconnectOffsetParentMatrix(self):
        # undo block
        cmds.undoInfo(openChunk=True)

        """offsetParentMatrix 연결 해제 후 원래 위치 유지"""
        # 연결 되어있는지 확인
        if cmds.isConnected(self.multMatrixNode+'.matrixSum', self.target+'.offsetParentMatrix'):
            cmds.disconnectAttr(self.multMatrixNode+'.matrixSum', self.target+'.offsetParentMatrix')
        self.resetOffsetParentMatrix()

        # undo block close
        cmds.undoInfo(closeChunk=True)


    def resetOffsetParentMatrix(self):
        """offsetParentMatrix 초기화 후 원래 위치 복원"""
        tempPosLoc= cmds.spaceLocator(n='tempPosLoc')[0]
        cmds.matchTransform(tempPosLoc, self.target)
        
        
        # 초기화 행렬 적용
        offsetparentMatrix = [1, 0, 0, 0, 
                              0, 1, 0, 0, 
                              0, 0, 1, 0, 
                              0, 0, 0, 1]
        cmds.setAttr(self.target+'.offsetParentMatrix', offsetparentMatrix, type='matrix')

        # 원래 위치 복원
        cmds.matchTransform(self.target, tempPosLoc)
        cmds.delete(tempPosLoc)
        

    def deletePivotLoc(self):
        if cmds.objExists(self.pivotLocName):
            cmds.delete(self.pivotLocName)
            cmds.delete(self.multMatrixNode)


    def calculateOffsetMatrix(self):
        """from target to pivotLoc"""
        targetMatrix = cmds.xform(self.target, q=True, ws=True, m=True)
        pivotMatrix = cmds.xform(self.pivotLocName, q=True, ws=True, m=True)
        targetMatrix = om.MMatrix(targetMatrix)
        pivotMatrix = om.MMatrix(pivotMatrix)
        offsetMatrix = pivotMatrix * targetMatrix.inverse()
        # targetMatrix * offsetMatrix = pivotMatrix
        return offsetMatrix

if __name__ == '__main__':
    testList = cmds.ls(sl=1)
    if len(testList) >= 2:
        tempPivot = TempPivot(testList[0], testList[1])
        tempPivot.connectOffsetParentMatrix()
    
    tempPivot.disconnectOffsetParentMatrix()