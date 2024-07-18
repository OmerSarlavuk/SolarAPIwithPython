class CitiesCoordinatePutDto:
    def __init__(self,id: int, name: str, latitude: float, longitude: float):
        self.id = id
        self.name = name
        self.latitude = latitude
        self.longitude = longitude