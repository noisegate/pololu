import pololu.pololu as pololu

if __name__ == '__main__':
    instance = pololu.Pololu(pololu.Pins(enable=22, direction=24, step=23))
    instance.disable()
 
