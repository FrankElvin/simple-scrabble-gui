from PyQt4.QtGui import *
from PyQt4.QtCore import *

class LetterButton(QPushButton):

	def __init__(self, letter):
		super(LetterButton, self).__init__(letter)

		self.LETTER_VALUES = {
			u"А": 1, u"Б": 3, u"В": 3, u"Г": 2, u"Д": 1, u"Е": 4,
			u"Ё": 2, u"Ж": 4, u"З": 1, u"И": 1, u"Й": 1, u"К": 5,
			u"Л": 1, u"М": 3, u"Н": 1, u"О": 1, u"П": 3, u"Р": 10,
			u"С": 1, u"Т": 1, u"У": 1, u"Ф": 1, u"Х": 4, u"Ц": 4,
			u"Ч": 8, u"Ш": 4, u"Щ": 10, u"Ъ": 8, u"Ы": 4, u"Ь": 10,
			u"Э": 8, u"Ю": 4, u"Я": 10, u"": 0
		}
		self.points = self.LETTER_VALUES[letter]
		#print "Letter:", letter, "Points:", self.points
		self.setColorByValue()
		#self.setEnabled(False)

	def setColorByValue(self):
		color = ""
		if self.points < 4:
			color = "white"
		elif self.points <=8:
			color = "yellow"
		else: color = "red"
		self.setStyleSheet("background-color: %s" %color)

	def sizeHint(self):
		return QSize(30, 30)
	
	def setText(self, letter):
		"""Override the standard setText button method"""
		super(LetterButton, self).setText(letter)
		self.points = self.LETTER_VALUES[unicode(letter)]
		self.setColorByValue()

