from forex_python.converter import CurrencyRates
from forex_python.bitcoin import BtcConverter
from decimal import Decimal
from datetime import datetime


def isfloat(value):
    try:
        float(value)
        return True
    except ValueError:
        return False


cur = {'EUR', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HUF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AUD', 'CHF',
       'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'USD', 'NOK', 'RUB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR',
       'BTC', 'get_history'}
b = BtcConverter()
c = CurrencyRates()
datet = datetime.today()
history = list()


def print_history(his):
    if len(his) == 0:
        print("No history.")
    else:
        print("You did", len(his), "conversion:")
        for i in range(len(his)):
            print(i + 1, ":", his[i])
    return None


print("If you want bitcoin input BTC")
while True:
    result = str()
    while True:
        first = input("First currency, please: ")
        if first == 'get_history':
            print_history(history)
            break

        if first not in cur and first.upper() not in cur:
            print("I don't know what mean", first, ", one more time, please:")
        else:
            break
    if first == 'get_history':
        continue
    first = first.upper()

    while True:
        second = input("Second currency, please: ")
        if second == 'get_history':
            print_history(history)
            break
        if second not in cur and second.upper() not in cur:
            print("I don't know what mean", second , ", one more time, please:")
        else:
            break
    if second == 'get_history':
        continue
    second = second.upper()

    while True:
        amount = input("How much? ")
        if amount == 'get_history':
            print_history(history)
            break
        if isfloat(amount) and float(amount) < 0:
            print("Negative? Seriously?")
        elif not isfloat(amount):
            print("Oops", amount, "is not a digit, one more time")
        else:
            break
    if amount == 'get_history':
        continue

    dyw = input("Do you want to know the currency rates on a specific date? (y/n): ")
    if dyw == 'get_history':
        print_history(history)
        continue

    if dyw == "y" or dyw == "Y":
        year = int(input("Year, please: "))
        month = int(input("Month, please: "))
        day = int(input("Day, please: "))
        datet = datetime(year, month, day)
        dyw = dyw.lower()
    if first == 'BTC' or second == 'BTC':
        if first == 'BTC' and dyw == 'y':
            result = str(amount) + str(first) + " = " \
                     + str((float(amount) * float(b.get_previous_price(second, datet)))) + str(second) \
                     + " on " + str(datet)
            print(result)
        elif first == 'BTC' and dyw != 'y':
            result = str(amount) + str(first) + " = " + str(float(amount) * float(b.get_latest_price(second))) \
                     + str(second) + " on " + str(datetime.now())
            print(result)
        elif second == 'BTC' and dyw == 'y':
            result = str(amount) + str(first) + " = " + str(b.convert_to_btc_on(float(amount), first, datet)) \
                     + str(second) + " on " + str(datet)
            print(result)
        else:
            result = str(amount) + str(first) + " = " + str(b.convert_btc_to_cur(float(amount), first)) \
                     + str(second) + " on " + str(datetime.now())
            print(result)
    else:
        result = str(amount) + str(first) + " = " + str(c.convert(first, second, Decimal(amount), datet)) \
                 + str(second) + " on " + str(datet)
        print(result)
    history.append(result)
