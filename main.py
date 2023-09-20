# This is a sample Python script.
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
    society_available_space_rate = society_controller.society_available_space_rate()
    display_manager.display_society_information()

    """
    while society_available_space_rate < 0:
    """
    society_controller.add_a_commercial_employee()
    display_manager.display_society_information()

    society_controller.add_a_developer_employee()
    display_manager.display_society_information()
