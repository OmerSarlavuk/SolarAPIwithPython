class SolarDataPostDto:
    def __init__(self, cityName: str, year: int, month: str, radiation: float):
        self.cityName = cityName
        self.year = year
        self.month = month
        self.radiation = radiation