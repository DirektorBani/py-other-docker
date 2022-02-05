month = int(input('Input month number: '))
day = int(input('Input date: '))

if (month == 1 and day >= 21) or (month == 2 and day <=19):
  print('Vodoley')
elif (month == 2 and day >= 20) or (month == 3 and day <=20):
  print('Kozerog')
elif (month == 3 and day >= 21) or (month == 4 and day <=20):
  print('Oven')
elif (month == 4 and day >= 21) or (month == 5 and day <=21):
  print('Telec')
elif (month == 5 and day >= 22) or (month == 6 and day <=21):
  print('Bliznec')
elif (month == 6 and day >= 22) or (month == 7 and day <=22):
  print('Rak')
elif (month == 7 and day >= 23) or (month == 8 and day <=21):
  print('Lev')
elif (month == 8 and day >= 22) or (month == 9 and day <=23):
  print('Deva')
elif (month == 9 and day >= 24) or (month == 10 and day <=23):
  print('Vesy')
elif (month == 10 and day >= 24) or (month == 11 and day <=22):
  print('Scorpion')
elif (month == 11 and day >= 23) or (month == 12 and day <=22):
  print('Strelec')
elif (month == 12 and day >= 23) or (month == 1 and day <=20):
  print('Kozerog')
else:
  print('ERROR: Please enter a valid month or date number')