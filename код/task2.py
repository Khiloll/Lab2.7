# Решите задачу: определите общие символы
# в двух строках, введенных с клавиатуры.


if __name__ == "__main__":
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")

    set1 = set(string1)
    set2 = set(string2)

    common_characters = set1.intersection(set2)

    print("Общие символы:", common_characters)