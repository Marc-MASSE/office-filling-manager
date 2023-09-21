import random

from constants.data_for_initialisation import SOCIETY
from controllers.society_controller import SocietyController
from views.display_manager import DisplayManager


if __name__ == '__main__':
    print('Office filling manager')

    # Initialisation of society data
    society_controller = SocietyController(SOCIETY)
    display_manager = DisplayManager(society_controller)

    # First society display
    display_manager.display_society_information()

    while society_controller.society_available_space_rate() < 0:
        display_manager.display_message("Hire a new employee.")

        # Hire a new employee : 0 means a commercial, 1 means a developer
        new_employee_type = random.randint(0, 1)
        input()

        if new_employee_type == 0:
            display_manager.display_message("Add a new commercial employee.")
            if society_controller.add_a_commercial_employee():
                display_manager.display_society_information()
            else:
                display_manager.display_message("There is no more space for another commercial employee.")
        else:
            display_manager.display_message("Add a new developer employee.")
            if society_controller.add_a_developer_employee():
                display_manager.display_society_information()
            else:
                display_manager.display_message("There is no more space for another developer employee.")

    display_manager.display_message("There is no more room for any employee.")
