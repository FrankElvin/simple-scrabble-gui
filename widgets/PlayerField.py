from PyQt4.QtGui import *
from PyQt4.QtCore import *

from player.PlayerWidget import PlayerWidget

class PlayerField(QWidget):

	def __init__(self, playerList):
		super(PlayerField, self).__init__()

		self.playerList = playerList
		pfLayout = QVBoxLayout()
		# pfLayout.addWidget(QLabel(u"Список игроков"))

		for player in playerList:
			pfLayout.addWidget(PlayerWidget(player))

		pfLayout.addStretch(20)

		self.setLayout(pfLayout)

		print "Player field initialized"
