str_kg = input("Please enter the number of kilograms you wish to convert: ")
total_kg = float(str_kg)

ounces = total_kg * 35.2739619495804106 

total_pound = int(ounces) // 16

total_ounce = ounces % 16

print(total_kg, "kilograms is", total_pound, "pounds and", total_ounce, "ounces.")
