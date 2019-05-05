from LetterButton import LetterButton

class GameLetter(LetterButton):

	def __init__(self, letter, x, y, multiplier):
		super(GameLetter, self).__init__(letter)

		#self.setAcceptDrops(True)
		self.setAcceptDrops(False)
		self.filled = False
		self.filledNow = False
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
	
	def __str__(self):
		return "Letter %s, points: %d, multiplier: %s" %(unicode(self.text()), self.points, str(self.multiplier))
			
	
	def dragEnterEvent(self, e):
		if e.mimeData().hasFormat('text/plain'): e.accept()
		else: e.ignore() 
	
	def dropEvent(self, e):
		if not self.filled:
			self.setText(e.mimeData().text())
			self.setAcceptDrops(False)
			self.openNearby()
			self.filled = True
			self.filledNow = True

			self.getNearbyWords()
	
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
	
	def getWord(self, row, start):
		left_done = False
		right_done = False
		i = 1
		word = [row[start]]
		while not(left_done) or not(right_done):
			if start-i < 0:
				left_done = True
			else: 
				left_letter = row[start-i]
				if left_letter.filledNow:
					word.append(left_letter) 
				else:
					left_done = True

			if start+i >= len(row):
				right_done = True
			else:
				right_letter = row[start+i]
				if right_letter.filledNow: 
					word.append(right_letter)
				else:
					right_done = True

			i += 1
		return word
	
	def getWordMultiplier(self, words):
		mult = 1
		for word in words:
			if len(word) != 1:
				for letter in word:
					if letter.multiplier['type'] == 'word':
						mult *= letter.multiplier['number']
		return mult
	
	def getWordPoints(self, word):
		points = 0
		word_mult = self.getWordMultiplier([word])

		for letter in word:
			print unicode(letter)
			if letter.multiplier['type'] == 'letter':
				points += letter.points * letter.multiplier['number']
			else:
				points += letter.points
		print "Raw points for row word: %d " %points
		print "word multiplier for row word: %d" %word_mult
		print "Result for row word: %d" %(points * word_mult)
		return points * word_mult


	def getNearbyWords(self):

		row = self.parent().letterMatrix[self.x]
		row_word = self.getWord(row, self.y)

		column = self.parent().getMatrixColumn(self.y)
		column_word = self.getWord(column, self.x)

		word_mult = self.getWordMultiplier([row_word, column_word])

		print '===== result for word with new letter ===='
		full_points = self.getWordPoints(row_word)
		print '===== result for word without adding letter ===='
		points_before = self.getWordPoints(row_word[1:])
		print "delta is: %d" %(full_points - points_before)
		print '*'*40

