from PyQt4.QtGui import *
from PyQt4.QtCore import *

from letter.SelectLetter import SelectLetter
from selecter.LetterSelecter import LetterSelecter
from selecter.TurnInfo import TurnInfo

class SelectField(QWidget):

	def __init__(self, playerList, letterBag, playerField):
		super(SelectField, self).__init__()

		self.playerList = playerList
		self.startLetterNum = 7
		self.activePlayer = 0
		self.letterBag = letterBag
		self.playerField = playerField
		self.frameList = []
		self.turnInfoList = []

		layout = QVBoxLayout()

		# initialize 1 frame per 1 player
		for player in self.playerList:

			frame = QFrame()
			ly = QVBoxLayout()

			letterList = []
			turnInfo = TurnInfo()

			for i in range(self.startLetterNum):
				letterList.append(
					SelectLetter(self.letterBag.take_from_bag().get_letter(), turnInfo)
				)

			btn = QPushButton(u"Завершить ход")
			btn.clicked.connect(self.nextTurn)

			ly.addWidget( QLabel(u"Ход игрока %s" %player.get_name()))
			ly.addWidget(LetterSelecter(player, letterList))
			ly.addStretch(20)
			ly.addWidget(turnInfo)
			ly.addWidget(btn)

			frame.setLayout(ly)
			self.frameList.append(frame)
			self.turnInfoList.append(turnInfo)

		for frame in self.frameList:
			layout.addWidget(frame)

		# hide all frames but first
		for frame in self.frameList[1:]:
			frame.hide()

		self.setLayout(layout)
		print "Select field initialized"
	
	def getNextPlayer(self):
		if self.activePlayer == len(self.playerList) -1:
			self.activePlayer = 0
		else:
			self.activePlayer += 1
	
	def nextTurn(self):
		""" Switches the frame with player menu """
		self.frameList[self.activePlayer].hide()

		self.playerList[self.activePlayer].increase_score(
			self.turnInfoList[self.activePlayer].plusScore
		)
		self.playerField.actualizePoints(self.activePlayer)

		self.turnInfoList[self.activePlayer].endTurn()

		self.getNextPlayer()
		self.frameList[self.activePlayer].show()


