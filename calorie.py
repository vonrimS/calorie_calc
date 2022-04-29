from temperature import Temperature

class Calorie:
    """
    Represent amount of calories calculated for today with formula
    BMR = 10*weight + 6.25*height - 5*age + 5 - 10*temperature
    """
    def __init__(self, weight, height, age, temperature):
        self.height = height
        self.weight = weight
        self.age = age
        self.temperature = temperature

    def calculate(self):
        result = 10 * self.weight + 6.25 * self.height - 5 * self.age + 5 - 10 * self.temperature
        return result

if __name__ == '__main__':
    temperature = Temperature(city="new-york", country='usa').get()
    calorie = Calorie(weight=75, height=169, age=36, temperature=16)
    print(calorie.calculate())