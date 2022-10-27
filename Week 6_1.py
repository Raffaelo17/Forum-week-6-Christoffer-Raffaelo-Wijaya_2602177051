# Exercise 1

inventory = {
    'gold': 500,
    'pouch': ['flint', 'twine', 'gemstone'],
    'backpack': ['xylophone', 'dagger', 'bedroll', 'bread loaf']
}


inventory.setdefault('pocket')
inventory['pocket'] = ['seashell', 'strange berry', 'lint']
inventory['pocket'].sort()
inventory['backpack'].remove('dagger')
inventory['gold'] += 50

print(inventory)
