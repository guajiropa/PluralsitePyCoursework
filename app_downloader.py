"""
#   Author      :   Robert James Patterson
#   Created     :   5/22/2017
#   Modified    :   5/22/2017
#   Project     :   app_downloader.py
#   Synopsis    :   Downloads files from a URL provided by the end user using Python and Qt5. In this 
#                   example we built our GUI in the QtDesigner, used :
#
#                   'C:\Python36\Scripts\pyuic5.exe <inputfile.ui> --output <outputfile.py>
#                   
#                   to create the python code from the *.ui element created by Qt.
#
"""

from  PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import new_downloader_ui


class AppDownloader(QDialog, new_downloader_ui.Ui_downloader_dialog):
    # NOTE: The second part of the second parameter in the inheritance clause is the
    # form name with a 'Ui_' append to it (this is done by 'pyuic5.exe').
    def __init__(self):
        QDialog.__init__(self)
        # This next call is required by Qt
        self.setupUi(self)

        self.progress.setValue(50)
        self.url_text.setText("http//www.google.com")


def main():
    app = QApplication(sys.argv)
    appDownloader = AppDownloader()
    appDownloader.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()