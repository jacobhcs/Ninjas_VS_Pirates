from classes.ninja import Ninja
from classes.pirate import Pirate

# INSTANTIATING OUR FIGHTERS
michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")

# FIGHT BEGINS HERE. LOOPS THROUGH CODE TILL UNTIL ONE PLAYERS HEALTH IS 0 OR BELOW
while michelangelo.health > 0 and jack_sparrow.health > 0:
    jack_sparrow.attack(michelangelo)
    michelangelo.attack(jack_sparrow)
    print("")
    jack_sparrow.show_stats()
    michelangelo.show_stats()
    print("*" * 100)