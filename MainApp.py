import time
import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *

from MainForm import *


class mainWindow(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    # Ui_MainWindow.verticalLayout.addWidget()

    app = QApplication(sys.argv)
    window = mainWindow()
    window.show()

    player = QMediaPlayer()
    # mc = QMediaContent(QUrl.fromLocalFile("/home/johnny/PycharmProjects/Python_1st/assets/videos/mv.mp4"))
    # player.setMedia(mc)
    player.setVolume(100)
    playlist = QMediaPlaylist()
    playlist.addMedia(QMediaContent(QUrl.fromLocalFile("/home/johnny/PycharmProjects/Python_1st/assets/videos/mv.mp4")))
    playlist.setPlaybackMode(QMediaPlaylist.CurrentItemInLoop)
    player.setPlaylist(playlist)
    videoWidget = QVideoWidget()
    palette = QPalette()
    palette.setBrush(QPalette.Background, Qt.black)
    # videoWidget.setPalette(QPalette().setBrush(QPalette.Background,Qt.black))
    player.setVideoOutput(videoWidget)
    videoWidget.show()
    # self.verticalLayout.addWidget(videoWidget)
    player.play()
    window.ui.verticalLayout.addWidget(videoWidget)

    sys.exit(app.exec_())
