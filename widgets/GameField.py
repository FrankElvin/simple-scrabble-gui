from PyQt4.QtGui import *
from PyQt4.QtCore import *

from letter.GameLetter import GameLetter

class GameField(QWidget):

	def __init__(self):
		super(GameField, self).__init__()

		gameLayout = QGridLayout()

		for i in range(14):
			for j in range(14):
				gameLayout.addWidget(GameLetter(""), i, j)

		self.setLayout(gameLayout)

		print "Game field initialized"

