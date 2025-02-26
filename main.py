import os
import sys

from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget, QDialog, QMessageBox

import db
from add_edit_form import AddEditCoffeeForm
from UI.ui_main import Ui_MainForm


class CoffeeApp(Ui_MainForm, QWidget):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Информация о кофе")

        self.table = self.findChild(QTableWidget, "tableWidget")
        self.headers = [
            "ID", "Название сорта", "Степень обжарки", "Молотый/в зернах",
            "Описание вкуса", "Цена", "Объем упаковки"
        ]
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        self.add_button.clicked.connect(self.add_coffee)
        self.edit_button.clicked.connect(self.edit_coffee)

        self.load_data()

    def add_coffee(self):
        dialog = AddEditCoffeeForm(self)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            self.load_data()

    def edit_coffee(self):
        selected_row = self.table.currentRow()
        if selected_row >= 0:
            coffee_id = self.table.item(selected_row, 0).text()
            dialog = AddEditCoffeeForm(self, coffee_id)
            if dialog.exec() == QDialog.DialogCode.Accepted:
                self.load_data()
        else:
            QMessageBox.warning(self, "Ошибка", "Выберите запись для редактирования")

    def load_data(self):
        rows = db.get_coffee_list()
        self.table.setRowCount(len(rows))

        for row_index, row_data in enumerate(rows):
            for col_index, col_data in enumerate(row_data):
                item = QTableWidgetItem(str(col_data))
                self.table.setItem(row_index, col_index, item)


def exception_logger(*args):
    print(*args)
    sys.__excepthook__(*args)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    sys.excepthook = exception_logger
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
