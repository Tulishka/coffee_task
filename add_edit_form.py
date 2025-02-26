from PyQt6.QtWidgets import QDialog, QMessageBox

import db
from UI.ui_add_edit_coffee import Ui_EditForm


class AddEditCoffeeForm(Ui_EditForm, QDialog):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent)
        self.setupUi(self)
        self.coffee_id = coffee_id

        if self.coffee_id:
            self.load_data()

        self.pushButton.clicked.connect(self.save_coffee)

    def load_data(self):

        coffee_data = db.get_coffee(self.coffee_id)
        if coffee_data:
            self.lineEdit.setText(coffee_data[1])
            self.lineEdit_2.setText(coffee_data[2])
            self.comboBox.setCurrentText(coffee_data[3])
            self.textEdit.setPlainText(coffee_data[4])
            self.doubleSpinBox.setValue(coffee_data[5])
            self.spinBox.setValue(coffee_data[6])

    def save_coffee(self):
        name = self.lineEdit.text()
        roast_level = self.lineEdit_2.text()
        ground_or_beans = self.comboBox.currentText()
        taste_description = self.textEdit.toPlainText()
        price = self.doubleSpinBox.value()
        package_volume = self.spinBox.value()

        if not name or not roast_level or not ground_or_beans or not taste_description:
            QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены")
            return

        if db.save_coffee(self.coffee_id, ground_or_beans, name, package_volume, price, roast_level, taste_description):
            self.accept()
        else:
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить данные")
