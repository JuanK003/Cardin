from math import exp
import random
import time

def generate_credit_card():
    exp_date2 = str(random.randint(1, 12)).zfill(2)
    exp_date_year = random.randint(21, 26)
    card_number = "4387 89" + str(random.randint(10, 99)) + " " + str(random.randint(1000, 9999)) + " " + str(random.randint(1000, 9999))
    cvv = str(random.randint(100, 999))

    return f"{card_number} | {exp_date2}/{exp_date_year} | {cvv}"

nb_nitros = int(input("Por favor ingrese el número de tarjetas a producir =>  "))

print("Generación de la tarjeta de crédito....")
for _ in range(nb_nitros):
    card = generate_credit_card()

    with open('Codes.txt', "a+") as f:
        f.write(f"{card}\n")

    print(f"[GENERANDO] - {card}")
    time.sleep(0.025)
