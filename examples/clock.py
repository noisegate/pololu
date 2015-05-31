import pololu.pololu as pololu
import datetime
import time

if __name__ == '__main__':
    instance = pololu.Pololu(pololu.Pins(enable=22, direction=17, step=27))
    instance.speed = 60
    while (1):
        hour = float(datetime.datetime.now().strftime("%H"))
        minute = float(datetime.datetime.now().strftime("%M"))
        second = float(datetime.datetime.now().strftime("%S"))
        angle = hour/12.0*360 + minute/60.0/30.0 + second/60.0/30.0/5.0
        print angle
        instance.goto(angle)
        time.sleep(2)
 
