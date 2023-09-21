class DisplayManager:
    def __init__(self, society_controller):
        self.society_controller = society_controller

    def display_employees_number(self):
        print("--------------------------------------------")
        print(f"There are {self.society_controller.calculate_commercial_employees_number()} commercial employees.")
        print(f"There are {self.society_controller.calculate_developer_employees_number()} developer employees.")

    def display_offices_available_space_rate(self):
        print("--------------------------------------------")

        print("Commercial offices available space rates :")
        commercial_rates = self.society_controller.list_of_commercial_offices_available_space_rates()
        commercial_index = 1
        for commercial_rate in commercial_rates:
            print(f"- Office n°{commercial_index} : rate = {commercial_rate}")
            commercial_index += 1

        print("Developer offices available space rates :")
        developer_rates = self.society_controller.list_of_developer_offices_available_space_rates()
        developer_index = 1
        for developer_rate in developer_rates:
            print(f"- Office n°{developer_index} : rate = {developer_rate}")
            developer_index += 1

    def display_society_available_space_rate(self):
        print("--------------------------------------------")
        print(f"Society available space rate = {self.society_controller.society_available_space_rate()}")

    def display_society_information(self):
        print("++++++++++++++++++++++++++++++++++++++++++++")
        print("Society information")
        self.display_employees_number()
        self.display_offices_available_space_rate()
        self.display_society_available_space_rate()

    def display_message(self, message: str = ""):
        print("--------------------------------------------")
        print(message)
