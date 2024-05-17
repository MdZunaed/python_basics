class Vehicle:
    def __init__(self, company, model, year):
        self.company = company
        self.model = model
        self.year = year

zunaedsCar = Vehicle(company='Mitshbishi', model='Lancer Evo x', year=2012)

zubaersBike = Vehicle(company= 'Apache', model='4v', year='2022')

print(zunaedsCar.company)
print(zubaersBike.model)