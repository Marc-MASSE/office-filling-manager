class SocietyController:
    def __init__(self, society):
        self.society = society

    def calculate_commercial_employees_number(self):
        commercial_employees_number = 0
        for office in self.society.commercial_offices:
            commercial_employees_number += office.employees_number
        return commercial_employees_number

    def calculate_developer_employees_number(self):
        developer_employees_number = 0
        for office in self.society.developer_offices:
            developer_employees_number += office.employees_number
        return developer_employees_number

    def list_of_commercial_offices_available_space_rates(self):
        rates = []
        for office in self.society.commercial_offices:
            rates.append(office.available_space_rate())
        return rates

    def list_of_developer_offices_available_space_rates(self):
        rates = []
        for office in self.society.developer_offices:
            rates.append(office.available_space_rate())
        return rates

    def society_available_space_rate(self):
        """
        Add all the available space rates of the society
        :return: an integer
        """
        society_rate = 0
        for commercial_rate in self.list_of_commercial_offices_available_space_rates():
            society_rate += commercial_rate
        for developer_rate in self.list_of_developer_offices_available_space_rates():
            society_rate += developer_rate
        return society_rate

    def add_a_commercial_employee(self):
        """
        Add a commercial employee in the first commercial office available.
        :return: True if the addition was made
                 False if there is no more room to add a new employee
        """
        commercial_employee_added = False
        for office in self.society.commercial_offices:
            if office.add_an_employee():
                commercial_employee_added = True
                break
        return commercial_employee_added

    def add_a_developer_employee(self):
        """
        Add a developer employee in the first commercial office available.
        :return: True if the addition was made
                 False if there is no more room to add a new employee
        """
        developer_employee_added = False
        for office in self.society.developer_offices:
            if office.add_an_employee():
                developer_employee_added = True
                break
        return developer_employee_added
