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
        self.Name = f"Plr {randint(0, 99)}"
        self.Health = 100
        self.Energy = 100
        self.Damage = 10
        self.Path = PathClass(0, 0, 0, "Default")
        self.Table = Table

    def ChooseAction(self):
        Choice = randint(0, 2)

        if Choice == 0:
            self.Attack()

    def Attack(self):
        if self.Table.Players.__len__() <= 1:
            return

        Choice = randint(0, len(self.Table.Players) - 1)

        self.Table.Players[Choice].Health -= self.Damage + self.Path.Damage

        print(f"Player {self.Name} has attacked Player {self.Table.Players[Choice].Name} for {Fore.RED + str(self.Damage + self.Path.Damage)} {Fore.RESET + "damage"}.")

Table = TableClass(3)
while Table.Players.__len__() > 1:
    Table.Turn += 1
    print(f"\n\nTurn {Table.Turn}")

    for i, Player in enumerate(Table.Players):
        Player.ChooseAction()

    PlayersToRemove = []
    for i, Player in enumerate(Table.Players):
        if Player.Health <= 0:
            PlayersToRemove.append((i, Player))
            break
    for i, Player in PlayersToRemove:
        print(f"Player {Player.Name} has died this turn.")
        Table.Players.pop(i)

    print()
    for i, Player in enumerate(Table.Players):
        print(f"Player {Player.Name} has {Player.Health} health remaining.")

    input("Press Enter to continue...")

print("\n")
print(Fore.YELLOW + f"Player {Table.Players[0].Name} has won the game!")