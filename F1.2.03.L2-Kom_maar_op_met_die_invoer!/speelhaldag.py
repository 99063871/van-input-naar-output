AmountPeople = int(input('Met hoeveel mensen bent u? '))
TimeGameSeat = int(input('Hoeveel minuten wilt u de game seat gebruiken (Per 5 min)? '))

PriceTicket = int(7.45)
PriceGameSeat = int(0.37) #per 5 min

TotalPrice = (AmountPeople * PriceTicket + TimeGameSeat / 5 * PriceGameSeat * AmountPeople)
TotalPrice = "{:.2f}".format(TotalPrice)
print("Dit geweldige dagje-uit met", AmountPeople, "mensen in de Speelhal met", TimeGameSeat, "minuten VR kost je maar", TotalPrice)
