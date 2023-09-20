import random

from controllers.society_controller import SocietyController
from controllers.society_initialisation import SocietyInitialisation
from views.display_manager import DisplayManager

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


if __name__ == '__main__':
    print('Office filling manager')

    # Initialisation of society data
    society_initializer = SocietyInitialisation()
    society = society_initializer.initialisation()
    society_controller = SocietyController(society)
    display_manager = DisplayManager(society_controller)

    # First society display
    display_manager.display_society_information()

    while society_controller.society_available_space_rate() < 0:
        print("--------------------------------------------")
        print("Hire a new employee.")
        # Hire a new employee : 0 means a commercial, 1 means a developer
        new_employee_type = random.randint(0, 1)
        input()

        if new_employee_type == 0:
            print("--------------------------------------------")
            print("Add a new commercial employee.")
            if society_controller.add_a_commercial_employee():
                display_manager.display_society_information()
            else:
                print("--------------------------------------------")
                print("There is no more space for another commercial employee.")
        else:
            print("--------------------------------------------")
            print("Add a new developer employee.")
            if society_controller.add_a_developer_employee():
                display_manager.display_society_information()
            else:
                print("--------------------------------------------")
                print("There is no more space for another developer employee.")

    print("There is no more room for any employee.")
