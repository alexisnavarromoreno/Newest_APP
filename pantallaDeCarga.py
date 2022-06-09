# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pantallaDeCarga.ui'
##
## Created by: Qt User Interface Compiler version 6.2.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QProgressBar, QSizePolicy, QVBoxLayout, QWidget,QMessageBox)

class Ui_VentanaDeCarga(object):
    def setupUi(self, VentanaDeCarga):
        if not VentanaDeCarga.objectName():
            VentanaDeCarga.setObjectName(u"VentanaDeCarga")
        VentanaDeCarga.resize(680, 400)
        font = QFont()
        font.setFamilies([u"Segoe UI"])
        font.setPointSize(14)
        VentanaDeCarga.setFont(font)
        icon = QIcon()
        icon.addFile(u"iconoNewest.ico", QSize(), QIcon.Normal, QIcon.Off)
        VentanaDeCarga.setWindowIcon(icon)
        self.centralwidget = QWidget(VentanaDeCarga)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.contenedor = QFrame(self.centralwidget)
        self.contenedor.setObjectName(u"contenedor")
        self.contenedor.setStyleSheet(u"QFrame{\n"
"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"}")
        self.contenedor.setFrameShape(QFrame.StyledPanel)
        self.contenedor.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.contenedor)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.labelTituloApp = QLabel(self.contenedor)
        self.labelTituloApp.setObjectName(u"labelTituloApp")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setPointSize(40)
        self.labelTituloApp.setFont(font1)
        self.labelTituloApp.setStyleSheet('margin: 5% auto;')
        self.labelTituloApp.setScaledContents(True)
        self.labelTituloApp.setAlignment(Qt.AlignCenter)
        self.labelTituloApp.setWordWrap(True)
        self.labelTituloApp.setMargin(0)
        self.labelTituloApp.setIndent(10)

        self.verticalLayout_2.addWidget(self.labelTituloApp)

        self.labelDescripcion = QLabel(self.contenedor)
        self.labelDescripcion.setObjectName(u"labelDescripcion")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(16)
        self.labelDescripcion.setFont(font2)
        self.labelDescripcion.setStyleSheet(u"color:rgb(191, 191, 191)")
        self.labelDescripcion.setScaledContents(True)
        self.labelDescripcion.setAlignment(Qt.AlignCenter)
        self.labelDescripcion.setWordWrap(True)
        self.labelDescripcion.setMargin(0)
        self.labelDescripcion.setIndent(10)

        self.verticalLayout_2.addWidget(self.labelDescripcion)

        self.progressBar = QProgressBar(self.contenedor)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar{\n"
"	\n"
"	background-color: rgb(255, 238, 102);\n"
"	color: rgb(75, 75, 75);\n"
"	border-style: none;\n"
"	border-radius: 10px;\n"
"	margin: 5% auto;\n"
"}\n"
"QProgressBar::chunk{\n"
"border-radius:10px;\n"
"	background-color: qlineargradient(spread:pad, x1:0, y1:0.426, x2:1, y2:0.443182, stop:0 rgba(255, 238, 102, 255), stop:1 rgba(255, 255, 255, 255));\n"
"}")
        self.progressBar.setValue(20)
        self.progressBar.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.progressBar)

        self.labelCargando = QLabel(self.contenedor)
        self.labelCargando.setObjectName(u"labelCargando")
        font3 = QFont()
        font3.setFamilies([u"Segoe UI"])
        font3.setPointSize(10)
        self.labelCargando.setFont(font3)
        self.labelCargando.setStyleSheet(u"color:rgb(191, 191, 191)")
        self.labelCargando.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.labelCargando)


        self.verticalLayout.addWidget(self.contenedor)

        self.mensajeNoInternet =  QMessageBox()
        self.mensajeNoInternet.setObjectName(u"mensajeNoInternet")
        self.mensajeNoInternet.setText("No hay internet")
        self.mensajeNoInternet.setIcon(QMessageBox.Critical)
        self.mensajeNoInternet.setText('Error en la conexion a internet')
        self.mensajeNoInternet.setInformativeText('Intentelo de nuevo más tarde o pongase en contacto con su proveedor de Internet')
        self.mensajeNoInternet.setWindowTitle('ERROR')
        self.mensajeNoInternet.setStandardButtons(QMessageBox.Ok)
        self.mensajeNoInternet.setStyleSheet('''
        
        QMessageBox{
            background:#FFF67F;color:#000
            }
            QLabel{
                background:transparent;color:#000
                }
        ''')


        

        VentanaDeCarga.setCentralWidget(self.centralwidget)

        self.retranslateUi(VentanaDeCarga)

        QMetaObject.connectSlotsByName(VentanaDeCarga)
    # setupUi

    def retranslateUi(self, VentanaDeCarga):
        VentanaDeCarga.setWindowTitle(QCoreApplication.translate("VentanaDeCarga", u"Newest", None))
        self.labelTituloApp.setText(QCoreApplication.translate("VentanaDeCarga", u"NE<strong>W</strong>EST", None))
        self.labelDescripcion.setText(QCoreApplication.translate("VentanaDeCarga", u"TU <strong>APP </strong>DE NOVEDADES", None))
        self.labelCargando.setText(QCoreApplication.translate("VentanaDeCarga", u"cargando...", None))
    # retranslateUi

