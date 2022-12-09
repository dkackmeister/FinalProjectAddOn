from controller import *


def main():
    """
    Starts application and displays window
    :return:
    """
    application = QApplication([])
    window = Controller()
    window.show()
    application.exec_()


if __name__ == '__main__':
    main()

