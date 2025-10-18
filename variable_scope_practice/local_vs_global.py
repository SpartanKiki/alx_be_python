# exercise1_local_vs_global.py

# This is a global variable
message = "I'm Global!"

def show_message():
    # This is a local variable with the same name
    message = "I'm Local!"
    print("Inside the function:", message)

# Outside the function
print("Outside the function:", message)

# Calling the function
show_message()

# Back outside the function again
print("After the function call:", message)
