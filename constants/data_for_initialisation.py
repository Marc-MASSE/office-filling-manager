from models.commercial_office import CommercialOffice
from models.developer_office import DeveloperOffice
from models.society import Society

COMMERCIAL_OFFICE1 = CommercialOffice(
    network_socket_number=6,
    outlets_number=6,
    phone_jacks_number=12,
    seats_number=12,
    tables_number=6,
    employees_number=2
)

COMMERCIAL_OFFICE2 = CommercialOffice(
    network_socket_number=4,
    outlets_number=4,
    phone_jacks_number=8,
    seats_number=8,
    tables_number=4,
    employees_number=2
)
COMMERCIAL_OFFICE3 = CommercialOffice(
    network_socket_number=3,
    outlets_number=3,
    phone_jacks_number=6,
    seats_number=6,
    tables_number=3,
    employees_number=2
)
DEVELOPER_OFFICE1 = DeveloperOffice(
    network_socket_number=15,
    outlets_number=15,
    phone_jacks_number=5,
    seats_number=8,
    tables_number=5,
    employees_number=2
)
DEVELOPER_OFFICE2 = DeveloperOffice(
    network_socket_number=12,
    outlets_number=12,
    phone_jacks_number=4,
    seats_number=6,
    tables_number=4,
    employees_number=2
)
SOCIETY = Society()
SOCIETY.add_a_commercial_office(COMMERCIAL_OFFICE1)
SOCIETY.add_a_commercial_office(COMMERCIAL_OFFICE2)
SOCIETY.add_a_commercial_office(COMMERCIAL_OFFICE3)
SOCIETY.add_a_developer_office(DEVELOPER_OFFICE1)
SOCIETY.add_a_developer_office(DEVELOPER_OFFICE2)

