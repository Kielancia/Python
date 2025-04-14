import random
import hangman_words
import hangman_art

lives = 6

print(hangman_art.logo)
chosen_word = random.choice(hangman_words.word_list)
print(chosen_word)

placeholder = ''
while len(placeholder) != len(chosen_word):
    placeholder += '_'
print(placeholder)

storage = ""
game_over = False

while not game_over and lives > 0:
    display = ""
    print(f"****************************<???>/{lives} LIVES LEFT****************************")
    guess = input("Guess a letter: ").lower()
    for letter in chosen_word:
        if letter == guess:
            if guess in storage:
                print(f"You've already guessed {guess}")
            display += letter
            storage += letter
        elif letter in storage:
            display += letter
        else:
            display += "_"
    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")
    print(display)
    if "_" not in display:
        game_over = True
        print("****************************YOU WIN****************************")
    elif lives == 0:
        game_over = True
        print(f"***********************YOU LOSE**********************")
        print(f"The word you were trying to guess was: {chosen_word}")
    print(hangman_art.stages[lives])


