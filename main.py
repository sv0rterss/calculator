from PyQt5.QtWidgets import(QWidget, QApplication, QPushButton, QLabel, QLineEdit, QVBoxLayout, QHBoxLayout)


app = QApplication([])
window = QWidget()

button1 = QPushButton("1")
button2 = QPushButton("2")
button3 = QPushButton("3")
button4 = QPushButton("4")
button5 = QPushButton("5")
button6 = QPushButton("6")
button7 = QPushButton("7")
button8 = QPushButton("8")
button9 = QPushButton("9")
button10 = QPushButton("*")
button11 = QPushButton("0")
button12 = QPushButton("/")
button13 = QPushButton("clear")
button14 = QPushButton("result")
button15 = QPushButton("+")
button16 = QPushButton("-")

label1 = QLabel('Результат')
label2 = QLabel('!')

line1 = QLineEdit()

h1 = QHBoxLayout()
h1.addWidget(button1)
h1.addWidget(button2)
h1.addWidget(button3)
h1.addWidget(button4)

h2 = QHBoxLayout()
h2.addWidget(button5)
h2.addWidget(button6)
h2.addWidget(button7)
h2.addWidget(button8)

h3 = QHBoxLayout()
h3.addWidget(button9)
h3.addWidget(button10)
h3.addWidget(button11)
h3.addWidget(button12)

h4 = QHBoxLayout()
h4.addWidget(button13)
h4.addWidget(button14)
h4.addWidget(button15)
h4.addWidget(button16)

h5 = QHBoxLayout()
h5.addWidget(label1)
h5.addWidget(label2)


v1 = QVBoxLayout()
v1.addWidget(line1)
v1.addLayout(h1)
v1.addLayout(h2)
v1.addLayout(h3)
v1.addLayout(h4)
v1.addLayout(h5)

window.setLayout(v1)





window.show()
app.exec()