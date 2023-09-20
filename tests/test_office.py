import unittest

from models.office import Office


class TestOffice(unittest.TestCase):
    def test_add_an_employee_should_be_possible(self):
        sut = Office(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=3,
            seats_number=3,
            tables_number=3,
            employees_number=2
        )
        expected_value = 3
        self.assertTrue(sut.add_an_employee())
        self.assertEquals(sut.employees_number, expected_value)

    def test_add_an_employee_should_not_be_possible(self):
        sut = Office(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=3,
            seats_number=3,
            tables_number=3,
            employees_number=3
        )
        expected_value = 3
        self.assertFalse(sut.add_an_employee())
        self.assertEquals(sut.employees_number, expected_value)

    def test_available_space_rate_should_be_negative(self):
        sut = Office(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=3,
            seats_number=3,
            tables_number=3,
            employees_number=2
        )
        expected_value = -5
        self.assertEquals(sut.available_space_rate(), expected_value)

    def test_available_space_rate_should_be_0(self):
        sut = Office(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=3,
            seats_number=3,
            tables_number=3,
            employees_number=3
        )
        expected_value = 0
        self.assertEquals(sut.available_space_rate(), expected_value)


if __name__ == '__main__':
    unittest.main()
