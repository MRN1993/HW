import random

random_number = random.randint(0,100)
print(random_number)

for Chance in range(5):
    user_number = int(input('Please enter anumber:' ))
    
    if user_number == random_number:
        print('win')
        break

    elif Chance == 4:
        print('Game Over!')
        
    elif user_number < random_number:
        print('Enter higher number')

    elif user_number > random_number:
        print('Enter lower number')

    

    

    
  