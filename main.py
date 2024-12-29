from lager import Lager
from seeder import seed_packages
from lastbil import Lastbil

ANTAL_LASTBILAR = 10

if __name__ == "__main__":
    seed_packages(2000)
    lager_1 = Lager("lagerstatus.csv")
    lastbilar = []
    for _ in range(ANTAL_LASTBILAR):
        lastbilar.append(Lastbil())
        
    print(f"lager förtjänst: {lager_1.förtjänst}")
    print(f"lager vikt: {lager_1.vikt}kg\n")
        
    print("lastar bilarna!")
    counter = 1
    for lastbil in lastbilar:
        ny_lagerstatus, bilens_förtjänst = lastbil.lasta_bil(lager_1.lagerstatus)
        lager_1.updatera(ny_lagerstatus, bilens_förtjänst)
        print(f"Bil_{counter} färdiglastad!")
        print(f"vikt: {lastbil.vikt}kg\nförtjänst: {lastbil.förtjänst}")
        counter += 1
        
    print("\nDagen avslutad")
    print(f"Dagens förtjänst: {lager_1.dagensförtjänst}")
    print(f"Dagens straffavgift: {lager_1.straff_avgift()}")
    print(f"Antal paket kvar i lager: {lager_1.antal_paket()}")
    print(f"Förtjänst kvar i lager: {lager_1.förtjänst}")
    print(f"Dagens vinst: {lager_1.dagensförtjänst-lager_1.straff_avgift()}")