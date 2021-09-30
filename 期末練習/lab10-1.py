class Movie:
    def __init__(self, name, year, director, box):
        self.name = str(name)
        self.year = int(year)
        self.director = str(director)
        self.box = list(box)


    def box_office(self):
        return '$' + str(sum(self.box)) + ' millions'


    def is_earlier_than(self, other):
        return self.year < other.year


frozen = Movie('Frozen', 2013, 'Jennifer', [1000, 200])
lionKing = Movie('Lion King', 1994, 'Robert Ralph', [4000, 500])
print(frozen.box_office()) # $1200 millions
print(frozen.is_earlier_than(lionKing)) # False
