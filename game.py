from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

jack_sparrow.attack(michelangelo)
michelangelo.attack(jack_sparrow)
print("")
jack_sparrow.show_stats()
michelangelo.show_stats()
print("*"*100)
jack_sparrow.attack(michelangelo)
michelangelo.attack(jack_sparrow)
print("")
jack_sparrow.show_stats()
michelangelo.show_stats()