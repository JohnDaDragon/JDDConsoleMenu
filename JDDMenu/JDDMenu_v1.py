class jdd_menu():
    """
        The `jdd_menu` class provides a customizable menu system for console applications. 

        It is designed for ease of use and flexibility, allowing the user to define menu options 
        and corresponding actions. The class can be easily adapted for various projects 
        by modifying the menu options and associated functionality.
    """


    def menu():
        """
            Displays a menu to the user and handles their input.

            This method prints a series of options to the console, and awaits the user's choice.
            Each option corresponds to a specific action or function in the application.
            The user's choice is then used to execute the appropriate action.

            Modifications needed for reuse:
            - Update printed menu options to reflect new choices.
            - Adjust the `choiceList` to match the number of new options.
            - Modify or add `elif` statements to handle new options.

            Returns:
            None
        """

        # Give the user information on what he would like to do and how to select it. 
        #TODO Change depeending on what the options are.
        print("     ----Main Menu----")
        print("Enter x to y") 
        print("Enter 0 to Quit")

        # Initial choice to see what user wants to do
        choice = str(input("Select an option to proceed: "))

        # This is the first if, so that subsequent copy and paste can all be elif for ease of use,can be used to bugtest continue function
        if choice == 'test':
            jdd_menu.continue_choice()
        
        #TODO Copy and paste this for however many choices you need  
        elif choice == 'n':
            # Enter the function that you would like to be the n'th option in the menu here
            jdd_menu.continue_choice()

        elif choice == '0':
            print('Thanks for using my Script!')
            exit()

        # Used to let user try again if input is not a valid choice
        else:
            print("Invalid Input, please try again")
            jdd_menu.menu()


    def continue_choice():     
        """
            Offers the user a choice to continue using the application or exit.

            This method is typically called after executing an action from the menu.
            It prompts the user to either return to the main menu for further actions
            or to quit the application.

            Returns:
            None
        """ 

        # Prompts user to decide to either continue using script or finish.
        cont = input('Would you like to Return to Main Menu? (y/n):')
        
        # Runs the menu function to return user to main menu
        if cont == 'y':
            jdd_menu.menu()
            
        # Ends the script as the user has specified they're finished using the script
        elif cont == 'n':
            print('Thanks for using my script!')
            exit()
            
        # Error for inputs outside of expected values, runs function again
        else:
            print('Invalid Imput, please enter y or n')
            jdd_menu.continue_choice()


# Driver of the script
def main():
    jdd_menu.menu()


if __name__ == '__main__':
    main()