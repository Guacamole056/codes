animal = [""] * 20
colour = [""] * 10
ColourTopPointer = 0
AnimalTopPointer = 0
#Checking how this works

def push_animal(DataToPush):
    global AnimalTopPointer
    if AnimalTopPointer == len(animal):
        return False
    else:
        animal[AnimalTopPointer] = DataToPush
        AnimalTopPointer = AnimalTopPointer + 1
        return True


def pop_animal():
    global AnimalTopPointer
    if AnimalTopPointer == 0:
        return ""
    else:
        ReturnData = animal[AnimalTopPointer - 1]
        AnimalTopPointer = AnimalTopPointer - 1
        return ReturnData


def push_colour(DataToPush):
    global ColourTopPointer
    if ColourTopPointer == len(colour):
        return False
    else:
        colour[ColourTopPointer] = DataToPush
        ColourTopPointer = ColourTopPointer + 1
        return True


def pop_colour():
    global ColourTopPointer
    if ColourTopPointer == 0:
        return ""
    else:
        ReturnData = colour[ColourTopPointer - 1]
        ColourTopPointer = ColourTopPointer - 1
        return ReturnData


push_animal("eagle")
push_animal("cat")
push_animal("dog")
print(animal)

push_colour("red")
push_colour("green")
push_colour("blue")
print(colour)


def output_item():
    PoppedAnimal = pop_animal()
    PoppedColour = pop_colour()
    if PoppedColour == "" and PoppedAnimal == "":
        print("No colour")
        print("No animal")
    elif PoppedColour == "":
        print("No colour")
        push_animal(PoppedAnimal)
    elif PoppedAnimal == "":
        print("No animal")
        push_colour(PoppedColour)
    else:
        print(PoppedColour, PoppedAnimal)


output_item()
