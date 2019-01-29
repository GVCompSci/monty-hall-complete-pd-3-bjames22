'''Brennan James 
Monty hall project part 3'''
import random 

rounds = int(input('Rounds to play: '))
while rounds < 10 or rounds > 10000: 
  rounds = int (int(input('Rounds must be in between 10 and 10,000: ')))
choice = input('Do you want to switch? ')
wins = 0
losses = 0
percent = 0
for i in range(1 , rounds + 1):
  car = random.randint(1,3)
  guess = random.randint(1,3)
  if choice.lower() == 'no':
    if guess == car:
      wins += 1
    else:
      losses += 1
  elif choice.lower() == 'yes':
    if guess == 1 and car == 1:
      losses += 1 
    elif guess == 1 and car == 2:
      wins += 1 
    elif guess == 1 and car == 3: 
      wins += 1 
    elif guess == 2 and car == 1:
      wins += 1
    elif guess == 2 and car == 2:
      losses += 1
    elif guess == 2 and car == 3:
      wins += 1
    elif guess == 3 and car == 1:
      wins += 1
    elif guess == 3 and car == 2:
      wins += 1
    else:
      losses += 1
  else:
    print('error')
percent = wins/rounds
percent *= 100
print('Wins: ', wins,'\tLosses: ', losses,'\tTotal Plays: ',rounds,'\t(',format(percent,'.2f'),'% wins)', sep = '')