voltorb = int(input("Qual o level do Voltorb? "))


if voltorb > 1 and voltorb <= 20:
    level = 20 * (voltorb)**3

elif voltorb >= 21 and voltorb <= 40:
    level = 8000 + (voltorb -10)**2

elif voltorb >= 41 and voltorb <= 60:
    level = 9000 + 5*voltorb

elif voltorb >= 61 and voltorb <= 80:
    level = 9300 + 2*voltorb

else:
    level = 9500 + voltorb

print("O nível do seu choque é de ", level, "W.")