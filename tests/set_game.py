import random

NUMBERS = [1, 2, 3]
SYMBOLS = ["DIAMOND", "SQUIGGLE", "OVAL"]
SHADINGS = ["STRIPPED", "SOLID", "OPEN"]
COLORS = ["RED", "GREEN", "PURPLE"]

class Card:
    def __init__(self, number, symbol, shading, color):
        if any([
            number not in NUMBERS,
            symbol not in SYMBOLS,
            shading not in SHADINGS,
            color not in COLORS
        ]):
            raise ValueError("Неправильные параметры карты")

        self.number = number
        self.symbol = symbol
        self.shading = shading
        self.color = color
    def __str__(self):
        return (str(self.number)+" "+ self.symbol+" "+ self.shading +" "+ self.color)

def check_set(cards):
    result = True
    if len(cards)!=3:
        return False
    if not check_numbers(cards):
        return False
    if not check_symbols(cards):
        return False
    if not check_shadings(cards):
        return False
    if not check_colors(cards):
        return False
    return result

def check_numbers(cards):
    result = False
    numbers = []
    for card in cards:
        numbers.append(card.number)
    if numbers.count(numbers[0])==3:
        result = True
    elif len(set(numbers))==3:
        result = True
    else:
        pass
    return result

def check_symbols(cards):
    result = False
    numbers = []
    for card in cards:
        numbers.append(card.symbol)
    if numbers.count(numbers[0])==3:
        result = True
    elif len(set(numbers))==3:
        result = True
    else:
        pass
    return result

def check_shadings(cards):
    result = False
    numbers = []
    for card in cards:
        numbers.append(card.shading)
    if numbers.count(numbers[0])==3:
        result = True
    elif len(set(numbers))==3:
        result = True
    else:
        pass
    return result

def check_colors(cards):
    result = False
    numbers = []
    for card in cards:
        numbers.append(card.color)
    if numbers.count(numbers[0])==3:
        result = True
    elif len(set(numbers))==3:
        result = True
    else:
        pass
    return result

def generate_set():
    result = []
    for i in range(3):
        result.append(Card(
        NUMBERS[random.randint(0,2)],
        SYMBOLS[random.randint(0,2)],
        SHADINGS[random.randint(0,2)],
        COLORS[random.randint(0,2)]))
    return result


# false_set=generate_set()
# for card in false_set:
#     print (card)
# print (check_set(false_set))

def generate_win_set():
    i = True
    while i:
        k = generate_set()
        if check_set(k):
            for card in k:
                print(card)
            i = False

# generate_win_set()
