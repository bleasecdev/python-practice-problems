# Write four classes that meet these requirements.
#
# Name:       Animal
#
# Required state:
#    * number_of_legs, the number of legs the animal has
#    * primary_color, the primary color of the animal
#
# Behavior:
#    * describe()       # Returns a string that describes that animal
#                         in the format
#                                self.__class__.__name__
#                                + " has "
#                                + str(self.number_of_legs)
#                                + " legs and is primarily "
#                                + self.primary_color
#
#
# Name:       Dog, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Bark!"
#
#
#
# Name:       Cat, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Miao!"
#
#
#
# Name:       Snake, inherits from Animal
#
# Required state:       inherited from Animal
#
# Behavior:
#    * speak()          # Returns the string "Sssssss!"


class Animal: 
    def __init__(self, number_of_legs, primary_color) -> None:
        self.number_of_legs = number_of_legs
        self.primary_color = primary_color
    
    def describe(self):
        return self.__class__.__name__ + " has " + str(self.number_of_legs) + " legs and is primarily " + self.primary_color

class Dog(Animal):
    def speak():
        return "Bark!"

class Cat(Animal):
    def speak():
        return "Miao!"

class Snake(Animal):
    def speak():
        return "Sssssss!" 


dog = Dog(4, "black")
cat = Cat(4, "brown")
snake = Snake(0, "Green")

print(dog.describe())
print(cat.describe())
print(snake.describe())
