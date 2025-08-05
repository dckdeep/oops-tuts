#initiate a class
class employee:
    def __init__(self):
        self.id = 321
        self.salary = 60000
        self.designation = "Software Engineer"

    def travel(self, destination):
        print(f"Employee is travelling to {destination}")    

#creating an object/instance of the class
sam = employee()

print(sam.id)
print(sam.salary)
print(sam.designation)
sam.travel("New York")

