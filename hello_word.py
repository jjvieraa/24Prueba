# Esta línea de código imprime la cadena "Hello, World!" en la consola. 
print("hola mundo")
# Esta línea de código solicita al usuario que ingrese su nombre y almacena la entrada en la variable 'name'.  
name = input("What is your name? ")  
# Esta línea de código imprime un saludo personalizado usando la entrada del usuario.  
print(f"Hello, {name}!")


x = 10 # Integer  
y = 3.14 # Float  
name = "Alice"  # String  
is_student = True # Boolean


# Assign the value 18 to the variable 'age'  
age = 18  
# Check if 'age' is greater than or equal to 18

if age >= 18:  # If the condition is true, print " You are an adult."  
    print("You are an adult.")  
# Check if 'age' is greater than or equal to 13 but less than 18  
elif age >= 13:  
# If the condition is true, print " You are a teenager."  
    print("You are a teenager.")  
# If none of the above conditions are true, execute the else block  
else:  print("You are a child.")
  
# Start a for loop that iterates 5 times, with 'i' taking values from 0 to 4  
for i in range(5):  
# Print the current value of 'i'  
    print(i)  

# Initialize the variable 'count' with the value 0  
count = 0  

# Start a while loop that runs as long as 'count' is less than 5 
while count < 5:  
# Print the current value of 'count'

    print(count)  
# Increment 'count' by 1  
    count += 1



# Define a function named 'sayhello' that takes one parameter 'name'  
def sayhello(name):  
	# Print a greeting message by concatenating "Hello, " with the value of 'name' and an exclamation mark  
	print("Hello, " + name + "!")  

# Define a function named add that takes two parameters 'a' and 'b' and returns the sum
def add(a, b):  
	return a + b  

# Call the 'sayhello' function with the argument "Alice"  
sayhello("Alice")  
	
# Call the 'add' function with the arguments 5 and 3  
res = add(5, 3) 
print(res)  # Prints 8 to the terminal
