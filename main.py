import random
number = random.randint(1, 10)

player_name = input("Hello, What's your name?")
number_of_guesses = 0
print('okay! '+ player_name+ ' I am Guessing a number between 1 and 10:')

while number_of_guesses < 5:
    guess = int(input())
    number_of_guesses += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        break
if guess == number:
    print('You guessed the number in ' + str(number_of_guesses) + ' tries!')
else:
    print('You did not guess the number, The number was ' + str(number))

 # Ask user to input name
 # Set number of guesses to zero
 # print "Ok user Im guessing a number"
 # While number of guesses is less than 5 do below command
 #   ask user to input guess number
 #   add one to the number of guessess
 #   if user's guess number is less than random number
 #       print "your guess is too low"
 #   if user's guess number is more than random number
 #       print "your guess is too high"
 #   if user's guess number is equal to random number
 #       stop while loop
 # if user's guess number equal the random number 
 #    print " you guessed the number in number of guesses times tries"
 # otherwise print" you did not guess the number and number was: "
 #End program