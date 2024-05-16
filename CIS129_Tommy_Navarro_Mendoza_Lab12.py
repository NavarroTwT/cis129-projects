# Pet class
class Pet:
    def __init__(self, name="", type="", age=0):
        self._name = name
        self._type = type
        self._age = age
        
    # Mutators 
    def setName(self, name):
        self._name = name

    def setType(self, type):
        self._type = type

    def setAge(self, age):
        self._age = age

    def getName(self):
        return self._name

    def getType(self):
        return self._type

    def getAge(self):
        return self._age

def main():
    # Pet object
    animal = Pet()

    # Get inputs for the pet
    input_name = input("Enter a pet name: ")
    animal.setName(input_name)

    input_type = input("Enter a pet type: ")
    animal.setType(input_type)

    input_age = int(input("Enter a pet age: "))
    animal.setAge(input_age)

    # Show values for this pet
    print(f"The pet name is {animal.getName()}")
    print(f"The pet type is {animal.getType()}")
    print(f"The pet age is {animal.getAge()}")

# Call main to test
main()
