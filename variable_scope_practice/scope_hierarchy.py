# exercise3_scope_hierarchy.py

# Global scope
number = 100

def outer():
    # Enclosing scope
    number = 50

    def inner():
        # Local scope
        number = 10
        print("Inner scope number:", number)  # Local wins

    inner()
    print("Enclosing scope number:", number)  # Enclosing wins

outer()
print("Global scope number:", number)  # Global wins
