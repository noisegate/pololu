import pololu.pololu as pololu

if __name__ == '__main__':

    p = pololu.Pololu(pololu.Pins(enable=22, direction=24, step=23))

    p.speed = 60
    p.stepsleft(400)
    p.stepsright(400)


