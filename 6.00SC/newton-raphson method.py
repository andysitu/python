epsilon = 0.01
k = int( raw_input("Enter an integer: ") )
guess = k / 2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    numGuesses += 1
    guess = guess - (((guess**2) - k)/ (2*guess))
print 'Square root of', k, 'is', guess, "with", numGuesses, "guesses."
