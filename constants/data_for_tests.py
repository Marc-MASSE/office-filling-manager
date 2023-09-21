from models.commercial_office import CommercialOffice
from models.developer_office import DeveloperOffice
from models.office import Office
from models.society import Society

COMMERCIAL_OFFICE_TEST1 = CommercialOffice(
    network_socket_number=3,
    outlets_number=3,
    phone_jacks_number=6,
    seats_number=6,
    tables_number=3,
    employees_number=2
)
COMMERCIAL_OFFICE_TEST2 = CommercialOffice(
    network_socket_number=3,
    outlets_number=3,
    phone_jacks_number=6,
    seats_number=6,
    tables_number=3,
    employees_number=3
)
DEVELOPER_OFFICE_TEST1 = DeveloperOffice(
    network_socket_number=9,
    outlets_number=9,
    phone_jacks_number=3,
    seats_number=5,
    tables_number=3,
    employees_number=2
)
DEVELOPER_OFFICE_TEST2 = DeveloperOffice(
    network_socket_number=9,
    outlets_number=9,
    phone_jacks_number=3,
    seats_number=5,
    tables_number=3,
    employees_number=3
)
SOCIETY_TEST = Society()
SOCIETY_TEST.add_a_commercial_office(COMMERCIAL_OFFICE_TEST1)
SOCIETY_TEST.add_a_commercial_office(COMMERCIAL_OFFICE_TEST2)
SOCIETY_TEST.add_a_developer_office(DEVELOPER_OFFICE_TEST1)
SOCIETY_TEST.add_a_developer_office(DEVELOPER_OFFICE_TEST2)
