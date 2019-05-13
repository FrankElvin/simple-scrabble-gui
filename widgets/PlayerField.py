from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

from .player.PlayerWidget import PlayerWidget

class PlayerField(QWidget):

	def __init__(self, playerList, letterBag):
		super(PlayerField, self).__init__()

		self.playerList = playerList
		self.letterBag = letterBag
		self.playerWidgetList = []
		self.tileCounter = QLabel("")
		self.actualizeBag()
		
		pfLayout = QVBoxLayout()
		for player in playerList:
			pw = PlayerWidget(player)
			self.playerWidgetList.append(pw)
			pfLayout.addWidget(pw)

		pfLayout.addStretch(20)
		pfLayout.addWidget(QLabel(u"Фишек осталось:"))
		pfLayout.addWidget(self.tileCounter)
		self.setLayout(pfLayout)

		print("Player field initialized")
	
	def actualizeBag(self):
		self.tileCounter.setText(
			str(self.letterBag.get_remaining_tiles())
		)

	def actualizePoints(self, playerIndex):
		self.playerWidgetList[playerIndex].actualizePoints()
