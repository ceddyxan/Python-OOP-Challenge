# Create a class called Pet with the following attributes:
class Pet:
    def __init__(self, name, hunger = 5, energy = 5, happiness = 5):
        self.name = name
        self.hunger = hunger
        self.energy = energy
        self.happiness = happiness
        self.tricks = []

    def eat(self, amount):
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1) 
        if self.hunger < 2: 
            print(f"{self.name} is full!🍽️")
        elif self.hunger < 10:
            #print(f"{self.name} is eating...") 
            print(f"{self.name} is enjoying the meal! 🍖")
        else:
            print(f"{self.name} is still hungry!🥱")
                      
    def play(self, amount):
        self.happiness = min(10, self.happiness + 2) 
        self.energy = max(0, self.energy - 2) 
        self.hunger = min(10, self.hunger + 1)
        if self.energy > 0:
            print(f"{self.name} is playing and having fun! 🎾")
        else:
            print(f"{self.name} is too tired to play.")
           
    def sleep(self, time):
        self.energy = min(10, self.energy + time) 
        self.happiness = max(0, self.happiness - time) 
        if self.energy < 10:
            print(f"{self.name} is sleeping...")
        else:
            print(f"{self.name} is fully rested!")
                   
    def train(self, trick):
        if self.energy >= 5: # 
            self.tricks.append(trick)
            self.happiness = min(10, self.happiness + 1) 
            self.energy = max(0, self.energy - 2) #
            print(f"{self.name} has learned a new trick: {trick}!")
        else:
            print(f"{self.name} is too tired to train.")

    def show_tricks(self):
        if self.tricks:
            print(f"{self.name} can do the following tricks: {', '.join(self.tricks)}")
        else:
            print(f"{self.name} hasn't learned any tricks yet.")
        

    def get_status(self):
        status = {
            "name": self.name,
            "hunger": self.hunger,
            "energy": self.energy,
            "happiness": self.happiness,
            "tricks": self.tricks
        }
        print(f"Pet Status: {status}")
        print(f"Name: {self.name}")
        print(f"Hunger: {self.hunger}")
        print(f"Energy: {self.energy}")
        print(f"Tricks: {', '.join(self.tricks) if self.tricks else 'None'}")
        self.eat() 
        self.play()
        self.sleep()
        self.show_tricks()
        print(f"Pet's status: Name: {self.name}, Hunger: {self.hunger}, Energy: {self.energy}, Happiness: {self.happiness}")