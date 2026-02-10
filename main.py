import time
from modules.game import Game


def main():
    game = Game()
    game.update_player_names()
    for round in range(1, 14):
        print(f"\nRound {round}!\n")
        time.sleep(1)
        for player in game.get_player_names():
            print(f"Player '{player.title()}', it's your turn!\n")
            time.sleep(1)
            game.play_round()


if __name__ == "__main__":
    main()