from decimal import Decimal

TWOPLACES = Decimal("1.00")


def method_drawdown(pot):  # draws 5% out of pot, has been replaced by user input
    new_pot = pot * Decimal(95) / 100
    new_pot_rounded = new_pot.quantize(TWOPLACES)
    return new_pot_rounded


def method_growth(pot):
    new_pot = pot + (pot * Decimal(3.3) / 100)
    new_pot_rounded = new_pot.quantize(TWOPLACES)
    return new_pot_rounded


#############


def change_rate(rate, coeff):
    return rate * coeff
