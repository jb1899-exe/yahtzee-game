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

            for player in players:
                print(f"{player.name.title()} total score: {player.get_player_score_total()}")

            time.sleep(1)
            for player in players:
                print(f"\n\nPlayer {player.name.title()}, it's your turn!")
                time.sleep(1)
                game.play_round(player)
    else:
        print("Quitting game...\n")


if __name__ == "__main__":
    main()