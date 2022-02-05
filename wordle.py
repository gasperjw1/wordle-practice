# imports
import random

# Prints each row in box
def printRow(currRow, answer):
    # Useless letter
    uL_TB = " - "
    uL_S1 = "|"
    uL_S2 = "|"

    # Useful letter in wrong place
    uF_TB = " ^ "
    uF_S1 = "<"
    uF_S2 = ">"

    # Correct letter in correct place
    c_TB = " * "
    c_S1 = "*"
    c_S2 = "*"

    correctLettersLeft = []
    index = 0
    for letter in answer:
        correctLettersLeft.append([letter,index])
        index += 1
    
    printList = []
    index = 0
    for letter in currRow:
        found = False
        correctPlace = False
        for l in correctLettersLeft:
            if l[0] == letter:
                found = True
                if l[1] == index:
                    correctPlace = True
                correctLettersLeft.remove(l)
        if found:
            if correctPlace:
                printList.append(3)
            else:
                printList.append(2)
        else:
            printList.append(1)
        index += 1
    
    for item in printList:
        if item == 1:
            print(uL_TB, end = '')
        elif item == 2:
            print(uF_TB, end = '')
        elif item == 3:
            print(c_TB, end = '')
    print()

    index = 0
    for item in printList:
        if item == 1:
            print(uL_S1 + currRow[index] + uL_S2, end = '')
        elif item == 2:
            print(uF_S1 + currRow[index] + uF_S2, end = '')
        elif item == 3:
            print(c_S1 + currRow[index] + c_S2, end = '')
        index += 1
    print()
    
    for item in printList:
        if item == 1:
            print(uL_TB, end = '')
        elif item == 2:
            print(uF_TB, end = '')
        elif item == 3:
            print(c_TB, end = '')
    print()

# Checks if word exists or not
def checkWord(word, gList):
    return len(word) == 5 and word in gList

def main():
    # Opening text files
    answerList = {}
    guessList = {}
    with open('answer_list.txt') as answerFile:
        dataFull = answerFile.read().split('\n')

        for word in dataFull:
            answerList[word] = 1
            guessList[word] = 1
        answerFile.close()
    with open('word_list.txt') as guessFile:
        dataFull = guessFile.read().split('\n')

        for word in dataFull:
            guessList[word] = 1
        guessFile.close()

    pastWords = []
    legend = "Legend:\nIf a letter is surrounded by |-| then the letter is not part of the answer\n\
    If a letter is surrounded by <^> then the letter is part of the answer but the placement is incorrect\n\
    If a letter is surrounded by *** then the letter is in the correct position compared to the answer\n"

    while True:
        print(legend)
        rounds = len(pastWords) + 1
        print('\nHistory: ', pastWords, '\n\nRound', rounds, '\n')
        answer = [k for k in answerList.keys()][random.randint(0,len(answerList.keys()))]

        guesses = [
            [
                ' ', ' ', ' ', ' ', ' '
            ],[
                ' ', ' ', ' ', ' ', ' '
            ],[
                ' ', ' ', ' ', ' ', ' '
            ],[
                ' ', ' ', ' ', ' ', ' '
            ],[
                ' ', ' ', ' ', ' ', ' '
            ]
        ]

        lettersNotUsed = list('abcdefghijklmnopqrstuvwxyz')
        lettersUsedButNotInAnswer = []
        lettersUsedAndInAnswer = []

        for i in range(5):
            guess = ''
            while not checkWord(guess, guessList):
                guess = input('Enter next guess: ')
            
            guesses[i] = list(guess)

            for letter in guess:
                if letter in lettersNotUsed:
                    if letter in answer:
                        lettersUsedAndInAnswer.append(letter)
                    else:
                        lettersUsedButNotInAnswer.append(letter)
                    lettersNotUsed.remove(letter)  

            for row in guesses:
                printRow(row, list(answer))
            
            if guess == answer:
                pastWords.append("Round " + str(rounds) + ": " + answer + " in " + str(i+1) + " guesses")
                print("\n\n")
                break
            elif i == 4:
                pastWords.append("Round " + str(rounds) + ": " + answer + " in - guesses")
                print("\n\n")
            else:
                print()
                print("Letters not used: ", lettersNotUsed)
                print("Letters not in answer: ", lettersUsedButNotInAnswer)
                print("Letters in answer: ", lettersUsedAndInAnswer)
                print()

if __name__ == "__main__":
    main()
