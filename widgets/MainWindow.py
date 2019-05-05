from PyQt4.QtGui import *
from PyQt4.QtCore import *

from widgets.GameField import GameField
from widgets.PlayerField import PlayerField
from widgets.SelectField import SelectField

class MainWindow(QWidget):

	def __init__(self, playerList, letterBag):
		super(MainWindow, self).__init__()
		self.playerList = playerList
		self.letterBag = letterBag
		self.setWindowTitle(u"Скромный интерфейс Scrubble на русском")
	
		# loading all subwindows
		self.playerField = PlayerField(self.playerList)
		self.gameField = GameField(self.letterBag)
		self.selectField = SelectField(
			self.playerList,
			self.letterBag
		)

		layout = QHBoxLayout()
		layout.addWidget(self.playerField)
		layout.addWidget(self.gameField)
		layout.addWidget(self.selectField)

		self.setLayout(layout)
		self.selectField.connectButtons()


