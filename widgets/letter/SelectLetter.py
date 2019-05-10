from LetterButton import LetterButton
from PyQt4 import QtCore, QtGui

class SelectLetter(LetterButton):

	def __init__(self, letter):
		super(SelectLetter, self).__init__(letter)

		self.used = False
		self.toChange = False
		self.clicked.connect(self.addToChange)

	def __str__(self):
		return "Letter %s; used: %s; toChange: %s" %(
			unicode(self.text()),
			self.used,
			self.toChange
		)

	def addToChange(self):
		if not self.parent().checkUsed():
			self.toChange = True
			self.setStyleSheet("background-color: magenta")
			self.parent().parent().prepareToChange()

	def mouseMoveEvent(self, e):
		
		# drag with only Right Button
		if e.buttons() != QtCore.Qt.RightButton:
			return

		# no drag if used
		if self.used or self.parent().checkChanged():
			return

		mimeData = QtCore.QMimeData()
		mimeData.setText(self.text())
		
		drag = QtGui.QDrag(self)
		drag.setMimeData(mimeData)
		
		dropAction = drag.start(QtCore.Qt.MoveAction)

		# if drag was successfull
		if drag.target():
			self.used = True
			self.setStyleSheet("background-color: cyan")
	
	def reload(self):
		self.used = False
		self.toChange = False
		self.setColorByValue()	
