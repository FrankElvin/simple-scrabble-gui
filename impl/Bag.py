from random import shuffle

LETTER_VALUES = {
	u"А": 1, u"Б": 3, u"В": 3, u"Г": 2, u"Д": 1,
	u"Е": 4, u"Ё": 2, u"Ж": 4, u"З": 1, u"И": 1,
	u"Й": 1, u"К": 5, u"Л": 1, u"М": 3, u"Н": 1,
	u"О": 1, u"П": 3, u"Р": 10,u"С": 1, u"Т": 1,
	u"У": 1, u"Ф": 1, u"Х": 4, u"Ц": 4, u"Ч": 8,
	u"Ш": 4, u"Щ": 10,u"Ъ": 8, u"Ы": 4, u"Ь": 10,
	u"Э": 8, u"Ю": 4, u"Я": 10, u"": 0
}


class Tile:

    def __init__(self, letter, letter_values):
        # Инициализация
        self.letter = letter.upper()
        if self.letter in letter_values:
            self.score = letter_values[self.letter]
        else:
            self.score = 0

    def get_letter(self):
        #Возвращает знвчение буквы
        return self.letter

    def get_score(self):
        #Возвращает сумму баллов игрока
        return self.score

class Bag:

    def __init__(self):
        self.bag = []
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        for i in range(quantity):
            self.bag.append(tile)

    def initialize_bag(self):

        self.add_to_bag(Tile(u"А", LETTER_VALUES), 9)
        self.add_to_bag(Tile(u"Б", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"В", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Г", LETTER_VALUES), 4)
        self.add_to_bag(Tile(u"Д", LETTER_VALUES), 12)
        self.add_to_bag(Tile(u"Е", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Ё", LETTER_VALUES), 3)
        self.add_to_bag(Tile(u"Ж", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"З", LETTER_VALUES), 9)
        self.add_to_bag(Tile(u"И", LETTER_VALUES), 9)
        self.add_to_bag(Tile(u"Й", LETTER_VALUES), 1)
        self.add_to_bag(Tile(u"К", LETTER_VALUES), 4)
        self.add_to_bag(Tile(u"Л", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"М", LETTER_VALUES), 6)
        self.add_to_bag(Tile(u"Н", LETTER_VALUES), 8)
        self.add_to_bag(Tile(u"О", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"П", LETTER_VALUES), 1)
        self.add_to_bag(Tile(u"Р", LETTER_VALUES), 6)
        self.add_to_bag(Tile(u"С", LETTER_VALUES), 4)
        self.add_to_bag(Tile(u"Т", LETTER_VALUES), 6)
        self.add_to_bag(Tile(u"У", LETTER_VALUES), 4)
        self.add_to_bag(Tile(u"Ф", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Х", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Ц", LETTER_VALUES), 1)
        self.add_to_bag(Tile(u"Ш", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Щ", LETTER_VALUES), 1)
        self.add_to_bag(Tile(u"Ъ", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Ы", LETTER_VALUES), 1)
        self.add_to_bag(Tile(u"Ь", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Э", LETTER_VALUES), 1)
        self.add_to_bag(Tile(u"Ю", LETTER_VALUES), 2)
        self.add_to_bag(Tile(u"Я", LETTER_VALUES), 1)
        shuffle(self.bag)

    def take_from_bag(self):
        return self.bag.pop()

    def get_remaining_tiles(self):
        return len(self.bag)
	
	def take_n_from_bag(self, n):
		out = []
		for i in range(n): out.append( self.take_from_bag() )
		return out
