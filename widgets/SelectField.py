from PyQt4.QtGui import *
from PyQt4.QtCore import *

from letter.SelectLetter import SelectLetter
from selecter.LetterSelecter import LetterSelecter

class SelectField(QWidget):

	def __init__(self, playerList):
		super(SelectField, self).__init__()

		self.playerList = playerList
		self.startLetterNum = 7
		self.activePlayer = 0

		self.selecterList = []
		for player in self.playerList:
			letterList = []
			for i in range(self.startLetterNum):
				letterList.append(SelectLetter(u"Ф"))
			self.selecterList.append(LetterSelecter(player, letterList))

		self.selectLayout = QVBoxLayout()
		self.selectLayout.addWidget(
			QLabel(u"Ход игрока %s" %self.playerList[0])
		)
		self.selectLayout.addWidget(self.selecterList[0])
		self.selectLayout.addStretch(20)
		self.selectLayout.addWidget(QPushButton(u"Завершить ход"))

		self.setLayout(self.selectLayout)
		print "Select field initialized"
	
	def getNextPlayer(self):
		if self.activePlayer == len(self.playerList) -1:
			self.activePlayer = 0
		else:
			self.activePlayer += 1
