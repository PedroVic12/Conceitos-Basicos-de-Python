# --------------------------------------
# Formas de conversar com o pc com input

# name = input("Qual seu nome?")
# print("Hello, " + name)
# print (f"hello, {name}")



print("--------------------------------------")
# Condiçoes
# n = int(input("number: "))

# if n > 0:
#     print("N is positve")
# elif n < 0:
#     print("N is not positive")
# else:
#     print("N is zero")

print("--------------------------------------")
# Sequencias e Loop
name = ["Pedro", "Ron", "Hermione", "Harry"]

name.append("Draco")
name.sort()

print(name)


print("--------------------------------------")
coordinateX = 10.0
coordinateY = 20.0

coordinate = (10.0, 20.0)
print(coordinate)

print("--------------------------------------")
# Create an empty set
s = set()

# add Elementos to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements")

for i in [1, 2, 3, 4, 5]:
    print(i)
print("--------------------------------------")

for i in range(6):
    print(i)

print("--------------------------------------")
houses = {"Homem aranha": "Marvel", "Superman": "DC"}
houses["Capitao america"] = "Marvel"
print(houses["Capitao america"])


print("--------------------------------------")
# Funçoes
# def square(z):
#     return z * z


# for w in range(10):
#     print(f"The square of {w} is {square(w)} ")


class flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []

    def add_passenger(self, name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity - len(self.passengers)


flight = flight(3)
print("--------------------------------------")
print("--------------------------------------")

people = ["Harry", "Ron", "Hermione", "Pedro"]
for person in people:
     
    if flight.add_passenger(person):
        print(f"Added {person} to flight")
    else:
        print(f"No avaiable seats for the {person}")
print("--------------------------------------")
print("--------------------------------------")

people = [
    {"name": "Harry", "house": "Marvel"},
    {"name": "Clark Kent", "house": "DC"},
    {"name": "Doutor Estranho", "house": "Marvel"}
]


people.sort(key=lambda person: person["name"])
print(people)