class Pet:
    PET_TYPES = ["dog", "cat", "rodent", "bird", "reptile", "exotic"]
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception(f"Invalid pet type: {pet_type}. Must be one of {Pet.PET_TYPES}.")
        self.name = name
        self.pet_type = pet_type
        self.owner = None
        if owner:
            self.set_owner(owner)
        Pet.all.append(self)

    def set_owner(self, owner):
        if not isinstance(owner, Owner):
            raise Exception("owner must be an instance of Owner.")
        self.owner = owner
   

class Owner:
    def __init__(self, name):
        self.name = name

    def pets(self):
        return [pet for pet in Pet.all if pet.owner == self]

    def add_pet(self, pet):
        if not isinstance(pet, Pet):
            raise Exception("pet must be an instance of Pet.")
        pet.set_owner(self)

    def get_sorted_pets(self):
        return sorted(self.pets(), key=lambda pet: pet.name)