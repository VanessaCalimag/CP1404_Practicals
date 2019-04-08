"""Guitar class"""


class Guitar:
    CURRENT_YEAR = 2019
    OLD_GUITAR = 50

    def __init__(self, name='', year=0, cost=0):
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        return '{self.name} ({self.year}) : ${self.cost:,.2f}'.format(self=self)

    def get_age(self):
        return Guitar.CURRENT_YEAR - self.year

    def is_vintage(self):
        return self.get_age() >= Guitar.OLD_GUITAR



