from PyQt4.QtGui import *
from PyQt4.QtCore import *

class FinishDialog(QMessageBox):
	
	def __init__(self, playerList):
		super(FinishDialog, self).__init__()

		self.playerList = playerList
		winner = self.getWinner()

		self.setIcon(QMessageBox.Information)
		self.setText(u"Победил игрок %s" %winner)
		self.setInformativeText(self.getStats())
		self.setWindowTitle(u"Игра окончена!")

		self.setStandardButtons(QMessageBox.Ok)
	
	def getWinner(self):
		winner = self.playerList[0]
		for player in self.playerList:
			if player.score > winner.score:
				winner = player
		return winner.get_name()
	
	def getStats(self):
		outLines = u"Итоговый счёт:"
		for player in self.playerList:
			outLines += "\n%s: %d" %(player.get_name(), player.get_score())
		return outLines
		
