from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class PlayerNumberDialog(QDialog):
	
	def __init__(self):
		super(PlayerNumberDialog, self).__init__()

		self.setWindowTitle(u"Введите количество игроков")
		self.resize(300,50)
		layout = QHBoxLayout()

		self.playerCounter = QSpinBox()
		self.playerCounter.setMinimum(2)
		self.playerCounter.setMaximum(4)

		btn = QPushButton("OK")
		btn.clicked.connect(self.accept)

		layout.addWidget(self.playerCounter)
		layout.addWidget(btn)

		self.setLayout(layout)


class PlayerNameWidget(QWidget):

	def __init__(self, playerCounter):
		super(PlayerNameWidget, self).__init__()

		self.input = QLineEdit("Player%d" %playerCounter)

		layout = QHBoxLayout()
		layout.addWidget(QLabel(u"Игрок %d: " %playerCounter))
		layout.addWidget(self.input)

		self.setLayout(layout)


class PlayerNameDialog(QDialog):
	
	def __init__(self, playerNumber):
		super(PlayerNameDialog, self).__init__()

		self.setWindowTitle(u"Ведите имена игроков")
		self.resize(300,50)
		layout = QVBoxLayout()
		self.players = []

		btn = QPushButton("OK")
		btn.clicked.connect(self.accept)

		for i in range(1, playerNumber+1):
			widget = PlayerNameWidget(i)
			self.players.append(widget)
			layout.addWidget(widget)
		layout.addWidget(btn)

		self.setLayout(layout)

