import random


class RockPaperScissors:
    """
    RockPaperScissors class:
    This class plays the Rock - Paper - Scissors game
    methods:
    1. get_player_choice
    2. get_computer_choice
    3. decide_winner
    4. play

    """
    def __init__(self, name: str):
        self.choices = ["rock", "paper", "scissors"]
        self.name = name

    def get_player_choice(self):
        """
        This function get the players' choice.
        there are only three choices

        Returns:
            users choice and raise an error if the input is wrong 
        """
        user_choice = input(f"Enter your choice ({self.choices}): ")
        print(f"user choice {user_choice}")
        if user_choice.lower() in self.choices:
            return user_choice.lower()
        print(f"Invalid choice, you must select from {self.choices}")
        return self.get_player_choice()

        
    def get_computer_choice(self):
        """
        This funtion gets the computer's choice using the random built in function.

        Returns:
            computer's chice out or three possible options.
        """
        return random.choice(self.choices)        

    def decide_winner(self, user_choice, computer_choice):
        """
        This function determines who is the winner, you (user) or the computer,
        based on the cpmparison between choices.

        Args:
            user_choice (str): 
            computer_choice (str): 
        Returns:
            winner, tie, cmopuer won!.
        """
        if user_choice == computer_choice:
            return "It is a tie."
        win_combinations = [("rock", "scissors"), ("paper", "rock"), ("scissors", "paper")]
        for win_combination in win_combinations:
            if (user_choice == win_combination[0]) & (computer_choice == win_combination[1]):
                return "Congradulations! You Won!"
            
        return "Oh NO, the computer WON!"

    def play(self):
        user_choice = self.get_player_choice()
        computer_choice = self.get_computer_choice()
        winner_msg = self.decide_winner(user_choice, computer_choice)
        print(f"compuer choice: {computer_choice}")
        print(winner_msg)


        


if __name__ == "__main__":
    game = RockPaperScissors("David")
while True:
    game.play()

    continue_game = input("Do you want to paly again? (Enter ant key to start or q/Q to end the game)")
    if continue_game.lower() == "q":
        break

