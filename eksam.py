# Esimene ülesanne

name = input("Nimi: ")
height_cm = float(input("Pikkus cm: "))
height_m = height_cm / 100
print(name + " on " + str(height_m), "m")

# Teine ülesanne

temp = 45

if temp < 0:
    print("Liiga külm")
elif temp > 30:
    print("Liiga palav")
else:
    print("Paras")

# Kolmas ülesanne

fruits = ["Õun", "Pirn", "PLOOM", "kirSS"]
print(fruits[1])
fruits[-1] = "murel"
fruits.append("banaan")
print(len(fruits))
print(fruits)

# Neljas ülesanne

for f in fruits:
    print(f.lower())
    