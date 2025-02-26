import sqlite3
import sys

from PyQt6.QtWidgets import QApplication, QTableWidget, QTableWidgetItem, QWidget
from PyQt6.uic import loadUi


class CoffeeApp(QWidget):
    def __init__(self):
        super().__init__()
        loadUi("main.ui", self)
        self.setWindowTitle("Информация о кофе")

        self.table = self.findChild(QTableWidget, "tableWidget")
        self.headers = [
            "ID", "Название сорта", "Степень обжарки", "Молотый/в зернах",
            "Описание вкуса", "Цена", "Объем упаковки"
        ]
        self.table.setColumnCount(len(self.headers))
        self.table.setHorizontalHeaderLabels(self.headers)

        self.load_data()

    def load_data(self):
        try:
            con = sqlite3.connect("coffee.sqlite")
            cur = con.cursor()
            cur.execute("SELECT * FROM coffee")
            rows = cur.fetchall()

            self.table.setRowCount(len(rows))

            for row_index, row_data in enumerate(rows):
                for col_index, col_data in enumerate(row_data):
                    item = QTableWidgetItem(str(col_data))
                    self.table.setItem(row_index, col_index, item)

            con.close()
        except sqlite3.Error as e:
            print(f"Ошибка: {e}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec())
