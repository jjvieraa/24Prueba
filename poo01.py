# Define a class named 'Dog'  
class Dog:  
    # Constructor method that initializes the attributes 'name' and 'age' of the dog  
    def __init__(self, name, age):  
        self.name = name # Assign the value of the parameter 'name' to the instance variable 'name'  
        self.age = age    # Assign the value of the parameter 'age' to the instance variable 'age'     
    # Method that makes the dog "bark" by printing "Wuff!"  
    def bark(self):  
        print("Wuff!")  
    
# Create an instance of the 'Dog' class with the name "Bello" and age 5  
my_dog = Dog("Bello", 5)  
# Call the 'bark' method of the 'my_dog' instance  
my_dog.bark()


try:  
    # Attempt to divide 10 by 0, which will raise a ZeroDivisionError  
    x = 10 / 0  
except ZeroDivisionError:  
    # Handle the ZeroDivisionError by printing an error message  
    print("You cannot divide by zero!")  
finally:  
    # This block is always executed, regardless of whether an exception occurred or not
    print("The program continues to run.")

