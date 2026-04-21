def check_password(password):
    # Перевірка довжини
    if len(password) < 8:
        return False, "Пароль занадто короткий (мінімум 8 символів)"

    # Перевірка наявності цифр
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "Пароль повинен містити хоча б одну цифру"

    # Перевірка наявності букв
    has_letter = any(char.isalpha() for char in password)
    if not has_letter:
        return False, "Пароль повинен містити хоча б одну букву"

    return True, "Пароль надійний!"


# Введення пароля двічі
while True:
    password1 = input("Введіть пароль: ")
    password2 = input("Повторіть пароль: ")

    # Перевірка співпадіння
    if password1 != password2:
        print("Помилка: паролі не співпадають! Спробуйте ще раз.\n")
        continue

    # Перевірка критеріїв
    is_valid, message = check_password(password1)
    print(f"\nРезультат: {message}")
    break