import random

player = []
computer = []
computer_score = 0
player_score = 0
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
win_flag = ""  # This flag can have two values 'computer' and 'player'
action = "yes"  # This flag can have two values 'yes' and 'no'
game_end = False


def update_score():
    global player
    global computer
    global computer_score
    global player_score
    computer_score = sum(computer)
    player_score = sum(player)


def game_ends():
    if len(win_flag) > 0 or player_score > 21 or computer_score > 21:
        return True
    else:
        return False


def get_card():
    global player
    global player_score
    player.append(random.choice(cards))
    update_score()


def print_cards():
    print(f"Your Cards: {player}, Your Score: {player_score}")
    print(f"Computer's First card is {computer[0]}")


user = 'yes'
while user == 'yes':
    from art import logo

    print(logo)
    for i in range(2):
        player.append(random.choice(cards))
        computer.append(random.choice(cards))

    # Checking for Black Jack
    if 11 in computer and 10 in computer:
        win_flag = "computer"
    elif 11 in player and 10 in player:
        win_flag = "player"

    # Updating the Scores
    update_score()

    print_cards()
    while player_score <= 21:
        action = input("Do you want to get another Card? 'yes' or 'no'")
        if action == 'yes':
            get_card()
            print_cards()
        else:
            break

    while computer_score < 17 and computer_score <= 21:
        computer.append(random.choice(cards))
        update_score()

    if player_score > 21 and 11 in player:
        player_score -= 10
    if computer_score > 21 and 11 in computer:
        computer_score -= 10
    print(f"Your final Hand: {player}, Your final Score: {player_score}")
    print(f"Computer's final Hand: {computer}, Computer's final Score: {computer_score}")
    if player_score <= 21:
        if computer_score > 21:
            win_flag = "Player"
        elif player_score < computer_score:
            win_flag = "Player"
    else:
        win_flag = "computer"
    print(f"{win_flag} won")
    user = input("Do you want to Play again? 'yes' or 'no'")
