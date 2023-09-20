import unittest

from controllers.society_controller import SocietyController
from models.commercial_office import CommercialOffice
from models.developer_office import DeveloperOffice
from models.society import Society


class TestSocietyController(unittest.TestCase):
    def test_calculate_commercial_employees_number(self):
        society = Society()
        commercial_office1 = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=2
        )
        commercial_office2 = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=3
        )
        society.commercial_offices = [commercial_office1, commercial_office2]
        sut = SocietyController(society)
        expected_value = 5
        self.assertEquals(sut.calculate_commercial_employees_number(), expected_value)

    def test_calculate_developer_employees_number(self):
        society = Society()
        developer_office1 = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=2
        )
        developer_office2 = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=3
        )
        society.developer_offices = [developer_office1, developer_office2]
        sut = SocietyController(society)
        expected_value = 5
        self.assertEquals(sut.calculate_developer_employees_number(), expected_value)


if __name__ == '__main__':
    unittest.main()
