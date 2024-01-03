"""
프로그램 엔트리 포인트 모듈입니다.
"""
import sys
from PyQt5.QtWidgets import QApplication
from PyQt_framework.GUI import MainGUI


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainGUI()
    window.setGeometry(100, 100, 1200, 800)
    window.show()
    sys.exit(app.exec_())
