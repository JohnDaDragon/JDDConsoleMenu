"""
Context-Aware Menu System Using JDDMenu and JDDMenuBuilder

This script provides the functionality to create dynamic, context-aware menus for console applications.
Using the JDDMenuBuilder and JDDMenu classes along with utility functions like dynamic_action_generator, 
users can build menus that adapt based on the provided context. The context is a dictionary containing 
information about the application's state, user details, or other relevant data.

Key Concepts:
- 'context': A dictionary passed to menu actions (callbacks), enabling them to behave differently based 
  on the current state or environment.
- 'JDDMenuBuilder': Used for building the menu with context-aware actions.
- 'JDDMenu': Displays the menu and handles user interaction, executing actions based on user input and context.
- 'JDDMenuUtils': Useful utility functions to help create menus

Usage of MenuUtils Features:

    1. Example usage of Dynamic Action Generator:
            
        dynamic_action = dynamic_action_generator(
        condition=lambda ctx: ctx.get('is_admin', False),
        action_if_true=admin_action,
        action_if_false=regular_user_action
        )
    
    2. Example usage of Safe Action Generator:

        def risky_action(ctx):
            # Code that may raise an exception
            ...

        # Wrapping the risky action in safe_action_generator
        safe_action = safe_action_generator(context, risky_action)
        safe_action()  # Executing the wrapped action safely



Create and Provide Context:
   user_context = {'is_admin': True}  # This would be dynamically determined by developers needs
   menu.display_menu(user_context)

This approach allows for creating menus that are not only interactive but also responsive to the current 
application state and user roles, enhancing user experience and system functionality.

"""


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
        menu = JDDMenu(menu_items, title="My Custom Menu", exit_option_text="Leave", prompt="Please choose: ")

        # Displaying the menu
        menu.display_menu()
    """

    def __init__(self, menu_options, title="Menu", exit_option_text="Exit", prompt="Select an option: ", cont=False):
        """
        Initializes a new instance of JDDMenu.
        """
        self.menu_options = menu_options
        self.title = title
        self.exit_option_text = exit_option_text
        self.prompt = prompt
        self.cont = cont


    def display_menu(self, context=None):
        """
        Displays the menu and handles user input to execute corresponding actions.
        """
        while True:
            print(self.title)
            print('-' * len(self.title))  # Simple underline for the title

            for index, (option_text, _) in enumerate(self.menu_options, start=1):
                print(f"Enter {index} to {option_text}")
            
            print(f"Enter 0 to {self.exit_option_text}")

            try:
                choice = int(input(self.prompt))
                if choice < 0 or choice > len(self.menu_options):
                    raise ValueError("Selection out of range")

                if choice == 0:
                    print("Exiting menu.")
                    break

                _, action = self.menu_options[choice - 1]
                action(context)
                if self.cont:
                    self.continue_choice()

            except ValueError as e:
                print(f"Invalid selection: {e}. Please try again.")

    

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


class JDDMenuBuilder:
    """
    A builder class for creating instances of the JDDMenu class.

    The JDDMenuBuilder facilitates the construction of a JDDMenu object by providing
    a fluent interface to add menu options and their associated actions. This approach
    allows for more readable and maintainable code when setting up complex menus.

    Important concepts to note when using:
        - Dynamic Actions: Allows creating actions that adapt based on the application's context using the `dynamic_action_generator`.
        - Parameterized Callbacks: Supports actions that accept additional parameters for enhanced flexibility.

    Attributes:
        menu_options (list of tuples): An internal list that stores the menu options 
                                       and their corresponding actions. Each tuple in
                                       this list contains a string (the text of the 
                                       menu option) and a callable (the action to be 
                                       executed when the option is selected).

    Methods:
        add_option(option_text, action):Adds a menu option to the internal list. Allows
                                        chaining for adding multiple options in a fluent manner.
        build(): Finalizes the construction of the JDDMenu object and returns it.

    Usage example:
        # Define actions for the menu
        def action1():
            print("Action 1 executed.")

        def action2():
            print("Action 2 executed.")

        # Creating a menu using the builder
        builder = JDDMenuBuilder()
        menu = builder.build()
        menu.display_menu()
    
    Example code for Adding to Menu
        
        builder.set_title("My Custom Menu")
        builder.set_exit_option_text("Leave")
        builder.set_prompt("Please choose: ")
        builder.add_option("Option 1", sample_action)
        builder.add_option("Option 2", sample_action)
        builder.add_option("Option 1", action1).add_option("Option 2", action2)
        builder.add_option("Parameterized Action", lambda ctx: action_with_params(ctx, "param1", "param2"))
        builder.add_option("Safe Action", lambda ctx: safe_action(ctx))
        builder.add_option("Dynamic Action", dynamic_action)
    """

    def __init__(self):
        """
        Initializes a new instance of JDDMenuBuilder.

        This builder is used for constructing a JDDMenu instance with customizable options,
        title, exit option text, and prompt. It starts with an empty list of menu options
        and default values for title, exit option text, and prompt.
        """
        self.menu_options = []
        self.title = "Menu"
        self.exit_option_text = "Exit"
        self.prompt = "Select an option: "

    def add_option(self, option_text, action):
        """
        Adds a menu option along with its corresponding action to the builder.

        Parameters:
        option_text (str): The text displayed for the menu option.
        action (callable): The action (function) to execute when this menu option is selected.

        Returns:
        JDDMenuBuilder: The instance of the builder to allow for method chaining.
        """
        # Error Prevention 
        if not callable(action):
            raise ValueError("The provided action is not callable")
        
        self.menu_options.append((option_text, action))
        return self

    def set_title(self, title):
        """
        Sets the title for the menu.

        Parameters:
        title (str): The title text to be displayed at the top of the menu.

        Returns:
        JDDMenuBuilder: The instance of the builder to allow for method chaining.
        """
        self.title = title
        return self

    def set_exit_option_text(self, text):
        """
        Sets the text for the exit option in the menu.

        Parameters:
        text (str): The text for the exit option in the menu.

        Returns:
        JDDMenuBuilder: The instance of the builder to allow for method chaining.
        """
        self.exit_option_text = text
        return self

    def set_prompt(self, prompt):
        """
        Sets the prompt text that is displayed when asking the user for input.

        Parameters:
        prompt (str): The prompt text to be displayed to the user.

        Returns:
        JDDMenuBuilder: The instance of the builder to allow for method chaining.
        """
        self.prompt = prompt
        return self

    def build(self):
        """
        Constructs and returns a JDDMenu object with the configured options, title, exit text, and prompt.

        Returns:
        JDDMenu: The constructed JDDMenu object with the specified settings.
        """
        return JDDMenu(self.menu_options, self.title, self.exit_option_text, self.prompt)


class JDDMenuUtils:
    """
    A utility class for the JDDMenu system, providing various helper methods to enhance menu functionality.

    JDDMenuUtils includes static methods that aid in creating and managing dynamic menu options and actions.
    These utilities are designed to offer additional flexibility and robust error handling for menu items,
    making it easier to create complex, context-aware, and error-resilient menu systems.

    The class includes methods for generating actions based on certain conditions and safely executing actions 
    with error handling. It serves as a toolkit to augment the capabilities of the JDDMenu and 
    JDDMenuBuilder classes, ensuring that menus can be both versatile and reliable.

    Methods:
    dynamic_action_generator(condition, action_if_true, action_if_false): Creates a dynamic action based
        on a provided condition, allowing different actions to be executed depending on the evaluation of
        the condition within the provided context.
    safe_action_generator(context, action): Wraps a given action in error handling logic to manage and log
        exceptions that occur during action execution, enhancing the stability of the menu system.

    Note: This class is intended to be used in conjunction with JDDMenu and JDDMenuBuilder for building
    dynamic and robust menu systems in console applications.
    """
    @staticmethod
    def dynamic_action_generator(condition, action_if_true, action_if_false):
        """
        Generates a dynamic action based on a given condition.

        Parameters:
        condition (callable): A function that takes context as an argument and returns a boolean.
        action_if_true (callable): The action to execute if the condition evaluates to True.
        action_if_false (callable): The action to execute if the condition evaluates to False.

        Returns:
        callable: A lambda function that executes the appropriate action based on the condition.
        """
        # Error Prevention
        if not callable(action_if_true) or not callable(action_if_false):
            raise ValueError("Provided actions must be callable")
        
        return lambda context: action_if_true(context) if condition(context) else action_if_false(context)

    @staticmethod
    def safe_action_generator(context, action_that_could_fail):
        """
        Wraps a given action in a safety layer to handle exceptions during its execution.

        This generator function is designed to enhance the reliability of actions used in the menu system. 
        It takes an action, a callable that performs a specific task, and wraps it in error-handling logic. 
        If an exception is raised while executing the action, it is caught, and a user-friendly message 
        is displayed. This approach ensures that the application remains stable and responsive even in 
        the face of unexpected errors.

        Parameters:
        context (dict): discussed within the module level docstring
        action_that_could_fail (callable): A callable object (function or lambda) that performs an action 
                                           and may raise exceptions during its execution.

        Returns:
        function: A lambda function that, when called, executes the provided action within a protected block. 
                  It captures and handles any exceptions, printing an error message and preventing application crashes.

        Note: This utility is particularly useful for actions within a menu system where stability and 
        error feedback are crucial for a good user experience.
        """
        # Error Prevention
        if not callable(action_that_could_fail):
            raise ValueError("Provided actions must be callable")
        
        try:
            action_that_could_fail(context)

        except Exception as e:
            print(f"An error occurred: {e}")

    # Future utility methods can be added here...