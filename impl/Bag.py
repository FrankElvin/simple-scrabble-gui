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

    def __init__(self, LETTER_VALUES, tile_class):
        self.bag = []
        self.letter_values = LETTER_VALUES
        self.tile_class = tile_class
        self.initialize_bag()

    def add_to_bag(self, tile, quantity):
        for i in range(quantity):
            self.bag.append(tile)

    def shuffle_self(self):
        shuffle(self.bag)

    def initialize_bag(self):

        self.add_to_bag(self.tile_class(u"А", self.letter_values), 9)
        self.add_to_bag(self.tile_class(u"Б", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"В", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Г", self.letter_values), 4)
        self.add_to_bag(self.tile_class(u"Д", self.letter_values), 12)
        self.add_to_bag(self.tile_class(u"Е", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Ё", self.letter_values), 3)
        self.add_to_bag(self.tile_class(u"Ж", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"З", self.letter_values), 9)
        self.add_to_bag(self.tile_class(u"И", self.letter_values), 9)
        self.add_to_bag(self.tile_class(u"Й", self.letter_values), 1)
        self.add_to_bag(self.tile_class(u"К", self.letter_values), 4)
        self.add_to_bag(self.tile_class(u"Л", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"М", self.letter_values), 6)
        self.add_to_bag(self.tile_class(u"Н", self.letter_values), 8)
        self.add_to_bag(self.tile_class(u"О", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"П", self.letter_values), 1)
        self.add_to_bag(self.tile_class(u"Р", self.letter_values), 6)
        self.add_to_bag(self.tile_class(u"С", self.letter_values), 4)
        self.add_to_bag(self.tile_class(u"Т", self.letter_values), 6)
        self.add_to_bag(self.tile_class(u"У", self.letter_values), 4)
        self.add_to_bag(self.tile_class(u"Ф", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Х", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Ц", self.letter_values), 1)
        self.add_to_bag(self.tile_class(u"Ш", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Щ", self.letter_values), 1)
        self.add_to_bag(self.tile_class(u"Ъ", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Ы", self.letter_values), 1)
        self.add_to_bag(self.tile_class(u"Ь", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Э", self.letter_values), 1)
        self.add_to_bag(self.tile_class(u"Ю", self.letter_values), 2)
        self.add_to_bag(self.tile_class(u"Я", self.letter_values), 1)
        self.shuffle_self()

    def take_from_bag(self):
        return self.bag.pop()

    def get_remaining_tiles(self):
        return len(self.bag)

    def take_n_from_bag(self, n):
        out = []
        for i in range(n): out.append( self.take_from_bag() )
        return out
