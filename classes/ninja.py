class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if self.health <= 0:
            print(f"{self.name} already lost the fight. Can't fight back")
            return self
                
        if pirate.health <= 0:
            print(f'{pirate.name}: "Stop attacking me I already lost."')
            return self

        pirate.health = pirate.health - self.strength
        if pirate.health > 0:
            print(f"{self.name} attacked {pirate.name} for {self.strength} damage. {pirate.name}'s remaining health is {pirate.health}")
            return self
        elif pirate.health <= 0:
            print(f"{self.name} attacked {pirate.name}. {pirate.name}'s remaining health is {pirate.health}. {self.name} Wins!")
            return self