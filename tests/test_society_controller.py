import unittest

from constants.data_for_tests import SOCIETY_TEST
from controllers.society_controller import SocietyController
from models.commercial_office import CommercialOffice
from models.developer_office import DeveloperOffice
from models.society import Society


class TestSocietyController(unittest.TestCase):
    def test_calculate_commercial_employees_number(self):
        sut = SocietyController(SOCIETY_TEST)
        # 5 = 2 employees in COMMERCIAL_OFFICE_TEST1 + 3 employees in COMMERCIAL_OFFICE_TEST1
        expected_value = 5
        self.assertEquals(sut.calculate_commercial_employees_number(), expected_value)

    def test_calculate_developer_employees_number(self):
        sut = SocietyController(SOCIETY_TEST)
        # 5 = 2 employees in DEVELOPER_OFFICE_TEST1 + 3 employees in DEVELOPER_OFFICE_TEST1
        expected_value = 5
        self.assertEquals(sut.calculate_developer_employees_number(), expected_value)

    def test_list_of_commercial_offices_available_space_rates(self):
        sut = SocietyController(SOCIETY_TEST)
        expected_value = [-7, 0]
        self.assertEquals(sut.list_of_commercial_offices_available_space_rates(), expected_value)

    def test_list_of_developer_offices_available_space_rates(self):
        sut = SocietyController(SOCIETY_TEST)
        expected_value = [-10, 0]
        self.assertEquals(sut.list_of_developer_offices_available_space_rates(), expected_value)

    def test_society_available_space_rate(self):
        sut = SocietyController(SOCIETY_TEST)
        # -17 = (-7) + 0 + (-10) + 0
        expected_value = -17
        self.assertEquals(sut.society_available_space_rate(), expected_value)

    def test_add_a_commercial_employee_should_return_false(self):
        society = Society()
        commercial_office1 = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=3
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
        self.assertFalse(sut.add_a_commercial_employee())

    def test_add_a_commercial_employee_should_return_true(self):
        society = Society()
        commercial_office1 = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=3
        )
        commercial_office2 = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=2
        )
        society.commercial_offices = [commercial_office1, commercial_office2]
        sut = SocietyController(society)
        self.assertTrue(sut.add_a_commercial_employee())

    def test_add_a_developer_employee_should_return_false(self):
        society = Society()
        developer_office1 = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=3
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
        self.assertFalse(sut.add_a_developer_employee())

    def test_add_a_developer_employee_should_return_true(self):
        society = Society()
        developer_office1 = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=3
        )
        developer_office2 = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=2
        )
        society.developer_offices = [developer_office1, developer_office2]
        sut = SocietyController(society)
        self.assertTrue(sut.add_a_developer_employee())


if __name__ == '__main__':
    unittest.main()
