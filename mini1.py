from PyQt5.QtWidgets import QApplication,QWidget
from PyQt5.Qt import Qt
from PyQt5 import QtCore,QtGui
import sys
import pyscreenshot
import pytesseract
import pyperclip

pytesseract.pytesseract.tesseract_cmd='C:/Program Files (x86)/Tesseract-OCR/tesseract.exe'
class Test(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Image to Text')

        self.setGeometry(100,100,600,400)

        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint | Qt.Dialog)

        self.setWindowState(Qt.WindowFullScreen)

        self.setStyleSheet("Background-color:Black")
        self.setWindowOpacity(0.5)

        QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CrossCursor))

        self.start,self.end=QtCore.QPoint(),QtCore.QPoint()

    def keyPressEvent(self,event):
        if event.key()==65:
            QApplication.quit()
    def mousePressEvent(self, event):
        self.start=self.end=event.pos()
        self.update()

    def mouseMoveEvent(self, event):
        self.end=event.pos()
        self.update()
    def mouseReleaseEvent(self,event):

        x1,x2=sorted((self.start.x(),self.end.x()))
        y1, y2 = sorted((self.start.y(), self.end.y()))


        self.hide()

        img=pyscreenshot.grab(bbox=(x1,y1,x2,y2))

        img_to_text(img)

        QApplication.quit()

def img_to_text(image):
    data=pytesseract.image_to_string(image)

    print(data)

    pyperclip.copy(data)

app=QApplication(sys.argv)
t= Test()
t.show()
sys.exit(app.exec_())