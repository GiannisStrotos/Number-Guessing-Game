secret_number = 4
guess = 0
attempts = 0 
while guess !=secret_number:
    guess = int(input("Μαντεψε εναν αριθμό(1-10)"))
    if guess < secret_number:
        print("Πιο μεγάλος αριθμός!")
        attempts=attempts+1
    elif guess > secret_number:
        print("Πιο μικρός αριθμός!")
        attempts=attempts+1
    else:
        print("Μπράβο το βρήκες")
        attempts=attempts+1

        print("Έκανες συνολικά",attempts,"προσπάθειες")
