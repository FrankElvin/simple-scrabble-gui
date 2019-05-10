from PyQt4.QtGui import *
from PyQt4.QtCore import *

from TurnInfo import TurnInfo

class PlayerFrame(QFrame):

	def __init__(self, player, letterSelecter):
		super(PlayerFrame, self).__init__()

		self.player = player
		self.letterSelecter = letterSelecter

		self.turnRevert = QPushButton(u"Отменить ход")
		self.turnEnd = QPushButton(u"Завершить ход")
		self.turnInfo = TurnInfo()

		layout = QVBoxLayout()
		layout.addWidget(QLabel(u"Ход игрока %s" %player.get_name()))
		layout.addWidget(self.letterSelecter)
		layout.addStretch(20)
		layout.addWidget(self.turnInfo)
		layout.addWidget(self.turnRevert)
		layout.addWidget(self.turnEnd)

		self.setLayout(layout)
	
	def revertTurn(self):
		# set plust points to zero
		self.turnInfo.endTurn()

		# remove new letters from the game field
		self.parent().parent().gameField.revertActions()
		self.turnEnd.setText(u"Завершить ход")

		# reload used letters at player frame
		for letter in self.letterSelecter.letterList:
			letter.reload()

	def checkEmptyHand(self):
		if self.letterSelecter.countRemaining() == 0:
			return True
		else:
			return False

	def applyPassOnPlayer(self):
		if not(self.letterSelecter.checkUsed()):
			self.player.passed += 1

	def prepareToChange(self):
		changeNum = 0
		for letter in self.letterSelecter.letterList:
			if letter.toChange: changeNum += 1
		self.turnEnd.setText(u"Завершить ход (поменять %d букв)" %changeNum)

