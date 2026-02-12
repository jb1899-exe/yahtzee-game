import time
from modules.game import Game
from modules.player import Player


def main():
    game = Game()
    game.update_player_names()
    players = [Player(name) for name in game.get_player_names()]

    if players:
        for round in range(1, 14):
            print(f"\n\nRound {round}!")
            # time.sleep(1)
            for player in players:
                print(f"\n\nPlayer {player.name.title()}, it's your turn!")
                # time.sleep(1)
                game.play_round(player)
                # TODO: Print user's score at end of each round
    else:
        print("Quitting game...\n")


if __name__ == "__main__":
    main()