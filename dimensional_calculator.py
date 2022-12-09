# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dimensional_calculator.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 413)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.select_rectangle = QtWidgets.QRadioButton(self.centralwidget)
        self.select_rectangle.setGeometry(QtCore.QRect(180, 270, 141, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.select_rectangle.setFont(font)
        self.select_rectangle.setObjectName("select_rectangle")
        self.text_input_tertiary = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input_tertiary.setEnabled(False)
        self.text_input_tertiary.setGeometry(QtCore.QRect(200, 190, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_input_tertiary.setFont(font)
        self.text_input_tertiary.setText("")
        self.text_input_tertiary.setObjectName("text_input_tertiary")
        self.text_input_primary = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input_primary.setGeometry(QtCore.QRect(200, 70, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_input_primary.setFont(font)
        self.text_input_primary.setText("")
        self.text_input_primary.setObjectName("text_input_primary")
        self.label_secondary = QtWidgets.QLabel(self.centralwidget)
        self.label_secondary.setGeometry(QtCore.QRect(110, 130, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_secondary.setFont(font)
        self.label_secondary.setText("")
        self.label_secondary.setObjectName("label_secondary")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(140, 0, 341, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_tertiary = QtWidgets.QLabel(self.centralwidget)
        self.label_tertiary.setGeometry(QtCore.QRect(110, 190, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_tertiary.setFont(font)
        self.label_tertiary.setText("")
        self.label_tertiary.setObjectName("label_tertiary")
        self.select_triangle = QtWidgets.QRadioButton(self.centralwidget)
        self.select_triangle.setGeometry(QtCore.QRect(410, 270, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.select_triangle.setFont(font)
        self.select_triangle.setObjectName("select_triangle")
        self.select_square = QtWidgets.QRadioButton(self.centralwidget)
        self.select_square.setGeometry(QtCore.QRect(310, 270, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.select_square.setFont(font)
        self.select_square.setObjectName("select_square")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 310, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_area = QtWidgets.QLabel(self.centralwidget)
        self.label_area.setGeometry(QtCore.QRect(60, 350, 371, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_area.setFont(font)
        self.label_area.setText("")
        self.label_area.setObjectName("label_area")
        self.text_input_secondary = QtWidgets.QLineEdit(self.centralwidget)
        self.text_input_secondary.setEnabled(False)
        self.text_input_secondary.setGeometry(QtCore.QRect(200, 130, 301, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.text_input_secondary.setFont(font)
        self.text_input_secondary.setText("")
        self.text_input_secondary.setObjectName("text_input_secondary")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 350, 111, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.button_calculate = QtWidgets.QPushButton(self.centralwidget)
        self.button_calculate.setGeometry(QtCore.QRect(450, 310, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_calculate.setFont(font)
        self.button_calculate.setObjectName("button_calculate")
        self.select_circle = QtWidgets.QRadioButton(self.centralwidget)
        self.select_circle.setGeometry(QtCore.QRect(90, 270, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.select_circle.setFont(font)
        self.select_circle.setChecked(True)
        self.select_circle.setObjectName("select_circle")
        self.label_primary = QtWidgets.QLabel(self.centralwidget)
        self.label_primary.setGeometry(QtCore.QRect(110, 70, 81, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_primary.setFont(font)
        self.label_primary.setObjectName("label_primary")
        self.label_perimeter = QtWidgets.QLabel(self.centralwidget)
        self.label_perimeter.setGeometry(QtCore.QRect(100, 310, 331, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_perimeter.setFont(font)
        self.label_perimeter.setText("")
        self.label_perimeter.setObjectName("label_perimeter")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 230, 161, 41))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.button_reset = QtWidgets.QPushButton(self.centralwidget)
        self.button_reset.setGeometry(QtCore.QRect(450, 360, 111, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.button_reset.setFont(font)
        self.button_reset.setObjectName("button_reset")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Dimensional Calculator"))
        self.select_rectangle.setText(_translate("MainWindow", "Rectangle"))
        self.label_4.setText(_translate("MainWindow", "Dimension Calculator"))
        self.select_triangle.setText(_translate("MainWindow", "Triangle"))
        self.select_square.setText(_translate("MainWindow", "Square"))
        self.label.setText(_translate("MainWindow", "Perimeter:"))
        self.label_2.setText(_translate("MainWindow", "Area:"))
        self.button_calculate.setText(_translate("MainWindow", "Calculate"))
        self.select_circle.setText(_translate("MainWindow", "Circle"))
        self.label_primary.setText(_translate("MainWindow", "Radius"))
        self.label_3.setText(_translate("MainWindow", "Select a Shape:"))
        self.button_reset.setText(_translate("MainWindow", "Reset"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
