class House:
    def __init__(self, name, traits):
        self.name = name
        self.traits = traits

houses = [
    House("Gryffindor", ["brave", "daring", "courageous", "chivalrous"]),
    House("Slytherin", ["ambitious", "cunning", "resourceful", "shrewd"]),
    House("Hufflepuff", ["loyal", "trustworthy", "hard-working", "just"]),
    House("Ravenclaw", ["wise", "intelligent", "creative", "witty"]),
]

def get_house():
    courage = int(input("Have you ever faced a dangerous situation and stood your ground? (1- Definitely yes, 2- Maybe, 3- No) "))
    ambition = int(input("Do you have a strong desire to be the best at what you do? (1- Definitely yes, 2- Maybe, 3- No) "))
    loyalty = int(input("Are you someone who values loyalty and trust? (1- Definitely yes, 2- Maybe, 3- No) "))
    wisdom = int(input("Do you consider yourself a wise and intelligent person? (1- Definitely yes, 2- Maybe, 3- No) "))

    points = [courage, ambition, loyalty, wisdom]
    house = ""
    highest_points = 0

    for h in houses:
        current_points = sum([point if trait in h.traits else 0 for point, trait in zip(points, h.traits)])
        if current_points > highest_points:
            highest_points = current_points
            house = h.name

    return house

print("Welcome to the Sorting Hat ceremony!")
print("Based on your answers, you might belong to the following house: " + get_house().capitalize())