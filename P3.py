                                          #   Project-3 [ Random Password Generator ] , Level-1

# Import necessary libraries
import string
import random
import tkinter as tk
from tkinter import messagebox

# Function to generate a password based on given criteria
def generate_password(min_length, numbers=True, special_characters=True):
#  min_length: The minimum length of the password.
#  numbers: Boolean indicating whether to include numbers (default is True).
#  special_characters: Boolean indicating whether to include special characters (default is True).
   
    # Define character sets
    s1 = string.ascii_letters  # All letters (uppercase and lowercase)
    s2 = string.digits  # All digits (0-9)
    s3 = string.punctuation  # All punctuation characters

    # Create the pool of characters based on user preferences
    characters = s1                                             
    if numbers:                                         # If numbers is True, it adds digits.
        characters += s2  # Add digits if requested
    if special_characters:
        characters += s3  # Add special characters if requested

    # Initialize variables
    pwd = ""  # Empty string to store the password
    meets_criteria = False  # Flag to check if all criteria are met
    has_number = False  # Flag to check if password has a number
    has_special = False  # Flag to check if password has a special character

    # Generate password
    while not meets_criteria or len(pwd) < min_length:
        # Add a random character to the password
        new_char = random.choice(characters)
        pwd += new_char

        # Check if the new character is a number or special character
        if new_char in s2:
            has_number = True
        elif new_char in s3:
            has_special = True

        # Check if all requested criteria are met
        meets_criteria = True      
        if numbers:
            meets_criteria = has_number  # Must have a number if requested , Meets criteria becomes whatever the number is
        if special_characters:
            meets_criteria = meets_criteria and has_special  # Must have a special character if requested

    return pwd

# Function to handle password generation from GUI inputs
def generate_password_gui():      #  This function retrieves input from the GUI, validates it, and calls 
                                  # "retrieves" refers to the process of getting or extracting values from user input fields within the graphical user interface (GUI). 
# The GUI is created using Tkinter. It includes:
# An entry widget for the password length.
# Checkbuttons for including numbers and special characters.
# A button to trigger password generation.
# A label to display the generated password.

    try:
        # Get user inputs from GUI elements
        min_length = int(length_entry.get())   # This line gets the text from the length_entry Entry widget and converts it to an integer.
        has_number = numbers_var.get()        
        has_special = special_var.get()      # These lines get the boolean values (True or False) from the Checkbutton widgets.

        # Validate input
        if min_length <= 0:
            raise ValueError("Password length must be a positive number.")

        # Generate password and update result label
        pwd = generate_password(min_length, has_number, has_special)
        result_label.config(text=f"Your Password is: {pwd}")
    except ValueError as e:
        # Show error message if input is invalid
        messagebox.showerror("Input Error", str(e))

# Create main window
root = tk.Tk()
root.title("Random Password Generator")
root.geometry("300x250")

# Create and place widgets
tk.Label(root, text="Password Length:").pack(pady=5)
length_entry = tk.Entry(root)
length_entry.pack()

# Checkbox for including numbers
numbers_var = tk.BooleanVar()   # BooleanVar is a variable class in Tkinter that is specifically used to hold a boolean value (True or False).
# numbers_var = tk.BooleanVar() creates a boolean variable named numbers_var.
# This variable will be linked to a Checkbutton widget, allowing the state of the Checkbutton (checked or unchecked) to be stored in numbers_var.
tk.Checkbutton(root, text="Include Numbers", variable=numbers_var).pack()
# The variable=numbers_var parameter links the Checkbutton to the numbers_var BooleanVar.
# When the user interacts with the Checkbutton, numbers_var automatically updates to True when checked and False when unchecked.

# Checkbox for including special characters
special_var = tk.BooleanVar()
tk.Checkbutton(root, text="Include Special Characters", variable=special_var).pack()

# Button to generate password
generate_button = tk.Button(root, text="Generate Password", command=generate_password_gui)
generate_button.pack(pady=10)

# Label to display the generated password
result_label = tk.Label(root, text="", wraplength=250)
result_label.pack(pady=10)

# Start the GUI event loop
root.mainloop()
