
from prac_06.guitar import Guitar

guitars = []
print('My guitars!')
name = input('Name: ')
while name != '':
    year = int(input('Year: '))
    cost = float(input('Cost: '))
    new_guitar_list = Guitar(name, year, cost)
    guitars.append(new_guitar_list)
    print('{self.name} ({self.year}) : ${self.cost:,.2f}'.format(self=new_guitar_list))
    name = input('Name: ')

print('These are my guitars:')
for i, guitar in enumerate(guitars):
    vintage_string = ''
    if guitar.is_vintage():
        vintage_string = '(vintage)'
        print("Guitar {}: {:>5} ({}), worth ${:,.2f}{}".format(i + 1, guitar.name, guitar.year, guitar.cost,
                                                                                                vintage_string))


