# feestlunch

txt = "De feestlunch kost je bij de bakker"
txt2 = "euro voor de" 
txt3 = "croissantjes en de"
txt4 = "stokbroden als de"
txt5 = "kortingsbonnen nog geldig zijn!"

AantalCroissantjes = 17
CroissantPrijs = 0.39

AantalStokbroden = 2
StokbroodPrijs = 2.78

AantalKortingsbonnen = 3 
KortingsbonWaarde = 0.50 

totaal = AantalCroissantjes * CroissantPrijs + AantalStokbroden * StokbroodPrijs - AantalKortingsbonnen * KortingsbonWaarde

print(txt, totaal, txt2, AantalCroissantjes, txt3, AantalStokbroden, txt4, AantalKortingsbonnen, txt5)
