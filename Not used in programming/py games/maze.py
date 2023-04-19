import random

# Define the class for the card object
class Card:
    def __init__(self):
        self.num1 = random.randint(1, 10)
        self.num2 = random.randint(1, 10)
        self.operation = random.choice(['+', '-', '*'])
        self.answer = eval(f"{self.num1} {self.operation} {self.num2}")
        self.text = f"{self.num1} {self.operation} {self.num2} = ?"

    def __str__(self):
        return self.text

# Define the function for playing the game
def play_game():
    # Create the deck of cards
    deck = []
    for i in range(10):
        card = Card()
        deck.append(card)

    # Shuffle the deck
    random.shuffle(deck)

    # Draw the cards and play the game
    player_score = 0
    computer_score = 0
    for i in range(10):
        card = deck.pop(0)
        print(f"Card {i+1}: {card.text}")
        player_answer = int(input("Your answer: "))
        if player_answer == card.answer:
            print("Correct! You get to keep the card.")
            player_score += 1
        else:
            print("Incorrect! The computer gets to keep the card.")
            computer_score += 1
        computer_answer = card.answer + random.randint(-2, 2)
        print(f"Computer's answer: {computer_answer}")
        if computer_answer == card.answer:
            print("Correct! The computer gets to keep the card.")
            computer_score += 1
        else:
            print("Incorrect! You get to keep the card.")
            player_score += 1

    # Determine the winner
    if player_score > computer_score:
        print(f"You win with {player_score} cards!")
    elif computer_score > player_score:
        print(f"The computer wins with {computer_score} cards!")
    else:
        print("It's a tie!")

# Play the game
play_game()
