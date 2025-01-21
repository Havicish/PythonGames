from random import *

class Player:
    def __init__(self, Name):
        self.Name = Name
        self.Score = 0
        self.Lives = 3
        self.Items = []
        self.Cams = False
        self.Shop = False
        self.Cash = 0

class Enemy:
    def __init__(self, Name):
        self.Name = Name
        self.Position = 0
        self.Agression = 0
        self.Pause = 0

class Office:
    def __init__(self):
        self.Cams = False
        self.Power = 100
        self.Doors = False
        self.Lights = False
        self.Vents = False

class Shop:
    def __init__(self):
        self.Items = []
        self.RareItemsChance = 0

    def Restock(self, ItemCount):
        ItemsToChooseFrom = ["Battery", "Flashlight", "Water", "Curtain"]
        for _ in range(ItemCount):
            self.Items.append(choice(ItemsToChooseFrom))

class Game:
    def __init__(self):
        self.Player = Player(input("What is your name? "))
        self.Enemies = []
        self.Office = Office()
        self.Shop = Shop()
        self.Day = 0
        self.Time = 0
        self.MaxTime = 3600

