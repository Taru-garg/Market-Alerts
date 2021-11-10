from PyQt6 import QtWidgets, uic
from .alert import Alert
from .alert_utils import read_alerts


class StartScreen(QtWidgets.QMainWindow):
    def __init__(self):
        super(StartScreen, self).__init__()
        uic.loadUi("src/ui/AlertBuilder.ui", self)
        self.childWindow = None
        self.create.clicked.connect(self.show_create_new_alert_ui)
        self.edit.clicked.connect(self.show_edit_old_alert_ui)

    def show_create_new_alert_ui(self):
        if not isinstance(self.childWindow, CreateNewAlertUi):
            self.childWindow = CreateNewAlertUi()
        if not self.childWindow.isVisible():
            self.childWindow.show()

    def show_edit_old_alert_ui(self):
        if not isinstance(self.childWindow, EditOldAlertUi):
            self.childWindow = EditOldAlertUi()
        if not self.childWindow.isVisible():
            self.childWindow.show()


class CreateNewAlertUi(QtWidgets.QDialog):
    def __init__(self):
        super(CreateNewAlertUi, self).__init__()
        uic.loadUi("src/ui/AlertBuilder_CreateDialog.ui", self)
        self.setModal(True)
        self.createAlert.clicked.connect(self.pull_and_set_details)
        self.cancel.clicked.connect(lambda: self.close())

    def pull_and_set_details(self):
        email = self.email.text()
        price = self.price.text()
        triggerReason = self.triggerReason.currentText()
        marketName = self.marketName.currentText()
        alert = Alert(email, price, triggerReason, marketName)
        created = alert.save_alert()
        if not created:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Unable to create alert. Please try again")
            msgBox.setWindowTitle("Alrt - Failed :-(")
            msgBox.exec()
        else:
            msgBox = QtWidgets.QMessageBox()
            msgBox.setText("Alert Created!")
            msgBox.setWindowTitle("Alrt - Success :-)")
            msgBox.exec()
        self.clear()

    def clear(self):
        self.email.clear()
        self.price.clear()
        self.triggerReason.SelectedIndex = -1
        self.marketName.SelectedIndex = -1


class EditOldAlertUi(QtWidgets.QDialog):
    def __init__(self):
        super(EditOldAlertUi, self).__init__()
        uic.loadUi("src/ui/AlertBuilder_EditDialog.ui", self)
        self.setModal(True)
        self.save.clicked.connect(lambda: print("Clicked"))
        self.cancel.clicked.connect(lambda: self.close())
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.resizeRowsToContents()
        self.load_ui_alerts()

    def load_ui_alerts(self):
        alerts = read_alerts()
        self.tableWidget.setRowCount(len(alerts))
        table_row = 0
        for alert in alerts:
            try:
                self.tableWidget.setItem(
                    table_row, 0, QtWidgets.QTableWidgetItem(alert.email)
                )
                self.tableWidget.setItem(
                    table_row, 1, QtWidgets.QTableWidgetItem(alert.marketName)
                )
                self.tableWidget.setItem(
                    table_row, 2, QtWidgets.QTableWidgetItem(alert.triggerReason)
                )
                self.tableWidget.setItem(
                    table_row, 3, QtWidgets.QTableWidgetItem(alert.price)
                )
                table_row = table_row + 1
            except:
                continue
        self.tableWidget.resizeColumnsToContents()

    # def remove_selected_rows(self):
    #     rows = get_selected_rows()
    #     for row in rows:
    #         os.remove(row.location)
