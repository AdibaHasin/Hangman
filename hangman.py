import random 
from words import word_list ##importing word from the list of words

def get_word():
    word = random.choice(word_list)  #generating random words
    return word.upper() #converting to upper case


def play(word):
    word_completion = "_" * len (word) #the random word as empty string 
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6
    print(" start game ")
    print(display_hangman(tries))

    print (word_completion)
    print("\n")

    while not guessed and tries > 0:
        guess = input("Guess a letter or a word:").upper()
            
            #letter matches the letter in word list
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters: #guessed the letter once
                    print ("Already guessed the letter", guess)
            elif guess not in word:
                    print(guess, "is not word.")
                    tries-=1
                    guessed_letters.append(guess)
            else:
                print(guess, "is in the word")
                guessed_letters.append(guess)
                word_as_list = list(word_completion) #converting the random word to list
                indices = [i for i, letter in enumerate(word) if letter == guess]
                for index in indices:  #checking the guessed words against the guessed words
                    word_as_list[index] = guess
                    word_completion = "".join(word_as_list) #converting it to string 
                    if "_" not in word_completion:
                        #correct word has been guessed
                        guessed = True

        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print("guessed the word", guess)
            elif guess!=word:
                print (guess, "is not the word")
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word 
        else:
            print("Not a valid guess.")
        print(display_hangman(tries))
        print(word_completion)
        print("\n")
    if guessed:
        print("You win!")

    else:
        print("the word was"+ word + "try next time")
        
                
def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                """,
                # head, torso, both arms, and one leg
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                """,
                # head, torso, and both arms
                """
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                """,
                # head, torso, and one arm
                """
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                """,
                # head and torso
                """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
                # head
                """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
                # initial empty state
                """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """
    ]
    return stages[tries]


def main():
    word = get_word()
    play(word)
    while input("Play Again? (Y/N) ").upper() == "Y":
        word = get_word()
        play(word)


if __name__ == "__main__":
    main()