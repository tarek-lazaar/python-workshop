
nb_apples = int(input("how many apples ? "))

unit = input("what unit ?")

if unit == "Kg" :
    weight = (1 / 5) * nb_apples
    print("Weight in Kg is :" , weight)

elif unit == "lbs":
    weight = (1 / 5) * nb_apples * 2.20
    print("Weight in lbs is :", weight)
else :
    print("please check the unit")





