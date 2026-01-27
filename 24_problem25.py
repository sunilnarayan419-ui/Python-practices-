# Guess The Number Game

class NumberGame:
    """ This program allows the user to guess a number """

    def __init__(self, number):
        self.number = number 

    def play(self):
        while True:
            try:
                guess = int(input("Enter your guess number: "))

                if guess == self.number:
                    print("Congratulations!! You guessed the correct number ")
                    break
                else:
                    print("It's wrong!! Try again.")

            except ValueError:
                print("Please enter a valid number!")


# RUN THE GAME
game = NumberGame(123)
game.play()
