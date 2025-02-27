import sys
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from configCalculator import MainWindow, Display, Info, ButtonsGrid
from styles import setupTheme
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
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsGrid)

    # Execute the app
    window.adjustFixedSize()

    window.show()
    app.exec()
