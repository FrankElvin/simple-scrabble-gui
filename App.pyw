import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from random import randint

from widgets.GameField import GameField
from widgets.PlayerField import PlayerField
from widgets.SelectField import SelectField
from widgets.StartDialogs import PlayerNumberDialog, PlayerNameDialog

def showStartDialog():
	numberDialog = PlayerNumberDialog()
	numberDialog.exec_()

	print "player number:", numberDialog.playerCounter.value() 

	nameDialog = PlayerNameDialog(numberDialog.playerCounter.value())
	nameDialog.exec_()

	players = []
	for player in nameDialog.players:
		players.append(player.input.text())
	return players



if __name__ == '__main__':

	app = QApplication(sys.argv)
	
	# get the initial data from dialogs
	playerList = showStartDialog()

	# Build the window widget
	mainWindow = QWidget()
	mainWindow.setWindowTitle(u"Скромный интерфейс Scrubble на русском")
	
	# loading all subwindows
	playerField = PlayerField(playerList)
	gameField = GameField()
	selectField = SelectField(playerList)

	# adding subwindows to the layout
	layout = QHBoxLayout()
	layout.addWidget(playerField)
	layout.addWidget(gameField)
	layout.addWidget(selectField)
	mainWindow.setLayout(layout)

	# Show window and run
	mainWindow.show()
	app.exec_()
