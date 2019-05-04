from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LetterSelecter(QWidget):

	def __init__(self, player, letterList):
		super(LetterSelecter, self).__init__()

		self.playerName = player.get_name()
		self.letterList = letterList
		self.letterLayout = QGridLayout()
		self.letterWidth = 5

		self.setLayout(self.letterLayout)
		self.reloadLetters()
	
	def addLetter(self, letter):
		self.letterList.append(letter)
	
	def removeUsedLetters(self):

		to_remove = []
		for letter in self.letterList:
			if letter.used == 1:
				to_remove.append(letter)

		for remove in to_remove:
			self.letterList.remove(remove)

	def reloadLetters(self):

		# remove all widgets
		for i in reversed(range(self.letterLayout.count())): 
			self.letterLayout.itemAt(i).widget().setParent(None)

		row_number = 0
		column_number = 0

		for letter in self.letterList:
			self.letterLayout.addWidget(letter, row_number, column_number)
			column_number += 1

			if column_number > self.letterWidth:
				row_number += 1
				column_number = 0
		
