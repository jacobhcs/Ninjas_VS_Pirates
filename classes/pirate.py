class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 15
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , ninja ):
        if self.health <= 0:
            print("Can't attack. You're dead.")
            return self
        
        ninja.health = ninja.health - self.strength
        if ninja.health > 0:
            print(f"You attacked the pirate. Pirates remaining health is {ninja.health}")
        elif ninja.health <= 0:
            print(f"The pirates health is {ninja.health}. You Win")
        return self