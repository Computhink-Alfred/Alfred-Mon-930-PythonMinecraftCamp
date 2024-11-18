def teleport():
    agent.teleport_to_player()

def moveForward():
    agent.move(FORWARD, 1)

def moveBackward():
    agent.move(BACK, 1)

def moveLeft():
    agent.move(LEFT, 1)

def moveRight():
    agent.move(RIGHT, 1)

def moveUp():
    agent.move(UP, 1)

def moveDown():
    agent.move(DOWN, 1)

def turnLeft():
    agent.turn(LEFT)

def turnRight():
    agent.turn(RIGHT)

player.on_chat("come", teleport)
player.on_chat("fw", moveForward)
player.on_chat("bk", moveBackward)
player.on_chat("ml", moveLeft)
player.on_chat("mr", moveRight)
player.on_chat("up", moveUp)
player.on_chat("down", moveDown)
player.on_chat("tl", turnLeft)
player.on_chat("tr", turnRight)