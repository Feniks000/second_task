import os
import sys
import PyQt5
from random import randint
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('UI.ui', self)
        self.pushButton.clicked.connect(self.circle)
        self.label = QLabel()
        canvas = QPixmap(800, 800)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.pushButton, 0, 0, alignment=Qt.AlignLeft)
        layout.addWidget(self.label, 1, 0)

    def circle(self):
        x, y = [randint(10, 700) for i in range(2)]
        r = randint(10, 100)
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor(255, 255, 0))
        painter.setPen(pen)
        painter.drawEllipse(x, y, r, r)
        painter.end()
        self.update()

    def err_message(self, text: str) -> None:
        QMessageBox().warning(self, 'Error', text)


if __name__ == '__main__':
    #     file = open('UI.ui', 'w')
    #     file.write("""<?xml version="1.0" encoding="UTF-8"?>
    # <ui version="4.0">
    #  <class>MainWindow</class>
    #  <widget class="QMainWindow" name="MainWindow">
    #   <property name="geometry">
    #    <rect>
    #     <x>0</x>
    #     <y>0</y>
    #     <width>800</width>
    #     <height>600</height>
    #    </rect>
    #   </property>
    #   <property name="windowTitle">
    #    <string>MainWindow</string>
    #   </property>
    #   <widget class="QWidget" name="centralwidget">
    #    <widget class="QPushButton" name="pushButton">
    #     <property name="geometry">
    #      <rect>
    #       <x>10</x>
    #       <y>10</y>
    #       <width>151</width>
    #       <height>51</height>
    #      </rect>
    #     </property>
    #     <property name="text">
    #      <string>Generate.</string>
    #     </property>
    #    </widget>
    #   </widget>
    #  </widget>
    #  <resources/>
    #  <connections/>
    # </ui>
    # """)
    # file.close()
    app = QApplication(sys.argv)
    mn = Main()
    mn.show()
    sys.exit(app.exec())
