from PyQt4.QtGui import *
from PyQt4.QtCore import *

class BadWordDialog(QMessageBox):
	
	def __init__(self, word):
		super(BadWordDialog, self).__init__()

		self.setIcon(QMessageBox.Warning)
		self.setText(u"Нельзя выбрать слово %s" %word)
		self.setInformativeText(u'Слово "%s"не найдено в базе данных игры.\nНо его можно туда добавить!' %word)
		self.setWindowTitle(u"Ошибка ввода слова")

		self.setStandardButtons(QMessageBox.Ok)
	
