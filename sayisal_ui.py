# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sayısal.ui'
##
## Created by: Qt User Interface Compiler version 6.10.1
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFormLayout,
    QGroupBox, QHBoxLayout, QLabel, QProgressBar,
    QPushButton, QRadioButton, QSizePolicy, QSpinBox,
    QTextEdit, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1366, 836)
        Dialog.setStyleSheet(u"QDialog {\n"
"    background-color: #18181b;\n"
"    color: #e4e4e7;\n"
"}\n"
"")
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-11, -1, 1391, 841))
        self.widget.setStyleSheet(u"")
        self.groupBox = QGroupBox(self.widget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 30, 500, 551))
        font = QFont()
        font.setPointSize(10)
        font.setBold(False)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(u"QGroupBox {\n"
"    background-color: #27272a;\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 12px;\n"
"    margin-top: 18px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #a1a1aa;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.verticalLayoutWidget = QWidget(self.groupBox)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(20, 50, 461, 461))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.verticalLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setStyleSheet(u"QLabel {\n"
"    background-color: #09090b;\n"
"    border: 2px dashed #3f3f46;\n"
"    border-radius: 10px;\n"
"    color: #71717a;\n"
"}\n"
"")

        self.verticalLayout.addWidget(self.label)

        self.groupBox_3 = QGroupBox(self.widget)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.groupBox_3.setGeometry(QRect(540, 160, 311, 241))
        self.groupBox_3.setFont(font)
        self.groupBox_3.setStyleSheet(u"QGroupBox {\n"
"    background-color: #27272a;\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 12px;\n"
"    margin-top: 18px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #a1a1aa;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.verticalLayoutWidget_3 = QWidget(self.groupBox_3)
        self.verticalLayoutWidget_3.setObjectName(u"verticalLayoutWidget_3")
        self.verticalLayoutWidget_3.setGeometry(QRect(20, 110, 271, 113))
        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.pushButton_3 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        font1 = QFont()
        font1.setPointSize(10)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setStyleSheet(u"QPushButton {\n"
"    background-color: #059669;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 6px;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #10b981;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #047857;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_3)

        self.pushButton_4 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"    background-color: #3b82f6;\n"
"    color: white;\n"
"    border-radius: 8px;\n"
"    padding: 8px 16px;\n"
"    font-size: 14px;\n"
"    font-weight: bold;\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: #60a5fa;\n"
"}\n"
"QPushButton:pressed {\n"
"    background-color: #2563eb;\n"
"}\n"
"QPushButton:disabled {\n"
"    background-color: #1e293b;\n"
"    color: #475569;\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.verticalLayoutWidget_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        font2 = QFont()
        font2.setBold(True)
        self.pushButton_5.setFont(font2)
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"    background-color: #3f3f46;\n"
"    color: #f4f4f5;\n"
"    border: 1px solid #52525b;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    font-weight: 600;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #52525b;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #27272a;\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.pushButton_5)

        self.spinBox = QSpinBox(self.groupBox_3)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setGeometry(QRect(30, 60, 251, 31))
        self.label_9 = QLabel(self.groupBox_3)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(30, 35, 241, 21))
        self.groupBox_2 = QGroupBox(self.widget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(860, 30, 500, 801))
        self.groupBox_2.setFont(font)
        self.groupBox_2.setStyleSheet(u"QGroupBox {\n"
"    background-color: #27272a;\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 12px;\n"
"    margin-top: 18px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #a1a1aa;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.horizontalLayoutWidget = QWidget(self.groupBox_2)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(20, 660, 461, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.horizontalLayoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        font3 = QFont()
        font3.setPointSize(11)
        font3.setBold(True)
        self.pushButton.setFont(font3)
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"    background-color: #8b5cf6;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 10.5pt;\n"
"    font-weight: 600;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a78bfa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7c3aed;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #27272a;\n"
"    color: #52525b;\n"
"    border: 2px solid #52525b;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_2 = QPushButton(self.horizontalLayoutWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setFont(font3)
        self.pushButton_2.setStyleSheet(u"QPushButton {\n"
"    background-color: #8b5cf6;\n"
"    border: none;\n"
"    border-radius: 12px;\n"
"    padding: 8px 16px;\n"
"    font-size: 10.5pt;\n"
"    font-weight: 600;\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: #a78bfa;\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background-color: #7c3aed;\n"
"}\n"
"\n"
"QPushButton:disabled {\n"
"    background-color: #27272a;\n"
"    color: #52525b;\n"
"    border: 2px solid #52525b;\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.pushButton_2)

        self.verticalLayoutWidget_2 = QWidget(self.groupBox_2)
        self.verticalLayoutWidget_2.setObjectName(u"verticalLayoutWidget_2")
        self.verticalLayoutWidget_2.setGeometry(QRect(20, 50, 461, 461))
        self.verticalLayout_2 = QVBoxLayout(self.verticalLayoutWidget_2)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.verticalLayoutWidget_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"QLabel {\n"
"    background-color: #09090b;\n"
"    border: 2px dashed #3f3f46;\n"
"    border-radius: 10px;\n"
"    color: #71717a;\n"
"}\n"
"")

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.groupBox_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(140, 550, 251, 71))
        font4 = QFont()
        font4.setPointSize(14)
        self.label_3.setFont(font4)
        self.label_3.setAlignment(Qt.AlignCenter)
        self.textEdit = QTextEdit(self.widget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(30, 590, 501, 241))
        self.textEdit.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid #3f3f46;\n"
"    background-color: #18181b;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: #22d3ee;\n"
"    font-family: Consolas, \"Courier New\", monospace;\n"
"    font-size: 11pt;\n"
"}\n"
"")
        self.textEdit.setReadOnly(True)
        self.groupBox_4 = QGroupBox(self.widget)
        self.groupBox_4.setObjectName(u"groupBox_4")
        self.groupBox_4.setGeometry(QRect(540, 30, 311, 131))
        self.groupBox_4.setFont(font)
        self.groupBox_4.setStyleSheet(u"QGroupBox {\n"
"    background-color: #27272a;\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 12px;\n"
"    margin-top: 18px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #a1a1aa;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.radioButton = QRadioButton(self.groupBox_4)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(10, 30, 221, 20))
        self.radioButton.setStyleSheet(u"QCheckBox, QRadioButton {\n"
"    spacing: 6px;\n"
"}\n"
"")
        self.formLayoutWidget_2 = QWidget(self.groupBox_4)
        self.formLayoutWidget_2.setObjectName(u"formLayoutWidget_2")
        self.formLayoutWidget_2.setGeometry(QRect(10, 90, 271, 39))
        self.formLayout_2 = QFormLayout(self.formLayoutWidget_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.formLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.formLayoutWidget_2)
        self.label_8.setObjectName(u"label_8")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_8)

        self.comboBox = QComboBox(self.formLayoutWidget_2)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setStyleSheet(u"QComboBox {\n"
"    background-color: #27272a;\n"
"    color: #f4f4f5;\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 8px;\n"
"    padding: 4px;\n"
"}\n"
"\n"
"QComboBox::drop-down {\n"
"    border: none;\n"
"}\n"
"")

        self.formLayout_2.setWidget(0, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.radioButton_2 = QRadioButton(self.groupBox_4)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(10, 60, 221, 20))
        self.radioButton_2.setStyleSheet(u"QCheckBox, QRadioButton {\n"
"    spacing: 6px;\n"
"}\n"
"")
        self.groupBox_5 = QGroupBox(self.widget)
        self.groupBox_5.setObjectName(u"groupBox_5")
        self.groupBox_5.setGeometry(QRect(540, 400, 311, 231))
        self.groupBox_5.setFont(font)
        self.groupBox_5.setStyleSheet(u"QGroupBox {\n"
"    background-color: #27272a;\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 12px;\n"
"    margin-top: 18px;\n"
"    padding: 10px;\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    subcontrol-position: top left;\n"
"    padding: 0 8px;\n"
"    color: #a1a1aa;\n"
"    font-weight: bold;\n"
"}\n"
"")
        self.formLayoutWidget = QWidget(self.groupBox_5)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 30, 291, 193))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.progressBar = QProgressBar(self.formLayoutWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 6px;\n"
"    background-color: #27272a;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #a78bfa;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.progressBar.setValue(24)

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.progressBar)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.progressBar_2 = QProgressBar(self.formLayoutWidget)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 6px;\n"
"    background-color: #27272a;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #a78bfa;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.progressBar_2.setValue(24)

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.progressBar_2)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.progressBar_3 = QProgressBar(self.formLayoutWidget)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 6px;\n"
"    background-color: #27272a;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #a78bfa;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.progressBar_3.setValue(24)

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.progressBar_3)

        self.label_7 = QLabel(self.formLayoutWidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_7)

        self.progressBar_4 = QProgressBar(self.formLayoutWidget)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 6px;\n"
"    background-color: #27272a;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #a78bfa;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.progressBar_4.setValue(24)

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.progressBar_4)

        self.label_10 = QLabel(self.formLayoutWidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font1)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_10)

        self.progressBar_5 = QProgressBar(self.formLayoutWidget)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 6px;\n"
"    background-color: #27272a;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #a78bfa;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.progressBar_5.setValue(24)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.progressBar_5)

        self.label_11 = QLabel(self.formLayoutWidget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setFont(font1)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_11)

        self.progressBar_6 = QProgressBar(self.formLayoutWidget)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setStyleSheet(u"QProgressBar {\n"
"    border: 1px solid #3f3f46;\n"
"    border-radius: 6px;\n"
"    background-color: #27272a;\n"
"    text-align: center;\n"
"    color: white;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background-color: #a78bfa;\n"
"    border-radius: 6px;\n"
"}\n"
"")
        self.progressBar_6.setValue(24)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.progressBar_6)

        self.textEdit_2 = QTextEdit(self.widget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(540, 640, 311, 191))
        self.textEdit_2.setStyleSheet(u"QTextEdit {\n"
"    border: 1px solid #3f3f46;\n"
"    background-color: #18181b;\n"
"    border-radius: 8px;\n"
"    padding: 8px;\n"
"    color: #22d3ee;\n"
"    font-family: Consolas, \"Courier New\", monospace;\n"
"    font-size: 11pt;\n"
"}\n"
"")
        self.textEdit_2.setReadOnly(True)

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"Canl\u0131 Kamera \u2013 Duygu Alg\u0131lama", None))
        self.label.setText("")
        self.groupBox_3.setTitle(QCoreApplication.translate("Dialog", u"\u0130\u015flemler", None))
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"Resim Olu\u015ftur", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"Duraklat", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"Her \u015feyi S\u0131f\u0131rla", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"Otomatik Resim \u00dcretme S\u0131kl\u0131\u011f\u0131", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"Resimler", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u2aa1", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u2aa2", None))
        self.label_2.setText("")
        self.label_3.setText("")
        self.groupBox_4.setTitle(QCoreApplication.translate("Dialog", u"\u00dcretim Modu", None))
        self.radioButton.setText(QCoreApplication.translate("Dialog", u"Tek Seferlik \u00dcretim", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"Stil:", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Dialog", u"Realistic", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Dialog", u"Anime", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("Dialog", u"Pixel Art", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("Dialog", u"Cyberpunk", None))

        self.radioButton_2.setText(QCoreApplication.translate("Dialog", u"Otomatik \u00dcretim", None))
        self.groupBox_5.setTitle(QCoreApplication.translate("Dialog", u"Duygular", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"Mutlu", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"K\u0131zg\u0131n", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u00dczg\u00fcn", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"Sakin", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"Korku", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u015ea\u015fk\u0131n", None))
    # retranslateUi

