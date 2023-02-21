import os
import socket
import psutil
import platform
import pandas as pd
from datetime import datetime
from PyQt5 import QtWidgets, QtGui
import sys


class SystemScanner(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(100, 100, 500, 500)
        self.setWindowTitle('System Scanner')

        self.output = QtWidgets.QTextEdit(self)
        self.output.setGeometry(10, 10, 480, 400)
        self.output.setStyleSheet("background-color:black; color:cyan;")

        self.scan_button = QtWidgets.QPushButton('SCAN', self)
        self.scan_button.setGeometry(200, 420, 100, 40)
        self.scan_button.clicked.connect(self.scan)

    def update_output(self, text):
        """Helper function to update the text area with the given text"""
        self.output.moveCursor(QtGui.QTextCursor.End)
        self.output.insertPlainText(text)
        QtWidgets.QApplication.processEvents()

    def scan(self):
        self.output.clear()

        self.update_output("Scanning system...\n")

        pc_name = socket.gethostname()
        ip_address = socket.gethostbyname(pc_name)

        self.update_output(f"PC Name: {pc_name}\n")
        self.update_output(f"IP Address: {ip_address}\n")

        self.update_output("Getting drive information...\n")

        drives = psutil.disk_partitions()
        drive_info = []
        for drive in drives:
            drive_name = drive.device.split(':')[0]
            usage = psutil.disk_usage(drive.mountpoint)
            used_space = round((usage.total - usage.free) / usage.total * 100)
            drive_info.append([drive_name, used_space])

        self.update_output("Drive Information:\n")
        for drive in drive_info:
            self.update_output(f"{drive[0]}: {drive[1]:.2f}% USED\n")

        self.update_output("Getting RAM and CPU usage...\n")

        ram_info = psutil.virtual_memory()
        ram_usage = ram_info.percent

        cpu_usage = psutil.cpu_percent()

        self.update_output(f"RAM Usage: {ram_usage}%\n")
        self.update_output(f"CPU Usage: {cpu_usage}%\n")

        self.update_output("Getting OS information...\n")

        os_info = platform.system() + ' ' + platform.release()

        self.update_output(f"OS: {os_info}\n")

        self.update_output("Saving system scan results to file...\n")

        data = {'PC Name': [pc_name], 'IP Address': [ip_address], 'OS': [os_info], 'RAM Usage %': [ram_usage],
                'CPU Usage %': [cpu_usage]}

        for drive in drive_info:
            data[drive[0]] = [drive[1]]

        df = pd.DataFrame(data)

        self.update_output("Saving scan results to an Excel file...")
        try:
            with pd.ExcelWriter(os.path.join(os.getcwd(), 'sys_can_res_{}.xlsx'.format(
                    datetime.now().strftime('%Y%m%d_%H%M%S')))) as writer:
                df.to_excel(writer, index=False)
                workbook = writer.book
                worksheet = writer.sheets['Sheet1']
                green_format = workbook.add_format({'bg_color': '#C6EFCE', 'font_color': '#006100'})
                red_format = workbook.add_format({'bg_color': '#FFC7CE', 'font_color': '#9C0006'})

                for i in range(df.shape[0]):
                    for j in range(df.shape[1]):
                        cell_value = df.iloc[i, j]
                        if isinstance(cell_value, (int, float)):
                            if cell_value > 60:
                                worksheet.write(i + 1, j, cell_value, red_format)
                            else:
                                worksheet.write(i + 1, j, cell_value, green_format)
        except Exception as e:
            self.update_output("Error saving scan results to an Excel file: {}".format(str(e)))
        else:
            self.update_output(
                "Scan results saved to file: sys_can_res_{}.xlsx".format(datetime.now().strftime('%Y%m%d_%H%M%S')))

        self.update_output("\nScan Results:\n")
        for i in range(df.shape[0]):
            for j in range(df.shape[1]):
                cell_value = df.iloc[i, j]
                if isinstance(cell_value, (int, float)):
                    if cell_value > 60:
                        self.output.setTextColor(QtGui.QColor('red'))
                    else:
                        self.output.setTextColor(QtGui.QColor('green'))
                else:
                    self.output.setTextColor(QtGui.QColor('cyan'))
                self.output.insertPlainText(str(cell_value) + '\t')
            self.update_output("")  # Add a newline after each row
        self.update_output("Scan complete.")


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = SystemScanner()
    window.show()
    try:
        sys.exit(app.exec_())
    except Exception as e:
        print(e)
