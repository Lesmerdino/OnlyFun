import random
import schedule
import time

class Person:
    def __init__(self):
        self.leben = "schlecht"
        self.fortschritt = 0
        self.lebendig = True  
    def arbeiten_an_sich(self):
        if self.lebendig:
            print("Arbeite an dir!")
            self.fortschritt += random.randint(1, 10)
            print(f"Fortschritt: {self.fortschritt}")

            if self.fortschritt >= 100:
                self.leben = "gut"
    def genieße_das_was_du_hast(self):
        if self.lebendig:
            print("Genieße das was du hast!")
    def lebensende_erreichen(self):
        self.lebendig = False
        print("Lebensende erreicht.")

person = Person()

def taegliche_routine():
    while person.lebendig and person.leben == "schlecht":
        person.arbeiten_an_sich()
    
    if person.leben == "gut":
        person.genieße_das_was_du_hast()
schedule.every().day.at("08:00").do(taegliche_routine)
schedule.every().day.at("23:59").do(person.lebensende_erreichen)
while person.lebendig:
    schedule.run_pending()
    time.sleep(1)
