from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PlayerWidget(QWidget):

	def __init__(self, playerName):
		super(PlayerWidget, self).__init__()

		playerLayout = QVBoxLayout()

		self.playerName = playerName
		self.score = 0

		playerLayout.addWidget(QLabel(playerName))
		self.scoreLabel = QLabel(str(self.score))
		playerLayout.addWidget(self.scoreLabel)

		self.setLayout(playerLayout)
	
	def changeScore(newScore):
		self.score = newScore
		self.scoreLabel.setText(str(newScore))
		
