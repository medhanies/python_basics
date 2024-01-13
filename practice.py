# def weather_condition(temperature):
#     if temperature > 7:
#         return "Warm"
#     else:
#         return "Cold"

# user_input = float(input("Enter temperature: "))
# print(weather_condition(user_input))


from cmath import sqrt



players = [180, 172, 178, 185, 190, 195, 192, 200, 210, 190]

#calculate the mean
x = ((180 + 172 + 178 + 185 + 190 + 195 + 192 + 200 + 210 + 190) / 10)

print(x)

#calculate the variance
var = (((players[0] - x) ** 2) + ((players[1] - x) ** 2) + ((players[2] - x) ** 2) + ((players[3] - x) ** 2) + ((players[4] - x) ** 2) + ((players[5] - x) ** 2)
+ ((players[6] - x) ** 2) + ((players[7] - x) ** 2) + ((players[8] - x) ** 2) + ((players[9] - x) ** 2) / 10)

print(var)

#calcutate std. deviation
stand_dev = sqrt(var)

print(stand_dev)

a = x - stand_dev
b = x + stand_dev
#which heights fall within 1 std from the mean
for player in players:
    print(player)