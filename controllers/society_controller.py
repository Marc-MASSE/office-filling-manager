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
        society_rate = 0
        for commercial_rate in self.list_of_commercial_offices_available_space_rates():
            society_rate += commercial_rate
        for developer_rate in self.list_of_developer_offices_available_space_rates():
            society_rate += developer_rate
        return society_rate

    def add_a_commercial_employee(self):
        commercial_employee_added = False
        for office in self.society.commercial_offices:
            if office.add_an_employee():
                commercial_employee_added = True
                break
        return commercial_employee_added

    def add_a_developer_employee(self):
        developer_employee_added = False
        for office in self.society.developer_offices:
            if office.add_an_employee():
                developer_employee_added = True
                break
        return developer_employee_added
