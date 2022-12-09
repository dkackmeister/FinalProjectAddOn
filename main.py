import tkinter
import math


def p_circle(radius):
    perimeter = float(2 * math.pi * radius)
    return perimeter


def p_rectangle(length, width):
    perimeter = 2 * (length + width)
    return perimeter


def p_square(length):
    perimeter = 4 * length
    return perimeter


def p_triangle(side_a, side_b, side_c):
    perimeter = side_a + side_b + side_c
    return perimeter



def a_circle(radius):
    area = math.pi * radius * radius
    return area


def a_rectangle(length, width):
    area = length * width
    return area


def a_square(length):
    area = length * length
    return area


def a_triangle(height, base):
    area = (base * height) / 2
    return area
def selection():
    print('----------------------')
    print('SELECT SHAPE')
    print('----------------------')
    print('1 - Circle')
    print('2 - Rectangle')
    print('3 - Square')
    print('4 - Triangle')
    shape = 0
    # Code to check that a valid shape has been selected
    while True:
        shape_input = input('Shape number: ')
        try:
            shape = int(shape_input)
        except ValueError:
            print('Please enter an integer (1-4)')
        if shape >= 1 and shape <=4:
            break
    return shape


def main():
    while True:
        # Check that input is in valid range
        user_shape = selection()
        comp_select = int(input('Computation (Area = 1 or Perimeter = 2): '))

        while comp_select < 1 or comp_select > 2:
            comp_select = int(input('Enter 1 or 2: '))

        #If Area
        if comp_select == 1:
            #Circle Area
            if user_shape == 1:
                radius = float(input('Circle radius: '))
                c_area = '{:.2f}'.format(a_circle(radius))
                print(f'Circle area = {c_area}')

            #Rectangle Area
            elif user_shape == 2:
                length = float(input('Rectangle length: '))
                width = float(input('Rectangle width: '))
                r_area = '{:.2f}'.format(a_rectangle(length, width))
                print(f'Rectangle area: {r_area}')

            elif user_shape == 3:
                length = float(input('Square length: '))
                s_area = '{:.2f}'.format(a_square(length))
                print(f'Square area: {s_area}')

            elif user_shape == 4:
                base = float(input('Triangle side 1: '))
                height = float(input('Triangle side 2: '))
                t_area = '{:.2f}'.format(a_triangle(height, base))
                print(f'Triangle area: {t_area}')

        #if Perimeter
        elif comp_select == 2:
            if user_shape == 1:
                radius = float(input('Circle radius: '))
                c_perimeter = '{:.2f}'.format(p_circle(radius))
                print(f'Circle perimeter = {c_perimeter}')

            elif user_shape == 2:
                length = float(input('Rectangle length: '))
                width = float(input('Rectangle width: '))
                r_perimeter = '{:.2f}'.format(p_rectangle(length, width))
                print(f'Rectangle perimeter: {r_perimeter}')

            elif user_shape == 3:
                length = float(input('Square length: '))
                s_perimeter = '{:.2f}'.format(p_square(length))
                print(f'Square perimeter : {s_perimeter}')

            elif user_shape == 4:
                base = float(input('Triangle side 1: '))
                height = float(input('Triangle side 2: '))
                side3 = float(input('Triangle side 3: '))
                t_perimeter = '{:.2f}'.format(p_triangle(base, height, side3))
                print(f'Triangle perimeter: {t_perimeter}')

        qcontinue = str(input('Continue (y/n): ')).lower().strip()
        while (qcontinue == 'y' or qcontinue == 'n') is False:
            qcontinue = str(input('Enter y or n: ')).lower().strip()

        if qcontinue == 'y':
            continue
        elif qcontinue == 'n':
            print('PROGRAM DONE')
            quit()



if __name__ == '__main__':
    main()

