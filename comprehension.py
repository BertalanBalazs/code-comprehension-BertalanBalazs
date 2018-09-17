import random # Import the random module so we can assign for that below.

guesses_taken = 0 # count the quesses and store it in this variable

print('Hello! What is your name?') # output the welcome texts
myName = input()    # get the name from the user

number = random.randint(1, 20)  # making random numbers between 1 and 20
print('Well, ' + myName + ', I am thinking of a number between 1 and 20.') # output the riddle's sentece with the username

while guesses_taken < 6: # while guesses_taken below value 6 the while loop will execute
    print('Take a guess.') # ask the user to guess for a number
    guess = input() # user have to type 1 number
    guess = int(guess) # make an integer from the guess value

    guesses_taken += 1 # increase the variable values from 1

    if guess < number: #examine that the guess is below the thougt number 
        print('Your guess is too low.') # output that the quess is below the tought number

    if guess > number: #examine that the guess is above the thougt number
        print('Your guess is too high.') # output that the quess is above the tought number

    if guess == number: # examine that the quess equal with the number
        break # if yes the progrma exit from this loop

if guess == number: # examine that the quess equal with the number
    guesses_taken = str(guesses_taken) # make string from the guesses_taken value
    print('Good job, ' + myName + '! You guessed my number in ' + guesses_taken + ' guesses!') # output the congratulation sentences

if guess != number: # examine that the not quess equal with the number
    number = str(number) # make an integer from the guess value 
    print('Nope. The number I was thinking of was ' + number)  # output what was the thougt number
