import time
from modules.game import Game


def main():
    game = Game()
    game.update_player_names() #TODO: 'No' response does not quit program
    for round in range(1, 14):
        print(f"\nRound {round}!")
        time.sleep(1)
        for player in game.get_player_names():
            print(f"\nPlayer '{player.title()}', it's your turn!")
            time.sleep(1)
            game.play_round(player)


if __name__ == "__main__":
    main()