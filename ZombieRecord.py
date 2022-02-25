

import random

first_names=('Riely','Gutsy','Scabby','Meaty','Paley','Mort')
last_names=('McBrains','Gutsman','Meatface','Fleshington','Canker','Cadavers')
type=('Crawly Crawlers','Zom Walkers','Carcaus Scavengers','Running Necros','Stiff Spewys')
powers=('Acid Mucus','Thicc Boi','Stronk Stam','Brainy Senses','Range Mage')
locations=('Fairgrounds','Starbucks','Cocas Pizza','McCune Park','Baird Brothers','Canfield Highschool','MCCTC')
ages=('New Deadling','Toddler Deadling','Child Deadling','Teen Deadling','Adult Deadling')

zombies = []
for i in range(10):
    zombies.append(random.choice(first_names))
    zombies.append(random.choice(last_names))
    zombies.append(random.choice(type))
    zombies.append(random.choice(powers))
    zombies.append(random.choice(locations))
    zombies.append(random.choice(ages))

print (' '.join(zombies))