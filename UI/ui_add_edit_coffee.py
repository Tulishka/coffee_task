from PyQt6.QtCore import QRect, QMetaObject, QCoreApplication
from PyQt6.QtWidgets import QWidget, QFormLayout, QLabel, QLineEdit, QComboBox, QTextEdit, QDoubleSpinBox, QSpinBox, \
    QPushButton


class Ui_EditForm(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(357, 269)
        self.formLayoutWidget = QWidget(Form)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(10, 10, 341, 213))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label = QLabel(self.formLayoutWidget)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.LabelRole, self.label)

        self.lineEdit = QLineEdit(self.formLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.formLayout.setWidget(0, QFormLayout.ItemRole.FieldRole, self.lineEdit)

        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.LabelRole, self.label_2)

        self.lineEdit_2 = QLineEdit(self.formLayoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.formLayout.setWidget(1, QFormLayout.ItemRole.FieldRole, self.lineEdit_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.LabelRole, self.label_3)

        self.comboBox = QComboBox(self.formLayoutWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")

        self.formLayout.setWidget(2, QFormLayout.ItemRole.FieldRole, self.comboBox)

        self.label_4 = QLabel(self.formLayoutWidget)
        self.label_4.setObjectName(u"label_4")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.LabelRole, self.label_4)

        self.textEdit = QTextEdit(self.formLayoutWidget)
        self.textEdit.setObjectName(u"textEdit")

        self.formLayout.setWidget(3, QFormLayout.ItemRole.FieldRole, self.textEdit)

        self.label_5 = QLabel(self.formLayoutWidget)
        self.label_5.setObjectName(u"label_5")

        self.formLayout.setWidget(4, QFormLayout.ItemRole.LabelRole, self.label_5)

        self.doubleSpinBox = QDoubleSpinBox(self.formLayoutWidget)
        self.doubleSpinBox.setObjectName(u"doubleSpinBox")
        self.doubleSpinBox.setMaximum(100000.000000000000000)

        self.formLayout.setWidget(4, QFormLayout.ItemRole.FieldRole, self.doubleSpinBox)

        self.label_6 = QLabel(self.formLayoutWidget)
        self.label_6.setObjectName(u"label_6")

        self.formLayout.setWidget(5, QFormLayout.ItemRole.LabelRole, self.label_6)

        self.spinBox = QSpinBox(self.formLayoutWidget)
        self.spinBox.setObjectName(u"spinBox")
        self.spinBox.setMaximum(10000)

        self.formLayout.setWidget(5, QFormLayout.ItemRole.FieldRole, self.spinBox)

        self.pushButton = QPushButton(Form)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 220, 91, 41))

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u043d\u0430\u0437\u0432\u0430\u043d\u0438\u0435 \u0441\u043e\u0440\u0442\u0430", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u0441\u0442\u0435\u043f\u0435\u043d\u044c \u043e\u0431\u0436\u0430\u0440\u043a\u0438", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u043c\u043e\u043b\u043e\u0442\u044b\u0439/\u0432 \u0437\u0435\u0440\u043d\u0430\u0445", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("Form", u"\u041c\u043e\u043b\u043e\u0442\u044b\u0439", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("Form", u"\u0412 \u0437\u0435\u0440\u043d\u0430\u0445", None))

        self.label_4.setText(QCoreApplication.translate("Form", u"\u043e\u043f\u0438\u0441\u0430\u043d\u0438\u0435 \u0432\u043a\u0443\u0441\u0430", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u0446\u0435\u043d\u0430", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u043e\u0431\u044a\u0435\u043c \u0443\u043f\u0430\u043a\u043e\u0432\u043a\u0438", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u0421\u043e\u0445\u0440\u0430\u043d\u0438\u0442\u044c", None))
    # retranslateUi

