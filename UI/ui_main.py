from PyQt6.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableWidget, QPushButton


class Ui_MainForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(916, 613)
        self.verticalLayoutWidget = QWidget(Form)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 60, 911, 551))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.tableWidget = QTableWidget(self.verticalLayoutWidget)
        self.tableWidget.setObjectName(u"tableWidget")

        self.verticalLayout.addWidget(self.tableWidget)

        self.add_button = QPushButton(Form)
        self.add_button.setObjectName(u"add_button")
        self.add_button.setGeometry(QRect(10, 10, 131, 41))
        self.edit_button = QPushButton(Form)
        self.edit_button.setObjectName(u"edit_button")
        self.edit_button.setGeometry(QRect(150, 10, 131, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.add_button.setText(QCoreApplication.translate(
            "Form",
            u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c",
            None)
        )
        self.edit_button.setText(QCoreApplication.translate(
            "Form",
            u"\u0418\u0437\u043c\u0435\u043d\u0438\u0442\u044c \u0437\u0430\u043f\u0438\u0441\u044c",
            None)
        )
    # retranslateUi
