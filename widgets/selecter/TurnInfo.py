from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class TurnInfo(QWidget):

	def __init__(self, parent=None):
		super(TurnInfo, self).__init__(parent)

		layout = QGridLayout()
		self.plusScore = 0
		self.scoreLabel = QLabel("0")
		layout.addWidget(QLabel(u"За ход получено:"), 0, 0)
		layout.addWidget(self.scoreLabel, 0, 1)
		self.setLayout(layout)
	
	def addPoints(self, increase):
		self.plusScore += increase
		self.scoreLabel.setText(str(self.plusScore))
	
	def endTurn(self):
		self.plusScore = 0
		self.scoreLabel.setText(str(self.plusScore))

