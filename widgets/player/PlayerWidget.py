from PyQt4.QtGui import *
from PyQt4.QtCore import *

class PlayerWidget(QWidget):

	def __init__(self, player):
		super(PlayerWidget, self).__init__()

		playerLayout = QVBoxLayout()

		self.player = player

		playerLayout.addWidget(QLabel(self.player.get_name()))
		self.scoreLabel = QLabel(str(self.player.get_score()))
		playerLayout.addWidget(self.scoreLabel)

		self.setLayout(playerLayout)
	
	def actualizePoints(self):
		self.scoreLabel.setText(str(
			self.player.get_score()
		))
