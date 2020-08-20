"""Guessing a number from 1 to 100"""
import random


def testing():
    for index, item in enumerate('abc'):
        print(f'{index}:{item}')
        print(f'{random.randint(1,100)}')


def guessing_game():
    """guessing a number from 1 to 100"""
    random_number = random.randint(1, 100)
    count = 1
    while ans := int(input("Try to guess the number: ")):
        
        if random_number < ans:
            print("My number is lower...")
        elif random_number > ans:
            print("My number is higher...")
        elif random_number == ans:
            print("yeah! you found it!")
            break
        
        if count > 3:
            print("Sorry, no more chances left")
            break
        count = count +1

def main():
    guessing_game()

main()
