from PyQt4.QtGui import *
from PyQt4.QtCore import *

from letter.SelectLetter import SelectLetter
from selecter.LetterSelecter import LetterSelecter
from selecter.TurnInfo import TurnInfo
from selecter.PlayerFrame import PlayerFrame

class SelectField(QWidget):

	def __init__(self, playerList, letterBag):
		super(SelectField, self).__init__()

		self.playerList = playerList
		self.startLetterNum = 7
		self.activePlayer = 0
		self.letterBag = letterBag
		self.frameList = []
		layout = QVBoxLayout()

		# initialize 1 frame per 1 player
		for player in self.playerList:

			letterList = []
			for i in range(self.startLetterNum):
				letterList.append(
					SelectLetter(self.letterBag.take_from_bag().get_letter())
				)
			letterSelecter = LetterSelecter(player, letterList)

			frame = PlayerFrame(player, letterSelecter)
			self.frameList.append(frame)

		for frame in self.frameList:
			layout.addWidget(frame)

		# hide all frames but first
		for frame in self.frameList[1:]:
			frame.hide()

		self.setLayout(layout)
		print "Select field initialized"
	
	def connectButtons(self):
		for frame in self.frameList:
			frame.turnEnd.clicked.connect(self.nextTurn)
			frame.turnRevert.clicked.connect(frame.revertTurn)
	
	def getNextPlayer(self):
		if self.activePlayer == len(self.playerList) -1:
			self.activePlayer = 0
		else:
			self.activePlayer += 1
	
	def addPointsToCurrent(self, points):
		self.frameList[self.activePlayer].turnInfo.addPoints(points)
	
	def nextTurn(self):
		""" Main logic of the turn ending """
		self.frameList[self.activePlayer].hide()
		# add current points to the real Player instance
		self.playerList[self.activePlayer].increase_score(
			self.frameList[self.activePlayer].turnInfo.plusScore
		)
		# actualize points on the Player screen basing on Player instance
		self.parent().playerField.actualizePoints(self.activePlayer)
		# set turn info conditions to zeros
		self.frameList[self.activePlayer].turnInfo.endTurn()

		# clear old letters from the letter list
		self.frameList[self.activePlayer].letterSelecter.removeUsedLetters()

		# add new letters to players hand
		for i in range(self.frameList[self.activePlayer].turnInfo.letterCounter.value()):
			self.frameList[self.activePlayer].letterSelecter.addLetter(
				SelectLetter(self.letterBag.take_from_bag().get_letter() )
			)
		self.frameList[self.activePlayer].letterSelecter.reloadLetters()

		# actualize tile counter
		self.parent().playerField.actualizeBag()

		# Prepare game field to the next turn
		self.parent().gameField.confirmActions()

		# change frame with player
		self.getNextPlayer()
		self.frameList[self.activePlayer].show()
	
