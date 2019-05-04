from LetterButton import LetterButton

class GameLetter(LetterButton):

	def __init__(self, letter, x, y, multiplier):
		super(GameLetter, self).__init__(letter)

		#self.setAcceptDrops(True)
		self.setAcceptDrops(False)
		self.filled = 0
		self.x = x
		self.y = y
		self.multiplier = multiplier

		if multiplier['type'] == 'letter':
			if multiplier['number'] == 2:
				self.setStyleSheet("background-color: cyan")
			elif multiplier['number'] == 3:
				self.setStyleSheet("background-color: blue")
		elif multiplier['type'] == 'word':
			if multiplier['number'] == 2:
				self.setStyleSheet("background-color: pink")
			elif multiplier['number'] == 3:
				self.setStyleSheet("background-color: red")
		else:
			self.setStyleSheet("background-color: green")
			
	
	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'): e.accept()
		else: e.ignore() 
	
	def dropEvent(self, e):
		if self.filled == 0:
			self.setText(e.mimeData().text())
			self.setAcceptDrops(False)
			self.openNearby()
			self.filled = 1
	
	def getNearbyLetters(self):
		xs = self.x-1, self.x  , self.x  , self.x+1
		ys = self.y  , self.y-1, self.y+1, self.y

		out_list = []
		for coord in zip(xs, ys):
			if (
				(coord[0]>=0 and coord[1]>=0) and 
				(coord[0]<len(self.parent().letterMatrix) and coord[1]<len(self.parent().letterMatrix))
			):
				out_list.append(self.parent().letterMatrix[coord[0]][coord[1]])
		return out_list
	
	def openNearby(self):
		list = self.getNearbyLetters()
		for letter in list: letter.setAcceptDrops(True)
			
