################################################
#
#  testar o modulo airtravel

################################################

import airtravel
from airtravel import Flight, Aircraft
import pprint
from pprint import pprint

""" modulo para testar classes Flight e Aircraft assim 
como a funcao console_card_printer() do modulo airtravel """


print ("################ TESTES DE RESERVAS")

print("Criacao do Voo L-345-1 \n")
f = Flight("BA758", Aircraft("L-345-1", "airbus A319", 22, 6))

print(" Reservas dos lugares 12A, 15F, 15E, 1C e 1D \n")
f.allocate_seat("12A", "Manel dos anzois")
# f.allocate_seat("12A","Maria antonieta")
f.allocate_seat("15F", "Hanz dos algarves")
f.allocate_seat("15E", "Antonio SImoes")
# f.allocate_seat("E27","Yukuriri")
f.allocate_seat("1C", "John Major")
f.allocate_seat("1D", "Richard")
# f.allocate_seat("DD","Larry Page")
pprint(f._seating)

print ("################ TESTES DE ALTERACAO DE RESERVAS")
print ("mudança de lugar do 12A para o 15D \n")
f.relocate_passageiro("12A", "15D")
pprint(f._seating)


print ("################ LUGARES DISPONIVEIS POR VOO")
print(f.number())
print(f.aircraft_model())
pprint(f._seating)
print(f.num_available_seats())


print ("################ IMPRESSO DOS CARTOS DE EMBARQUE DE UM VOO")
#f.make_boarding_cards(airtravel.console_card_printer())

