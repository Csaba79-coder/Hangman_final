import random
import string
import sys


def main():
    lives = 7
    word = guess_word()
    play(word, lives)


def difficulty(i):
    lives = 7
    while True:
        print('Choose a difficulty')
        print("[1] Easy level with 7 lives")
        print("[2] Medium level with 5 lives")
        print("[3] Hard level with 3 lives")
        print("[0] Exit the program")
        option = int(input("Enter your option: "))
        while option != 0:
            if option == 1:
                print("Selected: easy level with 7 lives!")
                return lives
            elif option == 2:
                print("Selected: medium level with 5 lives!")
                return (lives)-2
            elif option == 3:
                print("Selected: hard level with 3 lives!")
                return (lives)-4
            else:
                print("Unknown Option Selected!")
                break
            return difficulty()
        if option == 0:
            print('Thanks for playing with Hangman2.0! Good bye!')
            sys.exit()


def guess_word():
    with open('countries-and-capitals.txt', 'r') as file:
        text = file.read()
        coupital = text.split(' | ')
        position = random.randint(0, len(coupital)-1)
        randword = coupital[position]
        final = randword.split('\n')
        return final[random.randint(0, 1)]


def play(word, lives):
    finished = False
    lives = difficulty(i=True)
    print('Starting game now!')
    print('Here\'s the word to guess!')
    guess_letter = []
    guess_letters = []
    unknown_word = []
    guessed_letter = []
    collect_letter = []
    printed_unknown_word = ""
    for char in word:
        if char == ' ':
            unknown_word.append(char)
        else:
            unknown_word.append("_ ")
    for x in unknown_word:
        printed_unknown_word += x
    print(printed_unknown_word+"\n")
    print(word)

    while not finished:
        tries(lives)
        guess_letters = input('What is your letter? ')

        if guess_letters == "quit":
            print("Thank you for playing with us, welcome back any time!")
            sys.exit()

        for index, char in enumerate(word):
            if char == guess_letters.lower() or char == guess_letters.upper():
                unknown_word[index] = word[index]
            printed_unknown_word = ''
            for char_in_unknown_word in unknown_word: # letakart szó
                printed_unknown_word += char_in_unknown_word
        print(printed_unknown_word)

        if guess_letters.lower() in word.lower():
            if guess_letters in guessed_letter:
                print("You have already guessed this letter, and it is in the word please guess again!")
            else:
                print("Good guess! Letter is in word!")
        elif guess_letters.lower() not in guessed_letter:
            print("Guess letter is not in word, please guess again!")
            if type(guess_letters) == string:
                collect_letter.append(guess_letters.lower())
                lives -= 1
        elif guess_letters.lower() in guessed_letter:
            print("You have already guessed this letter, and it is not in the word, please guess again!")

        guessed_letter.append(guess_letters.lower())
        print(collect_letter)

        if '_ ' not in printed_unknown_word:
            finished = True
            with open('Win', 'r') as complete:
                Win = complete.read()
            print(Win)
            print("You've won!")
            valid_answer = False
            while not valid_answer:
                new_game = input('Would you like another game? y = Yes n = No: ')
                if new_game == "y":
                    valid_answer = True
                    main()
                elif new_game == "n":
                    valid_answer = True
                    print("Good bye, see you soon!")
                    sys.exit()
                else:
                    print("Please give a valid input!")


def tries(lives):
    if lives >= 7:
        with open('Hanging(7)', 'r') as seven:
            se = seven.read()
        print(se)
    elif lives == 6:
        with open('Hanging(6)', 'r') as six:
            si = six.read()
        print(si)
    elif lives == 5:
        with open('Hanging(5)', 'r') as five:
            fi = five.read()
        print(fi)
    elif lives == 4:
        with open('Hanging(4)', 'r') as four:
            fo = four.read()
        print(fo)
    elif lives == 3:
        with open('Hanging(3)', 'r') as three:
            th = three.read()
        print(th)
    elif lives == 2:
        with open('Hanging(2)', 'r') as two:
            tw = two.read()
        print(tw)
    elif lives == 1:
        with open('Hanging(1)', 'r') as one:
            on = one.read()
        print(on)
    else:
        with open('Hanging(0)', 'r') as game_over:
            lose = game_over.read()
        print(lose)
        while True:
            new_game = input('Would you like another game? y = Yes n = No: ')
            if new_game == "y":
                valid_answer = True
                main()
            elif new_game == "n":
                valid_answer = True
                print("Good bye, see you soon!")
                sys.exit()
            else:
                print("Please give a valid input!")


if __name__ == '__main__':
    print('Welcome to Hangman 2.0')
    name = input('What is your name? ')
    print('Good luck '+ name.capitalize() + '!')
    main()