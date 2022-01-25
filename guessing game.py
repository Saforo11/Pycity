# The guessing game
i = 1
correct_num = 3
while i <= 3:
    guess_num = input('Guess the number: ')
    i += 1
    if int(guess_num) == correct_num:
        print('Well Done! You guessed right')
        break
else:
    print('Sorry, you failed')