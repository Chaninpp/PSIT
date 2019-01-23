''' BloodDonation '''
def main(age_temp, weight_temp, amount_temp):
    ''' for '''
    age = True if age_temp > 17 and age_temp <= 70 else False
    weight = True if weight_temp >= 45 else False
    amount = True if age_temp < 55 else False if amount_temp == 0 else True
    if (age_temp == 17 or age_temp >= 60) and age_temp <= 70:
        allow = input()
        age = True if allow == 'True' else False
    print('Yes' if age and weight and amount else 'No')

main(int(input()), int(input()), int(input()))
