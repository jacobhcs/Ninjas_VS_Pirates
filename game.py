from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

# jack_sparrow.attack(michelangelo).show_stats()
michelangelo.attack(jack_sparrow).show_stats()
# michelangelo.show_stats()
