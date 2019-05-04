from PyQt4.QtGui import *
from PyQt4.QtCore import *

from letter.SelectLetter import SelectLetter
from selecter.LetterSelecter import LetterSelecter

class SelectField(QWidget):

	def __init__(self, playerList, letterBag):
		super(SelectField, self).__init__()

		self.playerList = playerList
		self.startLetterNum = 7
		self.activePlayer = 0
		self.letterBag = letterBag

		print "Initial bag size:", len(self.letterBag.bag)


		btn = QPushButton(u"Завершить ход")
		btn.clicked.connect(self.nextTurn)


		self.selecterList = []
		for player in self.playerList:
			letterList = []
			for i in range(self.startLetterNum):
				letterList.append(
					SelectLetter(self.letterBag.take_from_bag().get_letter())
				)
			self.selecterList.append(LetterSelecter(player, letterList))

		self.selectLayout = QVBoxLayout()
		self.selectLayout.addWidget(
			QLabel(u"Ход игрока %s" %self.playerList[0])
		)
		self.selectLayout.addWidget(self.selecterList[0])
		self.selectLayout.addStretch(20)
		#self.selectLayout.addWidget(QPushButton(u"Завершить ход"))
		self.selectLayout.addWidget(btn)

		self.setLayout(self.selectLayout)
		print "Select field initialized"
	
	def getNextPlayer(self):
		if self.activePlayer == len(self.playerList) -1:
			self.activePlayer = 0
		else:
			self.activePlayer += 1
	
	def nextTurn(self):
		print "Bag size:", len(self.letterBag.bag)
