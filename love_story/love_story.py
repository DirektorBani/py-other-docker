boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    print('Perfect couples: ')
    for a, b in zip(sorted(boys), sorted(girls)):
        print(a, b)
else:
    print('Sorry! But Quantity is not equal')