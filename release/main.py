import sys
import sqlite3

from ui.mainForm import Ui_MainWindow
from ui.addEditCoffeeForm import Ui_Dialog

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QDialog,
    QInputDialog,
    QTableWidgetItem,
    QAction,
)


class AddEditCoffeeDialog(QDialog, Ui_Dialog):

    def __init__(self, parent, data=None):
        super().__init__(parent)
        self.setupUi(self)
        if data:
            cur, id = data
            old_data = cur.execute("""SELECT * FROM Coffee WHERE id = {}""".format(id)).fetchall()[0]
            self.sort.setText(old_data[1])
            self.roast.setText(old_data[2])
            self.is_ground.setCurrentIndex((old_data[3] - 1) % 2)
            self.description.setPlainText(old_data[4])
            self.price.setValue(old_data[5])
            self.volume.setValue(old_data[6])
        else:
            self.label_id.setVisible(False)
            self.id.setBisible(False)

    def getData(self):
        data = {
            'sort': self.sort.text(),
            'roast': self.roast.text(),
            'is_ground': self.is_ground.currentText() == 'Yes',
            'description': self.description.toPlainText(),
            'price': self.price.value(),
            'volume': self.volume.value()
        }
        return data

    @staticmethod
    def getCoffeeData(parent, edit_data=(0,)):
        if edit_data[0]:
            dialog = AddEditCoffeeDialog(parent, edit_data[1:])
        else:
            dialog = AddEditCoffeeDialog(parent)

        if dialog.exec_() == QDialog.Accepted:
            data = dialog.getData()
            return (1, data)
        return (0, [])


class Coffee(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.initBar()
        with sqlite3.connect('data/coffee.db') as self.con:
            self.cur = self.con.cursor()

        title = ["id", "sort", "roast", "is_ground", "description", "price", "volume"]
        self.tableWidget.setColumnCount(len(title))
        self.tableWidget.setHorizontalHeaderLabels(title)
        self.loadTable()
    
    def initBar(self):

        bar = self.menuBar()

        fileMenu = bar.addMenu('File')

        add_coffee_action = QAction('Add coffee', self)
        add_coffee_action.setShortcut("Ctrl+N")
        add_coffee_action.triggered.connect(self.addCoffee)

        fileMenu.addAction(add_coffee_action)

        editMenu = bar.addMenu('Edit')

        edit_coffee_action = QAction('Edit coffee', self)
        edit_coffee_action.setShortcut('Ctrl+E')
        edit_coffee_action.triggered.connect(self.edit_coffee)

        editMenu.addAction(edit_coffee_action)
        

    def loadTable(self):
        req = "SELECT * FROM Coffee"
        data = self.cur.execute(req)
        self.tableWidget.setRowCount(0)
        for i, row in enumerate(data):
            self.tableWidget.setRowCount(self.tableWidget.rowCount() + 1)
            for j, elem in enumerate(row):
                if j == 3:
                    elem = 'молотый' if elem else 'в зёрнах' 
                self.tableWidget.setItem(i, j, QTableWidgetItem(str(elem)))
        self.tableWidget.resizeColumnsToContents()
    
    def addCoffee(self):
        res, data = AddEditCoffeeDialog.getCoffeeData(self)
        if res:
            self.cur.execute("""INSERT INTO Coffee (sort, roast, is_ground, description, price, volume)
            VALUES (%(sort)r, %(roast)r, %(is_ground)d, %(description)r, %(price)d, %(volume)d)""" % data)
            self.con.commit()
            self.loadTable()
    
    def edit_coffee(self):
        id = QInputDialog.getInt(self, 'Введите id', '', 1, 1)[0]
        res, data = AddEditCoffeeDialog.getCoffeeData(self, edit_data=(1, self.cur, id))
        data['id'] = id
        if res:
            self.cur.execute("""UPDATE Coffee
            SET sort = %(sort)r, 
            roast = %(roast)r, 
            is_ground = %(is_ground)d, 
            description = %(description)r, 
            price = %(price)d, 
            volume = %(volume)d
            WHERE id = %(id)d""" % data)
            self.con.commit()
            self.loadTable()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    coffee = Coffee()
    coffee.show()
    sys.exit(app.exec_())