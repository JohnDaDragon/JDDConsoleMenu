# Define the class JDDMenu
class JDDMenu:
    # This is the constructor method for the class. It's called when you create a new instance of JDDMenu.
    def __init__(self, menu_options):
        """
        Initializes the JDDMenu with a list of menu options and their corresponding actions.

        Parameters:
        menu_options (list of tuples): A list where each tuple contains a string (menu option text)
                                       and a function (the action to be executed when the option is selected).
        """
        # This line assigns the provided menu_options to an attribute of the class. 
        # Now, this attribute can be used in other methods of the class.
        self.menu_options = menu_options

    # This method is responsible for displaying the menu and processing user inputs.
    def display_menu(self):
        """
        Displays the menu and handles user input to execute corresponding actions.
        """
        # Infinite loop to keep showing the menu until we break out of it (not implemented here).
        while True:
            # This loop displays each menu option. 
            # 'enumerate' is used to get both the index and the value from the menu_options list.
            for index, (option_text, _) in enumerate(self.menu_options, start=1):
                # Print each menu option with its index. 
                print(f"{index}. {option_text}")

            try:
                # Asking the user to select an option. We expect a number as input.
                choice = int(input("Please select an option: "))
                # Fetch the action (function) corresponding to the user's choice.
                _, action = self.menu_options[choice - 1]

                # Execute the action.
                action()

            except (ValueError, IndexError):
                # If the user inputs an invalid option or if there's a conversion error, 
                # this block will execute, informing the user of an invalid selection.
                print("Invalid selection. Please try again.")

            # Note: There's no current way to exit this while loop. 
            # You might want to implement an 'exit' option.

# A sample function to be used as an action for the menu.
def sample_action():
    print("Sample action executed.")

# Example usage of the JDDMenu class.
menu_items = [
    # This list contains tuples with menu option text and corresponding actions (functions).
    ("Option 1", sample_action),
    ("Option 2", sample_action)  # Here, both options use the same function, but they can be different.
]

# Creating an instance of JDDMenu with the menu_items.
menu = JDDMenu(menu_items)
# Calling the display_menu method to show the menu and process user input.
menu.display_menu()
