from PyQt5.QtWidgets import*

app = QApplication([])
okno = QWidget()


main QHBoxLayout()
okno.setLayout(main)

line1 = QVBoxLayout()
Line2 = QVBoxLayout()
main.appLayout(line1)
main.appLayout(line2)

b1 = QPushButton('Дальше')
tx1 = QLabel('Результат')
Line.addWindget(b1)
Line.addWindget(tx1)
#tx1.hide()
def nex1:
    tx1.show()
    b1.hide()
b1.clicked.connect(next1)
okno.show()
app.exec_()

