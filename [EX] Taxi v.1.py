''' [EX] Taxi v.1 '''
def main():
    ''' Taxi Meter '''
    distance_in = int(input())
    time = int(input())
    price = 0
    distance = 0
    distance_in -= time
    print(price)
    while distance_in >= distance:
        if distance > 80:
            price += 8.50
        elif distance > 60:
            price += 7.50
        elif distance > 40:
            price += 6.50
        elif distance > 20:
            price += 6
        elif distance > 12:
            price += 5.50
        elif distance > 1:
            price += 5
        elif 0 <= distance <= 1:
            price += 35
        distance += 1
        print('++++', distance, price)
    print(price)

main()
