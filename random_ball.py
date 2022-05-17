from random import shuffle

mylist = [' ','o',' ']

def shuffle_list(mylist):
    shuffle(mylist)
    print("Let's lift the cups:")
    print(mylist)

print("There is a ball under one of the three cups. You get four guesses to find out where it is.")
print("The cups will be shuffled after each guess.")

input("Guess One. Which cup do you expect the cup to be under? Cup 1, 2, or 3? ")
shuffle_list(mylist)
guess1 = input("Was your guess correct? ").lower()

if guess1 == "yes":
    print("Good guess!")
    pass
elif guess1 == "no":
    print("Shuffling...")
    input("Guess Two: Cup 1, 2, or 3? ")   
    shuffle_list(mylist)

    guess2 = input("Was your guess correct this time? ").lower()

    if guess2 == "yes":
        print("Good guess!")
        pass
    elif guess2 == "no":
        print("Shuffling...")
        input("Guess three: Cup 1, 2, or 3? ")   
        shuffle_list(mylist)

        guess3 = input("Was your guess correct this time? ").lower()

        if guess3 == "yes":
            print("Good guess!")
            pass
        elif guess3 == "no":
            print("Shuffling...")
            input("Final guess, #four: Cup 1, 2, or 3? ")
            shuffle_list(mylist)

            guess3 = input("Was your guess correct this time? ").lower()

            if guess3 == "yes":
                print("Good guess!")
                pass
            elif guess3 == "no":
                print("Better luck next time!")
                




