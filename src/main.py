import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from main_window import MainWindow
from display import Display
from info import Info
from styles import setupTheme
from buttons import Button
from variables import WINDOW_ICON_PATH

if __name__ == '__main__':
    # Create application
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Set icon
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)

    # Info
    info = Info('2.0 ^ 10.0 = 1024')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Button
    button = Button('Texto do  botao')
    window.addToVLayout(button)

    # Execute the app
    window.adjustFixedSize()

    window.show()
    app.exec()
