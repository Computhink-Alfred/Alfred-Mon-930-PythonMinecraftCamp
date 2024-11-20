def teleport():
    agent.teleport_to_player()

def moveForward(steps):
    agent.move(FORWARD, steps)

def moveBackward(steps):
    agent.move(BACK, steps)

def moveLeft(steps):
    agent.move(LEFT, steps)

def moveRight(steps):
    agent.move(RIGHT, steps)

def moveUp(steps):
    agent.move(UP, steps)

def moveDown(steps):
    agent.move(DOWN, steps)

def turnLeft():
    agent.turn(LEFT)

def turnRight():
    agent.turn(RIGHT)

def destroyTree(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.move(UP, 1)
    agent.move(DOWN, steps)
    agent.collect_all()

def bulldoze(steps):
    for i in range(steps):
        agent.destroy(FORWARD)
        agent.destroy(LEFT)
        agent.destroy(RIGHT)
        agent.destroy(DOWN)
        agent.collect_all()
        agent.move(FORWARD, 1)

def buildWall():
    for i in range(5):
        for i in range(3):
            agent.place(FORWARD)
            agent.move(UP, 1)
        agent.move(DOWN, 3)
        agent.move(RIGHT, 1)

player.on_chat("come", teleport)
player.on_chat("fw", moveForward)
player.on_chat("bk", moveBackward)
player.on_chat("ml", moveLeft)
player.on_chat("mr", moveRight)
player.on_chat("up", moveUp)
player.on_chat("down", moveDown)
player.on_chat("tl", turnLeft)
player.on_chat("tr", turnRight)
player.on_chat("dup", destroyTree)
player.on_chat("mine", bulldoze)
player.on_chat("wall", buildWall)