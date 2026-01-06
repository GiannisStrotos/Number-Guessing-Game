#print(name.capitalize())
#print(name.replace("i","o"))

#name = input("Πώς σε λένε?")
#print("Γειά σου",name)
#name2 = input("τι κάνεις")
#print("Χαίρομαι",name)

#name = input("Όνομα")
#birth = int(input("Έτος γέννησης")) 
#age = 2026 - birth
#print("είσαι ο",name,"γεννήθηκες το",birth,"και είσαι",age,"ετών")

#age = int(input("πόσο χρονών είσαι?"))
#if age<13:
    #print("Είσαι παιδί")
#elif 13<=age<=19:
    #print("Είσαι έφηβος")
#elif age>=20:
    #print("Είσαι ενήλικας")


#number = int(input("Πες μου εναν αριθμο"))
#for i in range(number):
    #print(i)
#if i/2== 0:
    #print("ζυγός")
#else:
    #print("περιττός")



#def calculate_age(year_of_birth):
    #age = 2026-year_of_birth
    #return age 
#year = int(input("ετος γεννησης?"))
#age = calculate_age(year)
#print("εισαι",age)


#friends = ["βασιλης","γιαννης",]
#ages = (18,17)
#for i in range(3):
    #name = input("Ονομα φιλου")
    #age = int(input("ηλικια φιλου"))
    #friends.append(name)
    #print(name,"",age)


        
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