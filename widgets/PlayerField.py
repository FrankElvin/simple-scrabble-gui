from PyQt4.QtGui import *
from PyQt4.QtCore import *

from player.PlayerWidget import PlayerWidget

class PlayerField(QWidget):

	def __init__(self, playerList):
		super(PlayerField, self).__init__()

		self.playerList = playerList
		self.playerWidgetList = []
		pfLayout = QVBoxLayout()
		# pfLayout.addWidget(QLabel(u"Список игроков"))

		for player in playerList:
			pw = PlayerWidget(player)
			self.playerWidgetList.append(pw)
			pfLayout.addWidget(pw)

		pfLayout.addStretch(20)

		self.setLayout(pfLayout)

		print "Player field initialized"

	def actualizePoints(self, playerIndex):
		self.playerWidgetList[playerIndex].actualizePoints()
