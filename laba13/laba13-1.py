def number_to_text(num):
    number_dict = {
        1: "один",
        2: "два",
        3: "три",
        4: "чотири",
        5: "п'ять",
        6: "шість",
        7: "сім",
        8: "вісім",
        9: "дев'ять",
        10: "десять"
    }

    return number_dict.get(num, "Число поза діапазоном")


user_input = int(input("Введіть число від 1 до 10: "))
print(number_to_text(user_input))
