# Task 4
def make_hangman(secret_word):
    guesses=[]
    def hangman_closure(letter):
        guesses.append(letter)
        display = ''.join(ch if ch in guesses else '_' for ch in secret_word)
        print(display)
        return all(ch in guesses for ch in secret_word)

    return hangman_closure

secret = input("Enter the secret word: ")
game = make_hangman(secret)
done = False
while not done:
    letter = input("Guess a letter: ")
    done = game(letter)
print("You got it!")

