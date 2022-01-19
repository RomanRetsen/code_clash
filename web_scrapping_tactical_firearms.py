import sys
import time
import itertools
import requests
from bs4 import BeautifulSoup
import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc

#main GUI class
class IsProductAvailableForm(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_gui()
        self.cycle_check()

#layouting GUI widgets
    def setup_gui(self):
        self.vertical_lo = qtw.QVBoxLayout()
        self.data_frame_box = qtw.QHBoxLayout()
        self.button_frame_box = qtw.QHBoxLayout()
        self.data_frame = qtw.QFrame()
        self.buttons_frame = qtw.QFrame()
        self.text_area = qtw.QPlainTextEdit()
        self.close_btn = qtw.QPushButton('Got it')

        self.setLayout(self.vertical_lo)
        self.data_frame.setLayout(self.data_frame_box)
        self.buttons_frame.setLayout(self.button_frame_box)

        self.button_frame_box.addWidget(self.close_btn, alignment=qtc.Qt.AlignRight)
        self.data_frame_box.addWidget(self.text_area)
        self.vertical_lo.addWidget(self.data_frame, stretch=1)
        self.vertical_lo.addWidget(self.buttons_frame)
        self.text_area.insertPlainText("Product in stock\n")

        self.close_btn.clicked.connect(self.close)

        self.setGeometry(0, 0, 1300, 150)

# "until success" loop function checking if product is back in stock
# Currently there is one product in stock matching the pattern,
# that's why only condition 'count_of_available > 1' will trigger pop-up window
    def cycle_check(self):
        URL = "http://www.tacticalimports.ca/nonrestricted-firearms-c-1.html"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, "html.parser")
        while True:
            count_of_available = 0
            self.text_area.clear()
            for item in itertools.chain(soup.find_all("tr", class_="productListing-odd"), soup.find_all("tr", class_="productListing-even")):
                td_elements = item.find("td", class_="productListing-data", attrs={"align": "right"})
                tag_to_str = str(td_elements)
                if tag_to_str.find("Sold Out") == -1 and not tag_to_str.find("type-81") == -1:
                    count_of_available += 1
                    self.text_area.insertPlainText(tag_to_str)
                    print(tag_to_str)
            if count_of_available > 1:
                qtc.QCoreApplication.processEvents()
                self.show()
                break

            time.sleep(3600) # run the check every 1 hr

if __name__ == '__main__':
    app=qtw.QApplication(sys.argv)
    form=IsProductAvailableForm()
    # form.show()
    sys.exit(app.exec_())


