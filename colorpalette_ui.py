# -*- coding: utf-8 -*-
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class colorPalette(QDialog):
    def __init__(self, parent=None):
        super(colorPalette, self).__init__(parent)
        self.ui= Ui_ColorPalette_base()
        self.ui.setupUi(self)
        #self.setModal(False)
        self.btnUI = self.ui.__dict__
        self.RGBColorLst =[[93,93,93], [0, 0, 0],[73, 73, 73],[153, 153, 153], [155, 0, 40],[0, 4, 96], [0, 0, 255], [0, 69, 25], [38, 0, 66], [197, 0, 197], [134, 70, 50],[65, 35, 31],[149, 37, 0], [1, 0, 0],[0, 252, 0],[0,63, 149], [254, 254, 254],[245, 245, 0], [99, 218, 253],[66, 250, 160],[248, 171, 171],[223, 168, 118],[252,252,98],[0, 147, 81], [215, 143, 107], [223, 199, 78], [161, 206, 71],[58, 188, 145],[63, 204, 181],[58, 156, 205],[150, 103, 198],[204, 88, 165]]

        self.colorSet()
        self.functionConnect()
        self.currentColorID =0
        self.currentRGB = [93,93,93]

    
    def colorSet(self):
        for i in range(32):
            rgbVal= self.RGBColorLst[i]
            btnName = "color_btn_{0}".format(str(i))
            self.btnUI[btnName].setStyleSheet("background:rgb({0},{1},{2},255)".format(rgbVal[0], rgbVal[1],
                                                         rgbVal[2] ))
        self.btnUI['color_btn_0'].setText("No Color")

    def returnColorID(self, id):
        print( "returnColorID", id)
        self.currentColorID = id
        
        self.close()


    def functionConnect(self):
        self.btnUI['color_btn_0'].clicked.connect(lambda: self.returnColorID(0))
        self.btnUI['color_btn_1'].clicked.connect(lambda: self.returnColorID(1))
        self.btnUI['color_btn_2'].clicked.connect(lambda: self.returnColorID(2))
        self.btnUI['color_btn_3'].clicked.connect(lambda: self.returnColorID(3))
        self.btnUI['color_btn_4'].clicked.connect(lambda: self.returnColorID(4))
        self.btnUI['color_btn_5'].clicked.connect(lambda: self.returnColorID(5))
        self.btnUI['color_btn_6'].clicked.connect(lambda: self.returnColorID(6))
        self.btnUI['color_btn_7'].clicked.connect(lambda: self.returnColorID(7))
        self.btnUI['color_btn_8'].clicked.connect(lambda: self.returnColorID(8))
        self.btnUI['color_btn_9'].clicked.connect(lambda: self.returnColorID(9))
        self.btnUI['color_btn_10'].clicked.connect(lambda: self.returnColorID(10))
        self.btnUI['color_btn_11'].clicked.connect(lambda: self.returnColorID(11))
        self.btnUI['color_btn_12'].clicked.connect(lambda: self.returnColorID(12))
        self.btnUI['color_btn_13'].clicked.connect(lambda: self.returnColorID(13))
        self.btnUI['color_btn_14'].clicked.connect(lambda: self.returnColorID(14))
        self.btnUI['color_btn_15'].clicked.connect(lambda: self.returnColorID(15))
        self.btnUI['color_btn_16'].clicked.connect(lambda: self.returnColorID(16))
        self.btnUI['color_btn_17'].clicked.connect(lambda: self.returnColorID(17))
        self.btnUI['color_btn_18'].clicked.connect(lambda: self.returnColorID(18))
        self.btnUI['color_btn_19'].clicked.connect(lambda: self.returnColorID(19))
        self.btnUI['color_btn_20'].clicked.connect(lambda: self.returnColorID(20))
        self.btnUI['color_btn_21'].clicked.connect(lambda: self.returnColorID(21))
        self.btnUI['color_btn_22'].clicked.connect(lambda: self.returnColorID(22))
        self.btnUI['color_btn_23'].clicked.connect(lambda: self.returnColorID(23))
        self.btnUI['color_btn_24'].clicked.connect(lambda: self.returnColorID(24))
        self.btnUI['color_btn_25'].clicked.connect(lambda: self.returnColorID(25))
        self.btnUI['color_btn_26'].clicked.connect(lambda: self.returnColorID(26))
        self.btnUI['color_btn_27'].clicked.connect(lambda: self.returnColorID(27))
        self.btnUI['color_btn_28'].clicked.connect(lambda: self.returnColorID(28))
        self.btnUI['color_btn_29'].clicked.connect(lambda: self.returnColorID(29))
        self.btnUI['color_btn_30'].clicked.connect(lambda: self.returnColorID(30))
        self.btnUI['color_btn_31'].clicked.connect(lambda: self.returnColorID(31))



class Ui_ColorPalette_base(object):
    def setupUi(self, ColorPalette_base):
        if not ColorPalette_base.objectName():
            ColorPalette_base.setObjectName(u"ColorPalette_base")
        ColorPalette_base.resize(291, 204)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(ColorPalette_base.sizePolicy().hasHeightForWidth())
        ColorPalette_base.setSizePolicy(sizePolicy)
        ColorPalette_base.setMinimumSize(QSize(291, 204))
        ColorPalette_base.setMaximumSize(QSize(291, 204))
        ColorPalette_base.setSizeIncrement(QSize(0, 0))
        ColorPalette_base.setBaseSize(QSize(291, 204))
        ColorPalette_base.setSizeGripEnabled(False)
        ColorPalette_base.setModal(True)
        self.gridLayout = QGridLayout(ColorPalette_base)
        self.gridLayout.setSpacing(3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(10, 5, 10, 5)
        self.color_btn_0 = QPushButton(ColorPalette_base)
        self.color_btn_0.setObjectName(u"color_btn_0")
        self.color_btn_0.setEnabled(True)
        self.color_btn_0.setMinimumSize(QSize(0, 0))
        self.color_btn_0.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_0, 0, 0, 1, 1)

        self.color_btn_1 = QPushButton(ColorPalette_base)
        self.color_btn_1.setObjectName(u"color_btn_1")
        self.color_btn_1.setEnabled(True)
        self.color_btn_1.setMinimumSize(QSize(0, 0))
        self.color_btn_1.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_1, 0, 1, 1, 1)

        self.color_btn_2 = QPushButton(ColorPalette_base)
        self.color_btn_2.setObjectName(u"color_btn_2")
        self.color_btn_2.setEnabled(True)
        self.color_btn_2.setMinimumSize(QSize(0, 0))
        self.color_btn_2.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_2, 0, 2, 1, 1)

        self.color_btn_3 = QPushButton(ColorPalette_base)
        self.color_btn_3.setObjectName(u"color_btn_3")
        self.color_btn_3.setEnabled(True)
        self.color_btn_3.setMinimumSize(QSize(0, 0))
        self.color_btn_3.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_3, 0, 3, 1, 1)

        self.color_btn_4 = QPushButton(ColorPalette_base)
        self.color_btn_4.setObjectName(u"color_btn_4")
        self.color_btn_4.setEnabled(True)
        self.color_btn_4.setMinimumSize(QSize(0, 0))
        self.color_btn_4.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_4, 1, 0, 1, 1)

        self.color_btn_6 = QPushButton(ColorPalette_base)
        self.color_btn_6.setObjectName(u"color_btn_6")
        self.color_btn_6.setEnabled(True)
        self.color_btn_6.setMinimumSize(QSize(0, 0))
        self.color_btn_6.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_6, 1, 1, 1, 1)

        self.color_btn_5 = QPushButton(ColorPalette_base)
        self.color_btn_5.setObjectName(u"color_btn_5")
        self.color_btn_5.setEnabled(True)
        self.color_btn_5.setMinimumSize(QSize(0, 0))
        self.color_btn_5.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_5, 1, 2, 1, 1)

        self.color_btn_7 = QPushButton(ColorPalette_base)
        self.color_btn_7.setObjectName(u"color_btn_7")
        self.color_btn_7.setEnabled(True)
        self.color_btn_7.setMinimumSize(QSize(0, 0))
        self.color_btn_7.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_7, 1, 3, 1, 1)

        self.color_btn_8 = QPushButton(ColorPalette_base)
        self.color_btn_8.setObjectName(u"color_btn_8")
        self.color_btn_8.setEnabled(True)
        self.color_btn_8.setMinimumSize(QSize(0, 0))
        self.color_btn_8.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_8, 2, 0, 1, 1)

        self.color_btn_9 = QPushButton(ColorPalette_base)
        self.color_btn_9.setObjectName(u"color_btn_9")
        self.color_btn_9.setEnabled(True)
        self.color_btn_9.setMinimumSize(QSize(0, 0))
        self.color_btn_9.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_9, 2, 1, 1, 1)

        self.color_btn_10 = QPushButton(ColorPalette_base)
        self.color_btn_10.setObjectName(u"color_btn_10")
        self.color_btn_10.setEnabled(True)
        self.color_btn_10.setMinimumSize(QSize(0, 0))
        self.color_btn_10.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_10, 2, 2, 1, 1)

        self.color_btn_11 = QPushButton(ColorPalette_base)
        self.color_btn_11.setObjectName(u"color_btn_11")
        self.color_btn_11.setEnabled(True)
        self.color_btn_11.setMinimumSize(QSize(0, 0))
        self.color_btn_11.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_11, 2, 3, 1, 1)

        self.color_btn_12 = QPushButton(ColorPalette_base)
        self.color_btn_12.setObjectName(u"color_btn_12")
        self.color_btn_12.setEnabled(True)
        self.color_btn_12.setMinimumSize(QSize(0, 0))
        self.color_btn_12.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_12, 3, 0, 1, 1)

        self.color_btn_13 = QPushButton(ColorPalette_base)
        self.color_btn_13.setObjectName(u"color_btn_13")
        self.color_btn_13.setEnabled(True)
        self.color_btn_13.setMinimumSize(QSize(0, 0))
        self.color_btn_13.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_13, 3, 1, 1, 1)

        self.color_btn_14 = QPushButton(ColorPalette_base)
        self.color_btn_14.setObjectName(u"color_btn_14")
        self.color_btn_14.setEnabled(True)
        self.color_btn_14.setMinimumSize(QSize(0, 0))
        self.color_btn_14.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_14, 3, 2, 1, 1)

        self.color_btn_15 = QPushButton(ColorPalette_base)
        self.color_btn_15.setObjectName(u"color_btn_15")
        self.color_btn_15.setEnabled(True)
        self.color_btn_15.setMinimumSize(QSize(0, 0))
        self.color_btn_15.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_15, 3, 3, 1, 1)

        self.color_btn_16 = QPushButton(ColorPalette_base)
        self.color_btn_16.setObjectName(u"color_btn_16")
        self.color_btn_16.setEnabled(True)
        self.color_btn_16.setMinimumSize(QSize(0, 0))
        self.color_btn_16.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_16, 4, 0, 1, 1)

        self.color_btn_17 = QPushButton(ColorPalette_base)
        self.color_btn_17.setObjectName(u"color_btn_17")
        self.color_btn_17.setEnabled(True)
        self.color_btn_17.setMinimumSize(QSize(0, 0))
        self.color_btn_17.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_17, 4, 1, 1, 1)

        self.color_btn_18 = QPushButton(ColorPalette_base)
        self.color_btn_18.setObjectName(u"color_btn_18")
        self.color_btn_18.setEnabled(True)
        self.color_btn_18.setMinimumSize(QSize(0, 0))
        self.color_btn_18.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_18, 4, 2, 1, 1)

        self.color_btn_19 = QPushButton(ColorPalette_base)
        self.color_btn_19.setObjectName(u"color_btn_19")
        self.color_btn_19.setEnabled(True)
        self.color_btn_19.setMinimumSize(QSize(0, 0))
        self.color_btn_19.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_19, 4, 3, 1, 1)

        self.color_btn_20 = QPushButton(ColorPalette_base)
        self.color_btn_20.setObjectName(u"color_btn_20")
        self.color_btn_20.setEnabled(True)
        self.color_btn_20.setMinimumSize(QSize(0, 0))
        self.color_btn_20.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_20, 5, 0, 1, 1)

        self.color_btn_21 = QPushButton(ColorPalette_base)
        self.color_btn_21.setObjectName(u"color_btn_21")
        self.color_btn_21.setEnabled(True)
        self.color_btn_21.setMinimumSize(QSize(0, 0))
        self.color_btn_21.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_21, 5, 1, 1, 1)

        self.color_btn_22 = QPushButton(ColorPalette_base)
        self.color_btn_22.setObjectName(u"color_btn_22")
        self.color_btn_22.setEnabled(True)
        self.color_btn_22.setMinimumSize(QSize(0, 0))
        self.color_btn_22.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_22, 5, 2, 1, 1)

        self.color_btn_23 = QPushButton(ColorPalette_base)
        self.color_btn_23.setObjectName(u"color_btn_23")
        self.color_btn_23.setEnabled(True)
        self.color_btn_23.setMinimumSize(QSize(0, 0))
        self.color_btn_23.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_23, 5, 3, 1, 1)

        self.color_btn_24 = QPushButton(ColorPalette_base)
        self.color_btn_24.setObjectName(u"color_btn_24")
        self.color_btn_24.setEnabled(True)
        self.color_btn_24.setMinimumSize(QSize(0, 0))
        self.color_btn_24.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_24, 6, 0, 1, 1)

        self.color_btn_25 = QPushButton(ColorPalette_base)
        self.color_btn_25.setObjectName(u"color_btn_25")
        self.color_btn_25.setEnabled(True)
        self.color_btn_25.setMinimumSize(QSize(0, 0))
        self.color_btn_25.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_25, 6, 1, 1, 1)

        self.color_btn_26 = QPushButton(ColorPalette_base)
        self.color_btn_26.setObjectName(u"color_btn_26")
        self.color_btn_26.setEnabled(True)
        self.color_btn_26.setMinimumSize(QSize(0, 0))
        self.color_btn_26.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_26, 6, 2, 1, 1)

        self.color_btn_27 = QPushButton(ColorPalette_base)
        self.color_btn_27.setObjectName(u"color_btn_27")
        self.color_btn_27.setEnabled(True)
        self.color_btn_27.setMinimumSize(QSize(0, 0))
        self.color_btn_27.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_27, 6, 3, 1, 1)

        self.color_btn_28 = QPushButton(ColorPalette_base)
        self.color_btn_28.setObjectName(u"color_btn_28")
        self.color_btn_28.setEnabled(True)
        self.color_btn_28.setMinimumSize(QSize(0, 0))
        self.color_btn_28.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_28, 7, 0, 1, 1)

        self.color_btn_29 = QPushButton(ColorPalette_base)
        self.color_btn_29.setObjectName(u"color_btn_29")
        self.color_btn_29.setEnabled(True)
        self.color_btn_29.setMinimumSize(QSize(0, 0))
        self.color_btn_29.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_29, 7, 1, 1, 1)

        self.color_btn_30 = QPushButton(ColorPalette_base)
        self.color_btn_30.setObjectName(u"color_btn_30")
        self.color_btn_30.setEnabled(True)
        self.color_btn_30.setMinimumSize(QSize(0, 0))
        self.color_btn_30.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_30, 7, 2, 1, 1)

        self.color_btn_31 = QPushButton(ColorPalette_base)
        self.color_btn_31.setObjectName(u"color_btn_31")
        self.color_btn_31.setEnabled(True)
        self.color_btn_31.setMinimumSize(QSize(0, 0))
        self.color_btn_31.setFlat(False)

        self.gridLayout.addWidget(self.color_btn_31, 7, 3, 1, 1)

        QWidget.setTabOrder(self.color_btn_0, self.color_btn_1)
        QWidget.setTabOrder(self.color_btn_1, self.color_btn_2)
        QWidget.setTabOrder(self.color_btn_2, self.color_btn_3)
        QWidget.setTabOrder(self.color_btn_3, self.color_btn_4)
        QWidget.setTabOrder(self.color_btn_4, self.color_btn_6)
        QWidget.setTabOrder(self.color_btn_6, self.color_btn_5)
        QWidget.setTabOrder(self.color_btn_5, self.color_btn_7)
        QWidget.setTabOrder(self.color_btn_7, self.color_btn_8)
        QWidget.setTabOrder(self.color_btn_8, self.color_btn_9)
        QWidget.setTabOrder(self.color_btn_9, self.color_btn_10)
        QWidget.setTabOrder(self.color_btn_10, self.color_btn_11)
        QWidget.setTabOrder(self.color_btn_11, self.color_btn_12)
        QWidget.setTabOrder(self.color_btn_12, self.color_btn_13)
        QWidget.setTabOrder(self.color_btn_13, self.color_btn_14)
        QWidget.setTabOrder(self.color_btn_14, self.color_btn_15)
        QWidget.setTabOrder(self.color_btn_15, self.color_btn_16)
        QWidget.setTabOrder(self.color_btn_16, self.color_btn_17)
        QWidget.setTabOrder(self.color_btn_17, self.color_btn_18)
        QWidget.setTabOrder(self.color_btn_18, self.color_btn_19)
        QWidget.setTabOrder(self.color_btn_19, self.color_btn_20)
        QWidget.setTabOrder(self.color_btn_20, self.color_btn_21)
        QWidget.setTabOrder(self.color_btn_21, self.color_btn_22)
        QWidget.setTabOrder(self.color_btn_22, self.color_btn_23)
        QWidget.setTabOrder(self.color_btn_23, self.color_btn_24)
        QWidget.setTabOrder(self.color_btn_24, self.color_btn_25)
        QWidget.setTabOrder(self.color_btn_25, self.color_btn_26)
        QWidget.setTabOrder(self.color_btn_26, self.color_btn_27)
        QWidget.setTabOrder(self.color_btn_27, self.color_btn_28)
        QWidget.setTabOrder(self.color_btn_28, self.color_btn_29)
        QWidget.setTabOrder(self.color_btn_29, self.color_btn_30)
        QWidget.setTabOrder(self.color_btn_30, self.color_btn_31)

        self.retranslateUi(ColorPalette_base)

        self.color_btn_0.setDefault(False)
        self.color_btn_1.setDefault(False)
        self.color_btn_2.setDefault(False)
        self.color_btn_3.setDefault(False)
        self.color_btn_4.setDefault(False)
        self.color_btn_6.setDefault(False)
        self.color_btn_5.setDefault(False)
        self.color_btn_7.setDefault(False)
        self.color_btn_8.setDefault(False)
        self.color_btn_9.setDefault(False)
        self.color_btn_10.setDefault(False)
        self.color_btn_11.setDefault(False)
        self.color_btn_12.setDefault(False)
        self.color_btn_13.setDefault(False)
        self.color_btn_14.setDefault(False)
        self.color_btn_15.setDefault(False)
        self.color_btn_16.setDefault(False)
        self.color_btn_17.setDefault(False)
        self.color_btn_18.setDefault(False)
        self.color_btn_19.setDefault(False)
        self.color_btn_20.setDefault(False)
        self.color_btn_21.setDefault(False)
        self.color_btn_22.setDefault(False)
        self.color_btn_23.setDefault(False)
        self.color_btn_24.setDefault(False)
        self.color_btn_25.setDefault(False)
        self.color_btn_26.setDefault(False)
        self.color_btn_27.setDefault(False)
        self.color_btn_28.setDefault(False)
        self.color_btn_29.setDefault(False)
        self.color_btn_30.setDefault(False)
        self.color_btn_31.setDefault(False)


        QMetaObject.connectSlotsByName(ColorPalette_base)
    # setupUi

    def retranslateUi(self, ColorPalette_base):
        ColorPalette_base.setWindowTitle(QCoreApplication.translate("ColorPalette_base", u"ColorPalatte", None))
        self.color_btn_0.setText("")
        self.color_btn_1.setText("")
        self.color_btn_2.setText("")
        self.color_btn_3.setText("")
        self.color_btn_4.setText("")
        self.color_btn_6.setText("")
        self.color_btn_5.setText("")
        self.color_btn_7.setText("")
        self.color_btn_8.setText("")
        self.color_btn_9.setText("")
        self.color_btn_10.setText("")
        self.color_btn_11.setText("")
        self.color_btn_12.setText("")
        self.color_btn_13.setText("")
        self.color_btn_14.setText("")
        self.color_btn_15.setText("")
        self.color_btn_16.setText("")
        self.color_btn_17.setText("")
        self.color_btn_18.setText("")
        self.color_btn_19.setText("")
        self.color_btn_20.setText("")
        self.color_btn_21.setText("")
        self.color_btn_22.setText("")
        self.color_btn_23.setText("")
        self.color_btn_24.setText("")
        self.color_btn_25.setText("")
        self.color_btn_26.setText("")
        self.color_btn_27.setText("")
        self.color_btn_28.setText("")
        self.color_btn_29.setText("")
        self.color_btn_30.setText("")
        self.color_btn_31.setText("")
    # retranslateUi

