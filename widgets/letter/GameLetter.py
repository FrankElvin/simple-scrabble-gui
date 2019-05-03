from LetterButton import LetterButton

class GameLetter(LetterButton):

	def __init__(self, letter):
		super(GameLetter, self).__init__(letter)

		self.setAcceptDrops(True)
		self.filled = 0
		self.setStyleSheet("background-color: gray")
	
	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'): e.accept()
		else: e.ignore() 
	
	def dropEvent(self, e):
		if self.filled == 0:
			self.setText(e.mimeData().text())
			self.setAcceptDrops(False)
			self.filled = 1
