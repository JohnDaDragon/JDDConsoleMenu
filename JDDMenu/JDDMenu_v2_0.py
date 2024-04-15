class JDDMenu:
    """
    A class that represents a customizable menu system for console applications.

    The JDDMenu class provides a way to create interactive, text-based menus in the console.
    It allows for the addition of multiple menu options, each associated with a specific action
    (a function or a method). When a user selects an option, the corresponding action is executed.

    Attributes:
        menu_options (list of tuples): A list where each tuple contains a string (the menu option's
                                       text) and a callable (the action to be executed when the option
                                       is selected). The menu options are set during the initialization
                                       of the class and determine the behavior of the menu.

    Methods:
        display_menu(): Displays the menu options in the console and waits for the user's input.
                        Executes the action associated with the chosen option. The method handles
                        user input errors and allows for continuous operation until an exit condition
                        is met (like selecting an 'exit' option).

    Usage example:
        # Creating menu options and actions
        def sample_action():
            print("Action executed.")

        # Creating a JDDMenu instance
        menu_items = [("Option 1", sample_action), ("Option 2", sample_action)]
        menu = JDDMenu(menu_items)

        # Displaying the menu
        menu.display_menu()
    """
    def __init__(self, menu_options):
        """
        Initializes the JDDMenu with a list of menu options and their corresponding actions.

        Parameters:
        menu_options (list of tuples): A list where each tuple contains a string (menu option text)
        and a function (the action to be executed when the option is selected).
        """
        self.menu_options = menu_options

    def display_menu(self):
        """
        Displays the menu and handles user input to execute corresponding actions.
        """
        while True:
            # Displaying menu options
            for index, (option_text, _) in enumerate(self.menu_options, start=1):
                print(f"Enter {index} to {option_text}")

            print("Enter 0 to Quit")

            try:
                # Getting user's choice
                choice = int(input("Please select an option: "))

                if choice == 0:
                    print("Exiting menu.")
                    break

                _, action = self.menu_options[choice - 1]

                # Execute the corresponding action
                action()
                self.continue_choice()

            except (ValueError, IndexError):
                print("Invalid selection. Please try again.")
    
    def continue_choice(self):
        """
        Prompts the user to either continue using the application or exit.
        """
        while True:
            try:
                continue_choice = input("Do you want to continue? (yes/no): ").lower()
                if continue_choice in ['yes', 'y']:
                    break  # Breaks out of the continue_choice loop and goes back to the main menu
                elif continue_choice in ['no', 'n']:
                    print("Exiting menu.")
                    exit()  # Exits the program
                else:
                    raise ValueError
            except ValueError:
                print("Invalid input. Please answer with 'yes' or 'no'.")