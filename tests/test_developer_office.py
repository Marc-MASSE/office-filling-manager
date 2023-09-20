import unittest

from models.developer_office import DeveloperOffice


class TestDeveloperOffice(unittest.TestCase):
    def test_available_space_rate_should_be_negative(self):
        sut = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=2
        )
        expected_value = -10
        self.assertEquals(sut.available_space_rate(), expected_value)

    def test_available_space_rate_should_be_0(self):
        sut = DeveloperOffice(
            network_socket_number=9,
            outlets_number=9,
            phone_jacks_number=3,
            seats_number=5,
            tables_number=3,
            employees_number=3
        )
        expected_value = 0
        self.assertEquals(sut.available_space_rate(), expected_value)


if __name__ == '__main__':
    unittest.main()
