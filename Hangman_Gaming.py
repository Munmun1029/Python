import random
import Hangman_stages
print("******* Let's Play HANGMAN GAME *******")
word_list = ['lovemate', 'miss', 'hate', 'soulmate', 'heart mate', 'best friend', 'bff']
lives = 6
choose_word = random.choice(word_list)
display = []
for i in range(len(choose_word)):
    display += '_'
print(display)
game_over = False
while not game_over:
    guess = input("Guess the letter.").lower()
    for position in range(len(choose_word)):
        letter = choose_word[position]
        if letter == guess:
            display[position] = guess
    print(display)
    if guess not in choose_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("Your Loss..")
    if '_' not in display:
        game_over = True
        print("You WIN!!!")

    print(Hangman_stages.stages[lives])