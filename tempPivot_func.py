import maya.cmds as cmds
import maya.OpenMaya as om

class TempPivot:
    def __init__(self, pivotLocName, target):
        self.tempPivotLoc = pivotLocName
        self.target = target
        self.targetMatrix = cmds.xform(self.target, q=True, ws=True, m=True)
        self.createInitTempPivot()
        
    
    def createInitTempPivot(self):
        """임시 피벗 생성"""
        if not cmds.objExists(self.tempPivotLoc):
            cmds.spaceLocator(n=self.tempPivotLoc)
        self.copyMatrix(self.target, self.tempPivotLoc)
        # set pivotLoc's color red
        cmds.setAttr(self.tempPivotLoc+'.overrideEnabled', 1)
        cmds.setAttr(self.tempPivotLoc+'.overrideColor', 13)

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
        """offsetParentMatrix를 적용하면서 현재 위치 유지"""
        tempOriginLoc = cmds.spaceLocator(n='tempOriginLoc')[0]
        self.copyMatrix(self.target, tempOriginLoc)

        # 현재 스케일을 보정하여 적용
        scale = cmds.xform(self.target, q=True, ws=True, s=True)
        cmds.connectAttr(self.tempPivotLoc+'.worldMatrix[0]', self.target+'.offsetParentMatrix', f=True)

        # 기존 위치 복구
        self.copyMatrix(tempOriginLoc, self.target)
        cmds.xform(self.target, ws=True, s=scale)  # 스케일 유지
        cmds.delete(tempOriginLoc)

    def disconnectOffsetParentMatrix(self):
        """offsetParentMatrix 연결 해제 후 원래 위치 유지"""
        cmds.disconnectAttr(self.tempPivotLoc+'.worldMatrix[0]', self.target+'.offsetParentMatrix')
        self.resetOffsetParentMatrix()

    def resetOffsetParentMatrix(self):
        """offsetParentMatrix 초기화 후 원래 위치 복원"""
        currentMatrix = cmds.getAttr(self.target + '.worldMatrix[0]')
        currentScale = cmds.xform(self.target, q=True, ws=True, s=True)

        # 초기화 행렬 적용
        offsetparentMatrix = [1, 0, 0, 0, 
                              0, 1, 0, 0, 
                              0, 0, 1, 0, 
                              0, 0, 0, 1]
        cmds.setAttr(self.target+'.offsetParentMatrix', offsetparentMatrix, type='matrix')

        # 원래 위치 복원
        cmds.xform(self.target, ws=True, m=currentMatrix)
        cmds.xform(self.target, ws=True, s=currentScale)  # 스케일 복구

if __name__ == '__main__':
    testList = cmds.ls(sl=1)
    if len(testList) >= 2:
        tempPivot = TempPivot(testList[0], testList[1])
        tempPivot.connectOffsetParentMatrix()
    
    tempPivot.disconnectOffsetParentMatrix()