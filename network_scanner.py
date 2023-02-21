import sys
import threading
import time

import nmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QPlainTextEdit, QPushButton, QLineEdit, QLabel


class NmapScanner(QMainWindow):
    def __init__(self):
        super().__init__()

        # Create the GUI components
        self.setWindowTitle("Nmap Scanner")
        self.resize(400, 300)

        self.subnet_label = QLabel("Enter subnet (e.g. 192.168.1.0/24):", self)
        self.subnet_label.move(20, 20)
        self.subnet_label.resize(300, 30)

        self.subnet_input = QLineEdit(self)
        self.subnet_input.move(20, 50)
        self.subnet_input.resize(200, 30)

        self.scan_button = QPushButton("Scan", self)
        self.scan_button.move(20, 100)
        self.scan_button.clicked.connect(self.scan)

        self.result_label = QLabel("Scan results:", self)
        self.result_label.move(20, 150)

        self.result_area = QPlainTextEdit(self)
        self.result_area.move(20, 180)
        self.result_area.resize(360, 100)
        self.result_area.setReadOnly(True)

        self.show()

    def scan(self):
        # Get the subnet from the input field
        subnet = self.subnet_input.text()

        # Create a new Nmap scanner
        nm = nmap.PortScanner()

        # Run the Nmap scan with the given subnet
        nm.scan(hosts=subnet, arguments='-sn')

        # Get the list of hosts that were found
        hosts = nm.all_hosts()

        # Output the results to the text area
        self.result_area.clear()
        if len(hosts) == 0:
            self.result_area.insertPlainText("No hosts found.\n")
        else:
            self.result_area.insertPlainText("Hosts found:\n")
            for host in hosts:
                self.result_area.insertPlainText(host + "\n")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    scanner = NmapScanner()
    sys.exit(app.exec_())
