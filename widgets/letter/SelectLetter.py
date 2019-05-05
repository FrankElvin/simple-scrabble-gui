from LetterButton import LetterButton
from PyQt4 import QtCore, QtGui

class SelectLetter(LetterButton):

	def __init__(self, letter):
		super(SelectLetter, self).__init__(letter)

		self.used = 0

	def mouseMoveEvent(self, e):
		
		# drag with only Right Button
		if e.buttons() != QtCore.Qt.RightButton:
			return

		# no drag if used
		if self.used == 1:
			return

		mimeData = QtCore.QMimeData()
		mimeData.setText(self.text())
		
		drag = QtGui.QDrag(self)
		drag.setMimeData(mimeData)
		
		dropAction = drag.start(QtCore.Qt.MoveAction)

		# if drag was successfull
		if drag.target():
			self.used = 1
			self.setStyleSheet("background-color: cyan")
