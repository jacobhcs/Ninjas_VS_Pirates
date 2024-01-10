class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 200
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if self.health <= 0:
            print("Can't attack. You're dead.")
            return self
        
        pirate.health = pirate.health - self.strength
        if pirate.health > 0:
            print(f"You attacked the pirate. Pirates remaining health is {pirate.health}")
        elif pirate.health <= 0:
            print(f"The pirates health is {pirate.health}. You Win")
        return self