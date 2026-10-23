import random

letters = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ''

while True:
    print("Укажите длину пароля:")
    lenght = int(input())
    for i in range(lenght):
        password += random.choice(letters)
    print(password)
    s = input("Сгенерировать новый? Если да, введите True, если нет - False ")
    if s == "False":
        break
