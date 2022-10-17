def number_of_bottles(bottles, exchange, total):
    print(bottles, exchange, total)
    if bottles<exchange:
        return total
    return number_of_bottles(bottles//exchange+bottles%exchange, exchange, total+bottles//exchange)

print(number_of_bottles(9,3,9))
print(number_of_bottles(15,4,15))