monday_temperatures = [9.1, 8.8, 7.6]

for temperature in monday_temperatures:
    print(round(temperature))

print("Done")

for letter in 'hello':

    print(letter.title())
    print("Done")

def celsius_to_kelvin(cels):
    return cels + 273.15

monday_temperatures = [9.1, 8.8, -270.15]

for temperature in monday_temperatures:

    print(celsius_to_kelvin(temperature))

student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

for grades in student_grades.values():
    print(grades)

phone_numbers = {"John Smith": "+37682929928", "Marry Simpons": "+423998200919"}

for pair in phone_numbers.items():
    print("{} has a phone number {}".format(pair[0], pair[1]))

for key, value in phone_numbers.items():
    print("{} has a phone number {}".format(key, value))