import random
class JeuD:
    def _init_(self):
        self.NbrS = random.randint(1, 100)
        self.NbrE = 0

    def Start(self):
        print("Welcome 'guess a number'!")
        print("I think of a number between 1 and 100. Try to guess.")

        while True:
            guess = int(input("guess a number: "))
            self.NbrE += 1
            if guess < self.NbrS:
                print("Too low! Try again...")
            elif guess > self.NbrS:
                print("Too high ! Try again...")
            else:
                print(f"Congratulations! You guessed a number {self.NbrE}tries")
                break
jeu = JeuD()
jeu.Start()