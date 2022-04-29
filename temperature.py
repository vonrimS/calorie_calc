class Temperature:
    """
    Temperature scraped from weather webapp timeanddate.com/weather
    based on city and country user input
    """
    def __init__(self,country, city):
        self.city = city
        self.country = country

    def get(self):
        pass