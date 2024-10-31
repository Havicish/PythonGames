from random import randint
from os import system as sys
from colorama import Fore, Back, Style

class TableClass:
    def __init__(self, PlayerCount) -> None:
        self.Potions = []
        self.Paths = []
        self.Players = []

        self.Turn = 0

        for i in range(PlayerCount):
            self.Players.append(PlayerClass(self))

class PathClass:
    def __init__(self, Health, Energy, Damage, Name) -> None:
        self.Health = Health
        self.Energy = Energy
        self.Damage = Damage
        self.Name = Name

class PlayerClass:
    def __init__(self, Table: TableClass) -> None:
        self.Name = f"Plr{randint(0, 99)}"
        self.Health = 100
        self.Energy = 100
        self.Damage = 10
        self.Defense = 1.5 # Incoming damage will be divided by this number
        self.Defending = 0 # How many turns the player will be defending
        self.SavingEnergy = 0 # How many turns the player will be saving energy
        self.Path = PathClass(0, 0, 0, "Default")
        self.Table = Table

    def ChooseAction(self):
        if self.SavingEnergy > 0:
            print(f"Player {self.Name} is saving energy.")
            return

        Choice = randint(0, 2)

        if Choice == 0:
            self.Attack()

        if Choice == 1:
            self.Heal()

        if Choice == 2:
            self.Defend()

    def Attack(self):
        if self.Table.Players.__len__() <= 1:
            return
        
        if self.Energy < 5:
            return
        
        self.Energy -= 5

        Choice = randint(0, len(self.Table.Players) - 2)
        if self.Table.Players[Choice].Name == self.Name:
            Choice = (Choice + 1) % len(self.Table.Players)

        DefenceDivisor = 1
        if self.Table.Players[Choice].Defending > 0:
            DefenceDivisor = self.Table.Players[Choice].Defense

        self.Table.Players[Choice].Health -= round((self.Damage + self.Path.Damage) / DefenceDivisor)

        print(f"Player {self.Name} has attacked Player {self.Table.Players[Choice].Name} for {Fore.RED + str(round((self.Damage + self.Path.Damage) / DefenceDivisor)) + Fore.RESET} damage.")

    def Heal(self):
        if self.Health >= 90:
            return

        if self.Energy < 25:
            self.SavingEnergy = min(self.SavingEnergy + 2, 3)
            print(f"Player {self.Name} failed to heal.")
            return
        
        self.Energy -= 25

        self.Health += 10 + self.Path.Health

        print(f"Player {self.Name} has healed for {Fore.GREEN + str(10 + self.Path.Health) + Fore.RESET} hp.")

    def Defend(self):
        if self.Energy < 10:
            return

        self.Energy -= 10
        self.Defending += 2

        print(f"Player {self.Name} is defending.")

Table = TableClass(3)
while Table.Players.__len__() > 1:
    Table.Turn += 1

    print("\n\n\n\n\n\n\n")
    print(f"\n\nTurn {Table.Turn}")

    for i, Player in enumerate(Table.Players):
        Player.Energy += 5
        Player.Energy = min(Player.Energy, 100)
        Player.ChooseAction()

        Player.Defending = max(Player.Defending - 1, 0)
        Player.SavingEnergy = max(Player.SavingEnergy - 1, 0)

    PlayersToRemove = []
    for i, Player in enumerate(Table.Players):
        if Player.Health <= 0:
            PlayersToRemove.append((i, Player))
            break
    for i, Player in PlayersToRemove:
        print(Fore.RED + f"Player {Player.Name} has died this turn." + Fore.RESET)
        Table.Players.pop(i)

    print()
    for i, Player in enumerate(Table.Players):
        if Player.Defending == 0:
            print(f"Player {Player.Name} has:")
        else:
            print(f"Player {Fore.WHITE + Player.Name + Fore.RESET} has:")
        print(f"    {Fore.GREEN + str(Player.Health) + Fore.RESET} health.")
        print(f"    {Fore.YELLOW + str(Player.Energy) + Fore.RESET} energy.")

    input("Press Enter to continue...")

print("\n")
print(Fore.YELLOW + f"Player {Table.Players[0].Name} has won the game!")