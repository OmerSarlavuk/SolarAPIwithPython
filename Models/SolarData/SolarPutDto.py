class SolarPutDto:
    def __init__(self, id:int, cityName: str, year: int, month: str, radiation: float):
        self.id = id
        self.cityName = cityName
        self.year = year
        self.month = month
        self.radiation = radiation
        