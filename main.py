from pet import Pet

# Create a pet object
pet = Pet("Bosco" , hunger=5, energy=5, happiness=5)
pet2 = Pet("Mutina", hunger=3, energy=8, happiness=7)
pet3 = Pet("Whiskers", hunger=4, energy=6, happiness=9)
print(f"Pets Name: {pet.name},", f"{pet2.name},", f"{pet3.name}")

# Test the pet's methods
pet.eat(0), 
pet.play(0)
pet.sleep(0) 
pet.train("roll over")
pet.train("fetch")
pet.train("play dead")
pet2.eat(5)
pet2.play(5)
pet2.sleep(10)
pet2.train("jump")
pet2.train("dance")
pet3.eat(1)
pet3.play(10)
pet3.sleep(10)
pet3.train("spin")
pet3.train("sit")
pet,pet2,pet3.show_tricks()

print(f"Pet's current status:")
print(f"Name: {pet.name},{ pet2.name}, {pet3.name}")
print(f"Hunger: {pet.hunger},{ pet2.hunger}, {pet3.hunger}")
print(f"Energy: {pet.energy},{ pet2.energy}, {pet3.energy}")
print(f"Happiness: {pet.happiness},{ pet2.happiness}, {pet3.happiness}")
print(f"Tricks: [{', '.join(pet.tricks + pet2.tricks + pet3.tricks) if pet.tricks or pet2.tricks or pet3.tricks else 'None'}]")