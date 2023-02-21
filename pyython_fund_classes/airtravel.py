""" Exemplo para estudar classes e objetcs em Python """


class Flight:
    """ esta classe é oara voos """

    def __init__(self, number, aircraft):
        if not number[:2].isalpha():
            raise ValueError(f"Nao pode haver codigos de cmpoanhia com  '{number[:2]}'")
        if not number[:2].isupper():
            raise ValueError(f"Codigo de voo invalido ' {number[:2]}'")
        if not (number[2:].isdigit() and int(number[2:]) <= 9999):
            raise ValueError(f"o numero de rota é invalido {number[2:]}'")
        self._number = number
        self._aircraft = aircraft
        rows, seats = self._aircraft.seating_plan()
        self._seating = [None] + [{letter: None for letter in seats} for _ in rows]

    def aircraft_model(self):
        return self._aircraft.model()

    def number(self):
        return self._number

    def airline(self):
        return self._number[:2]

    def allocate_seat(self, seat, passageiro):
        """ serve para alocar um passageiro a um lugar"""

        letter, row = self._parse_seat(seat)

        if self._seating[row][letter] is not None:
            raise ValueError(f"Seat {seat} already occupied")

        self._seating[row][letter] = passageiro




    def _parse_seat(self, seat):
        rows, seat_letters = self._aircraft.seating_plan()
        letter = seat[-1]
        if letter not in seat_letters:
            raise ValueError(f"lugar invalido - letra invalida {letter}")
        row_text = seat[:-1]
        try:
            row = int(row_text)
        except ValueError:
            raise ValueError(f"Invalid seat row {row_text}")
        if row not in rows:
            raise ValueError(f"Invalid row number {row}")
        return letter, row


    def relocate_passageiro(self, from_seat, to_seat):
        """ mudar o ludar do passageiro que ja tem reserva"""

        from_letter, from_row = self._parse_seat(from_seat)
        if self._seating[from_row][from_letter] is None:
            raise ValueError(f"lugar from_seat nao está reservado a ninguem!")

        to_letter, to_row = self._parse_seat(to_seat)
        if self._seating[to_row][to_letter] is not None:
            raise ValueError(f"O lugar já está ocupado!!! nao se pode mudar para ká")

        self._seating[to_row][to_letter] = self._seating[from_row][from_letter]
        self._seating[from_row][from_letter] = None

    def num_available_seats(self):
        return sum( sum (1 for s in row.values() if s is None) for row in self._seating if row is not None)

    def make_boarding_cards(self,card_printer):
        for passageiro, cadeira in sorted (self._passenger_seats()):
            card_printer(passageiro, cadeira, self.number(), self.aircraft_model())

    def _passenger_seats(self):
        """ um gerador sobre o seatingplan() que devole tuplo passageiro,lugar"""
        row_numbers, seat_letters = self._aircraft.seating_plan()
        for row in row_numbers:
            for letter in seat_letters:
                passenger = self._seating[row][letter]
                if passenger is not None:
                    yield (passenger, f"{row}{letter}")

class Aircraft:
    def __init__(self, registration, model, num_rows, num_seats_per_row):
        self._registration = registration
        self._model = model
        self._num_rows = num_rows
        self._num_seats_per_row = num_seats_per_row

    def registration(self):
        return self._registration

    def model(self):
        return self._model

    def seating_plan(self):
        return (range(1, self._num_rows + 1), "ABCDEFGHJK"[:self._num_seats_per_row])


###########################################################################################
####################### SECCAO FORA DAS CLASSES            ################################
###########################################################################################
def console_card_printer(passageiro, lugar, flight_num, aircraft):
    """ funcao que imprime 1 cartao de embarque de 1 passageiro num voo"""
    output =    f"| Name: {passageiro}"     \
                f"  Flight: {flight_num}"   \
                f"  Seat: {lugar}"           \
                f" Aircraft: {aircraft}"    \
                "  |"
    banner = "+" + "-" * (len(output) - 2) + "+"
    border = "|" + " " * (len(output) - 2) + "|"
    lines = [banner, border, output, border, banner]
    card = "\n".join(lines)
    print(card)
    print()

