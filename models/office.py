class Office:
    """
    An office contains several employees.
    An employee needs :
    1 network socket
    1 outlet
    1 phone jack
    1 seat
    1 table
    """

    def __init__(
            self,
            network_socket_number=0,
            outlets_number=0,
            phone_jacks_number=0,
            seats_number=0,
            tables_number=0,
            employees_number=0
    ):
        self.network_socket_number = network_socket_number
        self.outlets_number = outlets_number
        self.phone_jacks_number = phone_jacks_number
        self.seats_number = seats_number
        self.tables_number = tables_number
        self.employees_number = employees_number

    def add_an_employee(self):
        """
        :return: True if there is a space for another employee
                 False if there is no space for another employee
        """
        employee_added = False
        if self.available_space_rate() < 0:
            self.employees_number += 1
            employee_added = True
        return employee_added

    def available_space_rate(self):
        """
        :return: an integer
            a negative number if there is available space for another employee
            0 if there is no more room for another employee
        """
        rate = (
                self.employees_number - self.network_socket_number +
                self.employees_number - self.outlets_number +
                self.employees_number - self.phone_jacks_number +
                self.employees_number - self.seats_number +
                self.employees_number - self.tables_number
        )
        return rate
