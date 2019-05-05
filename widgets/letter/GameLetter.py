from LetterButton import LetterButton

class GameLetter(LetterButton):

	def __init__(self, letter, x, y, multiplier):
		super(GameLetter, self).__init__(letter)

		self.setAcceptDrops(False)
		self.filled = False
		self.filledNow = False
		self.x = x
		self.y = y
		self.multiplier = multiplier
		self.openedBySelf = []

		self.applyColor()

	def __str__(self):
		return "Letter %s, points: %d, multiplier: %s" %(unicode(self.text()), self.points, str(self.multiplier))

	def applyColor(self):
		if self.multiplier['type'] == 'letter':
			if self.multiplier['number'] == 2:
				self.setStyleSheet("background-color: cyan")
			elif self.multiplier['number'] == 3:
				self.setStyleSheet("background-color: blue")
		elif self.multiplier['type'] == 'word':
			if self.multiplier['number'] == 2:
				self.setStyleSheet("background-color: pink")
			elif self.multiplier['number'] == 3:
				self.setStyleSheet("background-color: red")
		else:
			self.setStyleSheet("background-color: green")
		
	def erase(self):
		self.filled = False
		self.filledNow = False
		self.setText("")
		self.applyColor()

		if (self.x == 7 and self.y == 7):
			self.setAcceptDrops(True)

		for letter in self.openedBySelf:
			if not(letter.x == 7 and letter.y == 7):
				letter.setAcceptDrops(False)

		self.openedBySelf = []
			
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

			plusPoints = self.getPointsFromLetter()
			self.parent().parent().selectField.addPointsToCurrent(plusPoints)
	
	def getNearbyLetters(self):
		xs = self.x-1, self.x  , self.x  , self.x+1
		ys = self.y  , self.y-1, self.y+1, self.y

		out_list = []
		for coord in zip(xs, ys):
			if (
				(coord[0]>=0 and coord[1]>=0) and 
				(coord[0]<len(self.parent().letterMatrix) and coord[1]<len(self.parent().letterMatrix))
			):
				letter_to_open = self.parent().letterMatrix[coord[0]][coord[1]]
				if not letter_to_open.filled:
					out_list.append(letter_to_open)
		return out_list
	
	def openNearby(self):
		self.openedBySelf = self.getNearbyLetters()
		for letter in self.openedBySelf: letter.setAcceptDrops(True)
	
	def getWord(self, row, start):
		""" Returns list, containing a "word": letter chain nearby to the current letter. This list always starts with a current letter. """
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
					if letter.multiplier['type'] == 'word': mult *= letter.multiplier['number']
		return mult
	
	def getPointsFromLetter(self):
		"""Calculates point summary for adding letter to the game field."""

		# getting words including new letter
		words = self.getNearbyWords()

		# wariable for point change
		point_delta = 0

		# if we place letter on word multiplier space, we should add points form other letters in the word
		if self.multiplier['type'] == 'word':
			for word in words:
				point_delta += self.getWordDelta(word)

		# self points are: letter points x word multiplier(s) x space multiplier (letter or word)
		if self.multiplier['type'] == 'word':
			# self multiplier is included in word multiplier
			point_delta += self.points * self.getWordMultiplier(words)
		else:
			point_delta += self.points * self.multiplier['number'] * self.getWordMultiplier(words)

		return point_delta
			
	def getNearbyWords(self):
		"""Returns the list of words that include given letter."""
		row = self.parent().letterMatrix[self.x]
		row_word = self.getWord(row, self.y)

		column = self.parent().getMatrixColumn(self.y)
		column_word = self.getWord(column, self.x)

		return row_word, column_word
	
	def getWordDelta(self, word):
		"""Calculates points added to word by placing letter on a word multiplier position"""
		word_delta = 0
		if len(word) > 1:
			# result for word with new letter ===='
			full_points = self.getWordPoints(word)
			# result for word without adding letter ===='
			points_before = self.getWordPoints(word[1:])
			word_delta = full_points - points_before - self.points*self.multiplier['number']
		return word_delta

	def getWordPoints(self, word):
		"""Calculates the point sum for one word."""
		points = 0
		word_mult = self.getWordMultiplier([word])

		for letter in word:
			if letter.multiplier['type'] == 'letter':
				points += letter.points * letter.multiplier['number']
			else:
				points += letter.points
		return points * word_mult
