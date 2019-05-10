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

		letterBag = self.parent().parent().letterBag

		to_remove = []
		for letter in self.letterList:
			if letter.used:
				to_remove.append(letter)

			if letter.toChange:
				to_remove.append(letter)
				letterBag.add_to_bag(
					letterBag.tile_class(
						letter.letter,
						letterBag.letter_values
					),
					1
				)
		letterBag.shuffle_self()

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

	def checkUsed(self):
		used = False
		for letter in self.letterList:
			if letter.used == True:
				used = True
				break
		return used

	def checkChanged(self):
		changed = False
		for letter in self.letterList:
			if letter.toChange == True:
				changed = True
				break
		return changed

	def countRemaining(self):
		return len(self.letterList)

