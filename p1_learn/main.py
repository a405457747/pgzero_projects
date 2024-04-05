import pgzrun
player1 = Actor('1.png', [400, 300])
player2 = Actor('2.png', [400, 250])


def draw():
    player1.draw()
    player2.draw()


pgzrun.go();