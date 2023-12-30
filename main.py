from connect_four import ConnectFour


def main():
    while True:
        game = ConnectFour()
        if not game.play():
            break

main()