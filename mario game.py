import random

class Character():
    def __init__(self, name):
        self.name = name
        self.__life = 3
        self.__score = 0

    def kicked(self):
        self.__score += 10

    def punched(self):
        self.__score += 5

    def stabbed(self):
        self.__life -= 1

    def display_life(self):
        return self.__life

    def display_score(self):
        return self.__score

    def __str__(self):
        return f'Name: {self.name}\nLife: {self.__life}\nScore: {self.__score}'

mario = Character('Mario')

print("Welcome to the game!")

while mario.display_life() > 0:
    print("\nChoose an action:")
    print("1. Kick")
    print("2. Punch")
    print("3. Stab")
    choice = input("Enter the number corresponding to your action: ")

    if choice == '1':
        mario.kicked()
    elif choice == '2':
        mario.punched()
    elif choice == '3':
        mario.stabbed()
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
    
    print(f'{mario.name} took action!')

    if random.randint(1, 10) == 1:
        print("A random event occurred! The game ends.")
        break

if mario.display_life() <= 0:
    print(f'\n{mario.name} has run out of life! Game Over.')
