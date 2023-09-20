class Society:
    """
    A society contains :
    0 or several commercial offices
    0 or several developer offices
    """
    def __init__(self):
        self.commercial_offices = []
        self.developer_offices = []

    def add_a_commercial_office(self,commercial_office):
        self.commercial_offices.append(commercial_office)

    def add_a_developer_office(self, developer_office):
        self.developer_offices.append(developer_office)
