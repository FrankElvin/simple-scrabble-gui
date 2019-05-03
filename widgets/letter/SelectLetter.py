from LetterButton import LetterButton
from PyQt4 import QtCore, QtGui

class SelectLetter(LetterButton):

	def __init__(self, letter):
		super(SelectLetter, self).__init__(letter)

		self.used = 0

	def mouseMoveEvent(self, e):
		
		if e.buttons() != QtCore.Qt.RightButton:
			return

		if self.used == 1:
			return

		mimeData = QtCore.QMimeData()
		mimeData.setText(self.text())
		
		drag = QtGui.QDrag(self)
		drag.setMimeData(mimeData)
		
		dropAction = drag.start(QtCore.Qt.MoveAction)
		self.used = 1
		self.setStyleSheet("background-color: cyan")

