# Create a Rectangle class with attributes length and width. 
# Add methods to calculate the area and perimeter of the rectangle.
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def  area(self):
        return self.length * self.width

rectangle = Rectangle(22,70)
print(rectangle.area())


# Define a BankAccount class with attributes balance and account_number.
#  Add methods to deposit and withdraw funds from the account.
class BankAccount:
    def __init__(self,balance,account_number):
        self.balance = balance
        self.account_number = account_number
    def deposit(self,amount):
        self.amount = amount
        return f"You just deposited {self.amount} so your balance is {self.balance}"

    def withdraw(self,amount):
        self.amount = amount
        return f"Your balance is {self.balance}"

bankaccount = BankAccount(2000,"ft10000")
print(bankaccount.deposit(30))

# Create a Car class with attributes make, model, and year.
# Add methods to start and stop the car's engine
class Car:
    def __init__(self,make,model,year):
        self.make =make
        self.model =model
        self.year = year
    def start_engine(self):
        return f"{self.make}"
    def stop_engine(self,distance):
        self.distance = distance
        return f"The car stoped at{self.distance} km per hour"
    
car = Car("toyota","Prado",2022)
print(car.start_engine())
print(car.stop_engine(20))


# Define a Person class with attributes name, age, and occupation.
# Add a method to print out a greeting message that includes 
# the person's name and occupation.
class Person:
    def __init__(self,name,age,occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def  greeting(self):
        return f"hi {self.name}"
person = Person("maria",22,"rich wife")
print(person.greeting())


# Define a Dog class with attributes
#  name, breed, and age. Add methods to bark
#  (print out a message saying "Woof!") and
#  to convert the dog's agefrom human years 
# to dog years (multiply the age by 7).

class Dog:
    def __init__(self,name,breed,age):
        self.name = name
        self.breed= breed
        self.age = age
    def  bark(self,sound):
        self.sound = sound
        return f"the dog {self.sound}"
    
dog = Dog("Tom","German Shepherd",23)
print(dog.bark("woof!"))

languages = ["python", "Java", "Swift", "C", "C++"]

index = 0
while index < len(languages):
    language = languages[index]
    if language == "Swift" or language == "C++":
        index += 1
        continue
    print(language)
    index += 1

    


    