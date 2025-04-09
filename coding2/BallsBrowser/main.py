from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
usrurl = "https://www.google.com"
class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(usrurl))
        self.setCentralWidget(self.browser)
        self.showMaximized()
async def meue():
    usrurl = input("Enter URL: ")
meue()
app = QApplication([])
window = Browser()
app.exec_()

