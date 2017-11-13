import random
import time

#__________________________________________________________________________________________________________________________

def p1():
    diff = int(raw_input("\nChoose a difficulty:"
                         "\nEasy (1)"
                         "\nMedium (2)"
                         "\nHard (3)"))

    if diff == 1:
        limit = 10
        num = random.randint(1, limit)
    elif diff == 2:
        limit = 20
        num = random.randint(1, limit)
    elif diff == 3:
        limit = 100
        num = random.randint(1, limit)
    else:
        print("\nInvalid Input.")
        p1()

    while True:
        time.sleep(1)
        guess = int(raw_input("\nChoose a number from 1 to " + str(limit) + "."))

        if guess == num:
            print("\nCongratulations you got it!")
            break
        elif guess < num:
            print("\nThe number you entered is too low.")
        else:
            print("\nThe number you entered is too high.")

#__________________________________________________________________________________________________________________________

def p2():
    diff = int(raw_input("\nChoose a difficulty:"
                         "\nEasy (1)"
                         "\nMedium (2)"
                         "\nHard (3)"))

    p1TGuess = 0
    p2TGuess = 0
    rounds = 1
    p1G = 0
    p2G = 0

    while True:
        time.sleep(1)
        print("\nRound: " + str(rounds))

        if diff == 1:
            limit = 10
            p1Num = random.randint(1, limit)
            p2Num = random.randint(1, limit)
            total = 10
        elif diff == 2:
            limit = 20
            p1Num = random.randint(1, limit)
            p2Num = random.randint(1, limit)
            total = 15
        elif diff == 3:
            limit = 100
            p1Num = random.randint(1, limit)
            p2Num = random.randint(1, limit)
            total = 30
        else:
            print("\nInvalid Input.")
            p2()

        p1Guess = 0
        p2Guess = 0

        while True:
            time.sleep(1)
            guess = int(raw_input("\nIt is your turn player 1. Choose a number from 1 to " + str(limit) + "."))

            p1Guess += 1

            if guess == p1Num:
                print("\nCongratulations player 1. You got it!")
                break
            elif guess < p1Num:
                print("\nSorry player 1. The number you entered is too low.")
            else:
                print("\nSorry player 1. The number you entered is too high.")

        while True:
            time.sleep(1)
            guess = int(raw_input("\nIt is your turn player 2. Choose a number from 1 to " + str(limit) + "."))

            p2Guess += 1

            if guess == p2Num:
                print("\nCongratulations player 2. You got it!")
                break
            elif guess < p2Num:
                print("\nSorry player 2. The number you entered is too low.")
            else:
                print("\nSorry player 2. The number you entered is too high.")

        p1TGuess += p1Guess
        p2TGuess += p2Guess
        time.sleep(1)
        print("\nPlayer 1 ended the round with " + str(p1Guess) + " guesses.")
        time.sleep(1)
        print("\nPlayer 2 ended the round with " + str(p2Guess) + " guesses.")
        rounds += 1

        if p1TGuess >= total or p2TGuess >= total:
            time.sleep(1)
            print("\nPlayer 1 ended the game with " + str(p1TGuess) + " guesses.")
            time.sleep(1)
            print("\nPlayer 2 ended the game with " + str(p2TGuess) + " guesses.")
            time.sleep(1)
            if p1TGuess < p2TGuess:
                print("\nPlayer 1 wins!")
                p1G += 1
            elif p1TGuess > p2TGuess:
                print("\nPlayer 2 wins!")
                p2G += 1
            else:
                print("\nBoth of you have tied that round.")

        if p1G >= 3 or p2G >= 3:
            if p1G > p2G:
                print("\nPlayer 1 won the whole game!")
                break
            elif p1G < p2G:
                print("\nPlayer 2 won the whole game!")
                break

#__________________________________________________________________________________________________________________________

def comp():
    diff = int(raw_input("\nChoose a difficulty:"
                         "\nEasy (1)"
                         "\nMedium (2)"
                         "\nHard (3)"))

    time.sleep(1)

    cDiff = int(raw_input("\nChoose the difficulty for the computer:"
                         "\nEasy (1)"
                         "\nHard (2)"))

    if cDiff != 1 and cDiff != 2:
        print("\nInvalid Input.")
        comp()

    p1TGuess = 0
    compTGuess = 0
    prevGuess = 50
    rounds = 1
    higher = False
    p1G = 0
    compG = 0

    while True:
        time.sleep(1)
        print("\nRound: " + str(rounds))

        if diff == 1:
            limit = 10
            p1Num = random.randint(1, limit)
            compNum = random.randint(1, limit)
            total = 10
        elif diff == 2:
            limit = 20
            p1Num = random.randint(1, limit)
            compNum = random.randint(1, limit)
            total = 15
        elif diff == 3:
            limit = 100
            p1Num = random.randint(1, limit)
            print p1Num
            compNum = 100
            total = 30
        else:
            print("\nInvalid Input.")
            comp()

        p1Guess = 0
        compGuess = 0
        cGuess = limit
        compMax = 100
        compMin = 1

        while True:
            time.sleep(1)
            guess = int(raw_input("\nIt is your turn player 1. Choose a number from 1 to " + str(limit) + "."))

            p1Guess += 1

            if guess == p1Num:
                print("\nCongratulations player 1. You got it!")
                break
            elif guess < p1Num:
                print("\nSorry player 1. The number you entered is too low.")
            else:
                print("\nSorry player 1. The number you entered is too high.")

        while True:
            time.sleep(1)
            print("\nIt is The computer's turn")

            if cDiff == 1:
                cGuess = random.randint(1, limit)
            else:
                range = compMax - compMin
                if range == 1 and compMin == cGuess - 1:
                    cGuess -= 1
                elif range == 1 and compMax == cGuess + 1:
                    cGuess += 1
                else:
                    cGuess = int((range / 2) + compMin)

            compGuess += 1

            time.sleep(1)

            print("\nThe computer guessed " + str(cGuess) + ".")

            if cGuess == compNum:
                print("\nThe computer guessed correctly.")
                break
            elif cGuess < compNum:
                print("\nThe number the computer entered was too low.")
                compMin = cGuess
            else:
                print("\nThe number the computer entered was too high.")
                compMax = cGuess

        p1TGuess += p1Guess
        compTGuess += compGuess
        time.sleep(1)
        print("\nPlayer 1 ended the round with " + str(p1Guess) + " guesses.")
        time.sleep(1)
        print("\nThe computer ended the round with " + str(compGuess) + " guesses.")
        rounds += 1

        if p1TGuess >= total or compTGuess >= total:
            time.sleep(1)
            print("\nPlayer 1 ended the game with " + str(p1TGuess) + " guesses.")
            time.sleep(1)
            print("\nThe computer ended the game with " + str(compTGuess) + " guesses.")
            time.sleep(1)
            if p1TGuess < compTGuess:
                print("\nPlayer 1 wins!")
                p1G += 1
            elif p1TGuess > compTGuess:
                print("\nThe computer wins!")
                compG += 1
            else:
                print("\nBoth of you have tied.")

            if p1G >= 3 or compG >= 3:
                if p1G > compG:
                    print("\nPlayer 1 won the whole game!")
                    break
                elif p1G < compG:
                    print("\nPlayer 2 won the whole game!")
                    break

#__________________________________________________________________________________________________________________________

def main():
    while True:
        time.sleep(1)
        print("\nWelcome to the Guessing Game.")

        time.sleep(1)
        mode = int(raw_input("\nChoose a game mode:"
                             "\n1 Player (1)"
                             "\n2 Player (2)"
                             "\nComputer (3)"))

        if mode == 1:
            p1()
        elif mode == 2:
            p2()
        elif mode == 3:
            comp()
        else:
            print("\nInvalid Input.")
            continue

        choice = raw_input("\nWould you like to play again? (y/n)")
        if choice == "y":
            continue
        else:
            break

#__________________________________________________________________________________________________________________________

main()