from random import sample
from os import system

turns = 10
list_of_elements = []
number_guessing = []
message = ''

for i in range(100):
    list_of_elements.append(i+1)

choose_of_computer = sample(list_of_elements, 1)

while True:
    clean_screen()
    print('Number Guessing')
    print('You have to choose a number between 1 and 100')
    print(f'You have {turns} turns')
    print(message)
    print(f'Your guess: {number_guessing}' )
    print('Enter a Guess:', end=' ')

    your_choose = int(input())
   
    turns -= 1

    if turns == 0:
        clean_screen()
        print('Game Over')
        print(f'The number was {choose_of_computer}')
        break

    if your_choose in choose_of_computer:
        clean_screen()
        print(f'Congratulations! You got it right!')
        print(f'The choosen number was {choose_of_computer}')
        print(f'Your turns {number_guessing}')
        break
    
    for i in choose_of_computer:
                
        if your_choose > i:
            tuple_result = (your_choose, '↑')
            message = 'high value'
            
        if your_choose < i:
            tuple_result = (your_choose, '↓')
            message = 'low value'
        
    number_guessing.append(tuple_result)