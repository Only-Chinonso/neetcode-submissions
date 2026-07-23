class SuperHero:
    def __init__(self, name: str, power: str, strength: int):
        self.name = name
        self.power = power
        self.strength = strength
        self.strength_increase = 100
    
    def power_boost(self) -> None:
        self.strength += self.strength_increase
        print(f"{self.name}'s strength increased to {self.strength}!")



# Don't modify the following code
ironman = SuperHero("Iron Man", "Repulsor Beams", 85)

ironman.power_boost()
