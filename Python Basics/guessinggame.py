#GUESSING GAAME

secret_word = "Tiger"
guess = ""
count = 0
guess_limit = 3
limit = 3
out_of_guesses = False

print("The word is a name of an animal \n")
while guess != secret_word and not(out_of_guesses):
    if count < guess_limit :
        guess = input("Enter a guess: ")
        count += 1
        limit -= 1

        if guess != secret_word :
            print("Wrong!! " + f"{limit} Guesses left.")

    else :
        out_of_guesses= True

if out_of_guesses :
    print ("You ran out of tries. The word was", secret_word)
else :
    print("You have guessed correctly")