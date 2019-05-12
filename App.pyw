import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *

from widgets.MainWindow import MainWindow
from widgets.StartDialogs import PlayerNumberDialog, PlayerNameDialog

from impl.Bag import Bag, LETTER_VALUES, Tile
from impl.Player import Player

from db.db_connection import DbChecker

def showStartDialog():
	numberDialog = PlayerNumberDialog()
	numberDialog.exec_()
	if not numberDialog.result():
		return []

	nameDialog = PlayerNameDialog(numberDialog.playerCounter.value())
	nameDialog.exec_()
	if not nameDialog.result():
		return []

	players = []
	for player in nameDialog.players:
		#players.append(player.input.text())
		players.append(
			Player(player.input.text())
		)
	return players


if __name__ == '__main__':

	dbChecker = DbChecker('db\word_database.db')
	app = QApplication(sys.argv)
	
	# get the initial data from dialogs
	playerList = showStartDialog()
	if playerList:

		# initialize the bag
		letterBag = Bag(LETTER_VALUES, Tile)

		# Build the window widget
		mainWindow = MainWindow(playerList, letterBag, dbChecker)

		# Show window and run
		mainWindow.show()
		app.exec_()
