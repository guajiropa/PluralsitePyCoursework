# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new_downloader.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_downloader_dialog(object):
    def setupUi(self, downloader_dialog):
        downloader_dialog.setObjectName("downloader_dialog")
        downloader_dialog.resize(199, 149)
        downloader_dialog.setSizeGripEnabled(False)
        self.verticalLayout = QtWidgets.QVBoxLayout(downloader_dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.url_text = QtWidgets.QLineEdit(downloader_dialog)
        self.url_text.setObjectName("url_text")
        self.verticalLayout.addWidget(self.url_text)
        self.save_location_text = QtWidgets.QLineEdit(downloader_dialog)
        self.save_location_text.setObjectName("save_location_text")
        self.verticalLayout.addWidget(self.save_location_text)
        self.browse_button = QtWidgets.QPushButton(downloader_dialog)
        self.browse_button.setObjectName("browse_button")
        self.verticalLayout.addWidget(self.browse_button)
        self.progress = QtWidgets.QProgressBar(downloader_dialog)
        self.progress.setProperty("value", 0)
        self.progress.setAlignment(QtCore.Qt.AlignCenter)
        self.progress.setObjectName("progress")
        self.verticalLayout.addWidget(self.progress)
        self.download_button = QtWidgets.QPushButton(downloader_dialog)
        self.download_button.setObjectName("download_button")
        self.verticalLayout.addWidget(self.download_button)

        self.retranslateUi(downloader_dialog)
        QtCore.QMetaObject.connectSlotsByName(downloader_dialog)

    def retranslateUi(self, downloader_dialog):
        _translate = QtCore.QCoreApplication.translate
        downloader_dialog.setWindowTitle(_translate("downloader_dialog", "QtPy Downloader"))
        self.url_text.setPlaceholderText(_translate("downloader_dialog", "URL"))
        self.save_location_text.setPlaceholderText(_translate("downloader_dialog", "File save location . . ."))
        self.browse_button.setText(_translate("downloader_dialog", "Browse"))
        self.download_button.setText(_translate("downloader_dialog", "Download"))

