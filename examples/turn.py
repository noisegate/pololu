import pololu.pololu as pololu

if __name__ == '__main__':

    p = pololu.Pololu(pololu.Pins(enable=22, direction=17, step=27))

    p.speed = 16
    p.stepsleft(400)
    p.stepsright(400)

    print "integer steps 200 = 360 dgs"

    p.goto(200)
    p.goto(0)

    print "float means angle dgs"

    for i in range(9):
        p.goto(i*45.0)
        p.goto(0)
