from models.office import Office


class CommercialOffice(Office):
    """
    An office contains several employees.
    An employee needs :
    1 network socket
    1 outlet
    2 phone jacks
    2 seats
    1 table
    """

    def available_space_rate(self):
        """
        :return: an integer
            a negative number if there is available space for another employee
            CommercialOffice0 if there is no more room for another employee
        """
        rate = (
                self.employees_number - self.network_socket_number +
                self.employees_number - self.outlets_number +
                2 * self.employees_number - self.phone_jacks_number +
                2 * self.employees_number - self.seats_number +
                self.employees_number - self.tables_number
        )
        return rate
