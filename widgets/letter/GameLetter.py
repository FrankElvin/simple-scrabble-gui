
from LetterButton import LetterButton

class GameLetter(LetterButton):

	def __init__(self, letter):
		super(GameLetter, self).__init__(letter)

		self.setAcceptDrops(True)
