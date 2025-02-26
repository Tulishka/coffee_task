import sqlite3

from PyQt6.QtWidgets import QDialog, QMessageBox
from PyQt6.uic import loadUi


class AddEditCoffeeForm(QDialog):
    def __init__(self, parent=None, coffee_id=None):
        super().__init__(parent)
        loadUi("addEditCoffeeForm.ui", self)
        self.coffee_id = coffee_id

        if self.coffee_id:
            self.load_data()

        self.pushButton.clicked.connect(self.save_coffee)

    def load_data(self):
        try:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            cur.execute("SELECT * FROM coffee WHERE id=?", (self.coffee_id,))
            coffee_data = cur.fetchone()

            if coffee_data:
                self.lineEdit.setText(coffee_data[1])
                self.lineEdit_2.setText(coffee_data[2])
                self.comboBox.setCurrentText(coffee_data[3])
                self.textEdit.setPlainText(coffee_data[4])
                self.doubleSpinBox.setValue(coffee_data[5])
                self.spinBox.setValue(coffee_data[6])

            con.close()
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")

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

        try:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()

            if self.coffee_id:
                cur.execute("""
                    UPDATE coffee SET
                    name=?, roast_level=?, ground_or_beans=?, taste_description=?, price=?, package_volume=?
                    WHERE id=?
                """, (name, roast_level, ground_or_beans, taste_description, price, package_volume, self.coffee_id))
            else:
                cur.execute("""
                    INSERT INTO coffee (name, roast_level, ground_or_beans, taste_description, price, package_volume)
                    VALUES (?, ?, ?, ?, ?, ?)
                """, (name, roast_level, ground_or_beans, taste_description, price, package_volume))

            con.commit()
            con.close()
            self.accept()
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")
            QMessageBox.critical(self, "Ошибка", "Не удалось сохранить данные")
