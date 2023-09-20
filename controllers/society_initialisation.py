from constants.datas_for_initialisation import COMMERCIAL_OFFICES, DEVELOPER_OFFICES
from models.society import Society


class SocietyInitialisation:
    def __init__(self):
        self.society = None

    def initialisation(self):
        self.society = Society()
        self.society.commercial_offices = COMMERCIAL_OFFICES
        self.society.developer_offices = DEVELOPER_OFFICES
        return self.society


