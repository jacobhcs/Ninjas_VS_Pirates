class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 45
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , ninja ):
        if self.health <= 0:
            print(f"{self.name} Can't attack. You're dead.")
            return self
        
        ninja.health = ninja.health - self.strength
        if ninja.health > 0:
            print(f"{self.name} attacked {ninja.name} for {self.strength} damage. {ninja.name}'s remaining health is {ninja.health}")
            return self
        elif ninja.health <= 0:
            print(f"{self.name} attacked {ninja.name}. {ninja.name}'s remaining health is {ninja.health}. {self.name} Wins!")
            return self