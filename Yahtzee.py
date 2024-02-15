import random

class Player:
    def __init__(self, name):
        self.name = name
        self.dice = [0, 0, 0, 0, 0]
        self.score = 0

    def name_player(self):
        self.name = input("Enter name:")

    def roll_dice(self, num_dice):
        self.dice = [random.randint(1, 6) for _ in range(num_dice)]
        return self.dice

    def reroll_dice(self, dice_to_reroll):
        for i in dice_to_reroll:
            if 1 <= i <= 5:
                self.dice[i - 1] = random.randint(1, 6)
        return self.dice

    def cur_dice(self):
        print(f"{self.name}'s dice are: {self.dice}")

    def player_round(self, round_number):
        if round_number == 1:
            self.roll_dice(5)
            print(f"{self.name}'s first roll is: {self.dice}")
        else:
            while True:
                reroll_option = input("Would you like to reroll? type y or n: ")
                if reroll_option == "y":
                    dice_to_reroll = list(
                        map(int, input("Enter the indices of dice to reroll (e.g., 1 3 5) (separate with spaces): ").split()))
                    self.reroll_dice(dice_to_reroll)
                    print(f"{self.name}'s rerolled dice are: {self.dice}")
                    break
                elif reroll_option == "n":
                    print("Okay")
                    break


def print_rules():
    print("Yahtzee Rules:")
    print("1. The game consists of 13 rounds.")
    print("2. In each round, you can roll the dice up to 3 times.")
    print("3. After each roll, you can choose which dice to keep.")
    print("4. After the third roll, you must choose a category to score in.")
    print("5. The score is calculated based on the chosen category.")
    print("6. The player with the highest total score at the end wins.")



def run_game():
    print_rules()
    num_players = int(input("How many players? Maximum of 4"))
    players = []
    for i in range(num_players):
        player = Player("")
        player.name_player()
        players.append(player)

    for round_number in range(1, 4):
        for player in players:
            player.player_round(round_number)


if __name__ == "__main__":
    run_game()
