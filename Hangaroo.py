from isWordGuessed import isWordGuessed
from getGuessedWord import getGuessedWord
from getAvailableLetters import getAvailableLetters
def hangaroo(secretWord): 
        print('Welcome to Hangaroo')
        secretWord=secretWord.lower()
        secretWord=list(secretWord)
        lettersGuessed=[]
        x=isWordGuessed(secretWord,lettersGuessed)
        y=0
        while x!=True:
            x=isWordGuessed(secretWord,lettersGuessed)
            guess=input('Guess a letter:')
            guess = guess.lower()
            if ((guess in secretWord) and (guess not in lettersGuessed)):
                lettersGuessed.append(guess)
            #para mag store yung letters
                blue=getGuessedWord(secretWord,lettersGuessed)
                red=getAvailableLetters(lettersGuessed)
                print(blue,'Available letters:',red)
                x=isWordGuessed(secretWord,lettersGuessed)
            elif ((guess not in secretWord) and (guess not in lettersGuessed)):
                y += 1 
            else:
                print('try again:the letter is already given')
        else :
            print('you win!')
            print('number of mistakes',y)
            return print('Game Over!','The answer is:',secretWord,'Your answer is:',lettersGuessed)
            
            
