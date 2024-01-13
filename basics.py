day_hours = 24
week_days = 7

week_hours = day_hours * week_days

print(week_hours)

x = 10
y = "10"
z = 10.1

sum1 = x + x
sum2 = y + y

print(sum1, sum2)
print(type(x), type(y), type(z))

monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {"Marry": 9.1, "Sim": 8.8, "John": 7.5}

mysum = sum(student_grades.values())
length = len(student_grades)
mean = mysum / length
print(mean)

monday_temperatures = ["hello", 1, 2, 3]

def mean(mylist):
    the_mean = sum(mylist) / len(mylist)
    return the_mean
print(mean([1, 4, 6]))

def mean(value):
    if type(value) == dict:
        the_mean = sum(value.values()) / len(value.keys())
    else:
        the_mean = sum(value) / len(value)

    return the_mean

monday_temperatures = [9.1, 8.8, 7.5]
student_grades = {"Marry": 9.1, "Sim": 8.10, "John": 7.5}
print(mean(student_grades))

