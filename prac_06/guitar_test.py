
from prac_06.guitar import Guitar

name = "Gibson L-5 CES"
year = 1922
cost = 16035.40

first_guitar = Guitar(name, year, cost)
another_guitar = Guitar('Another Guitar', 2012, 50.50)
print(first_guitar)
print(another_guitar)
print('{} get.age() - Expected {}. Got {}'.format(first_guitar.name, 70, first_guitar.get_age()))
print('{} get.age() - Expected {}. Got {}'.format(another_guitar.name, 10, another_guitar.get_age()))
print('{} is.vintage() - Expected {}. Got {}'.format(first_guitar.name, True, first_guitar.is_vintage()))
print('{} is.vintage() - Expected {}. Got {}'.format(another_guitar.name, True, another_guitar.is_vintage()))