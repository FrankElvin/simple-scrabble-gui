class Player:
    """
    Инициализирует каждого игрока
    """
    def __init__(self, playerName):
        self.name = playerName
        self.score = 0
	
	def __str__(self):
		return "Name:", self.name, ", Score:", self.score

    def get_name(self):
        return self.name

    def increase_score(self, increase):
		self.score += increase

    def get_score(self):
        return self.score
