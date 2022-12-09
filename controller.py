import math
from PyQt5.QtWidgets import *
from dimensional_calculator import *

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)


class Controller(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.primary_number = 0.0
        self.secondary_number = 0.0
        self.tertiary_number = 0.0
        self.setupUi(self)
        self.button_calculate.clicked.connect(lambda: self.calculate())
        self.button_reset.clicked.connect(lambda: self.reset())
        self.select_circle.clicked.connect(lambda: self.circle())
        self.select_rectangle.clicked.connect(lambda: self.rectangle())
        self.select_square.clicked.connect(lambda: self.square())
        self.select_triangle.clicked.connect(lambda: self.triangle())

    def calculate(self):
        """
        Error handling for input and calculation display
        :return:
        """
        try:
            self.primary_number = float(self.text_input_primary.text())
        except ValueError:
            self.text_input_primary.setText('Please enter a number')
            return None

        if self.text_input_secondary.isEnabled():
            try:
                self.secondary_number = float(self.text_input_secondary.text())
            except ValueError:
                self.text_input_secondary.setText('Please enter a number')
                return None
        if self.text_input_tertiary.isEnabled():
            try:
                self.tertiary_number = float(self.text_input_tertiary.text())
            except ValueError:
                self.text_input_tertiary.setText('Please enter a number')
                return None

        if self.select_circle.isChecked():
            self.label_area.setText('{:.2f}'.format(self.a_circle()))
            self.label_perimeter.setText('{:.2f}'.format(self.p_circle()))
        elif self.select_rectangle.isChecked():
            self.label_area.setText('{:.2f}'.format(self.a_rectangle()))
            self.label_perimeter.setText('{:.2f}'.format(self.p_rectangle()))
        elif self.select_square.isChecked():
            self.label_area.setText('{:.2f}'.format(self.a_square()))
            self.label_perimeter.setText('{:.2f}'.format(self.p_square()))
        elif self.select_triangle.isChecked():
            self.label_area.setText('{:.2f}'.format(self.a_triangle()))
            self.label_perimeter.setText('{:.2f}'.format(self.p_triangle()))

    def circle(self):
        """
        Enables appropriate line edits and labels for circle calculation
        :return:
        """
        self.label_primary.setText('Radius')
        self.label_secondary.setText('')
        self.label_tertiary.setText('')

        self.text_input_secondary.setEnabled(False)
        self.text_input_tertiary.setEnabled(False)

        self.text_input_primary.setText('')
        self.text_input_secondary.setText('')
        self.text_input_tertiary.setText('')
        self.label_area.setText('')
        self.label_perimeter.setText('')

    def rectangle(self):
        """
        Enables appropriate line edits and labels for rectangle calculation
        :return: 
        """
        self.label_primary.setText('Length')
        self.label_secondary.setText('Width')
        self.label_tertiary.setText('')

        self.text_input_secondary.setEnabled(True)
        self.text_input_tertiary.setEnabled(False)

        self.text_input_primary.setText('')
        self.text_input_secondary.setText('')
        self.text_input_tertiary.setText('')
        self.label_area.setText('')
        self.label_perimeter.setText('')

    def square(self):
        """
        Enables appropriate line edits and labels for square calculation
        :return: 
        """
        self.label_primary.setText('Length')
        self.label_secondary.setText('')
        self.label_tertiary.setText('')

        self.text_input_secondary.setEnabled(False)
        self.text_input_tertiary.setEnabled(False)

        self.text_input_primary.setText('')
        self.text_input_secondary.setText('')
        self.text_input_tertiary.setText('')
        self.label_area.setText('')
        self.label_perimeter.setText('')
        
    def triangle(self):
        """
        Enables appropriate line edits and labels for triangle calculation
        :return: 
        """
        self.label_primary.setText('Side A')
        self.label_secondary.setText('Side B')
        self.label_tertiary.setText('Side C')

        self.text_input_secondary.setEnabled(True)
        self.text_input_tertiary.setEnabled(True)

        self.text_input_primary.setText('')
        self.text_input_secondary.setText('')
        self.text_input_tertiary.setText('')
        self.label_area.setText('')
        self.label_perimeter.setText('')

    def p_circle(self):
        """
        Find perimeter of a circle
        :return: float
        """
        perimeter = float(2 * math.pi * self.primary_number)
        return perimeter

    def p_rectangle(self): 
        """
        Find perimeter of a rectangle
        :return: float
        """
        perimeter = 2 * (self.primary_number + self.secondary_number)
        return perimeter

    def p_square(self):
        """
        Find perimeter of a square
        :return: float
        """
        perimeter = 4 * self.primary_number
        return perimeter

    def p_triangle(self):
        """
        Find perimeter of a triangle
        :return: float
        """
        perimeter = self.primary_number + self.secondary_number + self.tertiary_number
        return perimeter

    def a_circle(self):
        """
        Find area of a circle
        :return: float
        """
        area = math.pi * self.primary_number * self.primary_number
        return area

    def a_rectangle(self):
        """
        Find area of a rectangle
        :return: float
        """
        area = self.primary_number * self.secondary_number
        return area

    def a_square(self):
        """
        Find area of a square
        :return: float
        """
        area = self.primary_number * self.primary_number
        return area

    def a_triangle(self):
        """
        Use Heron's formula to find the area of a triangle given 3 sides
        :return:
        """
        a = self.primary_number
        b = self.secondary_number
        c = self.tertiary_number
        s = a + b + c / 2
        area = math.sqrt(s * (s - a) * (s - b) * (s - c))
        return area

    def reset(self):
        """
        reset application to beginning state
        :return:
        """
        self.circle()
        self.text_input_primary.setText('')
        self.text_input_secondary.setText('')
        self.text_input_tertiary.setText('')
        self.label_area.setText('')
        self.label_perimeter.setText('')

