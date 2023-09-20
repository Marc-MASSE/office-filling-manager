import unittest

from models.commercial_office import CommercialOffice


class TestCommercialOffice(unittest.TestCase):
    def test_available_space_rate_should_be_negative(self):
        sut = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=2
        )
        expected_value = -7
        self.assertEquals(sut.available_space_rate(), expected_value)

    def test_available_space_rate_should_be_0(self):
        sut = CommercialOffice(
            network_socket_number=3,
            outlets_number=3,
            phone_jacks_number=6,
            seats_number=6,
            tables_number=3,
            employees_number=3
        )
        expected_value = 0
        self.assertEquals(sut.available_space_rate(), expected_value)


if __name__ == '__main__':
    unittest.main()
