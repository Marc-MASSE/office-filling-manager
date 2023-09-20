from math import ceil

from models.office import Office


class DeveloperOffice(Office):
    """
    An office contains several employees.
    An employee needs :
    3 network sockets
    3 outlets
    1 phone jack
    1.5 seats
    1 table
    """

    def available_space_rate(self):
        """
        :return: an integer
            a negative number if there is available space for another employee
            0 if there is no more room for another employee
        """
        rate = (
                3 * self.employees_number - self.network_socket_number +
                3 * self.employees_number - self.outlets_number +
                self.employees_number - self.phone_jacks_number +
                ceil(1.5 * self.employees_number) - self.seats_number +
                self.employees_number - self.tables_number
        )
        return int(rate)
