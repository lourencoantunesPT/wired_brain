################################################
#
#  testar o modulo airtravel
################################################

import airtravel
from airtravel import Flight, Aircraft

f = Flight("BA758", Aircraft("L-345-1", "airbus A319", 22, 6))
f.allocate_seat("12A", "Manel dos anzois")
# f.allocate_seat("12A","Maria antonieta")
f.allocate_seat("15F", "Hanz dos algarves")
f.allocate_seat("15E", "Antonio SImoes")
# f.allocate_seat("E27","Yukuriri")
f.allocate_seat("1C", "John Major")
f.allocate_seat("1D", "Richard")
# f.allocate_seat("DD","Larry Page")

f.relocate_passageiro("12A", "15D")
print(f.num_available_seats())

print(f.number())
print(f.aircraft_model())

from pprint import pprint

pprint(f._seating)
print(f.num_available_seats())
