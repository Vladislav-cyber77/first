def register():
    print('Добро пожаловать в GITHUB!')
    print('Что бы зарегестрироваться введите:')
    name = input('Имя:')
    if name == name.upper():
        print('Имя не может состоять из всех заглавных букв')
        return
    if not name:
        print('Имя не может быть пустым')
        return
    if ' ' in name:
        print('В имени не может быть пробелов')
        return
    if any(digit in name for digit in '0123456789'):
        print('Имя не может содержать чисел')
        return
    if not name[0].isupper():
        print('Имя должно начинаться с заглавной Буквы')
        return
    password =input('Пароль:')
    if password.count('')==0 or password.count('.')==0:
        print("Пароль должен содержать '' или '.'")
        return
    if not any(numbers in password for numbers in '0123456789'):
        print('Пароль должен содержать хотя бы одну цифру')
        return
    age_input = input('Возраст: ')
    if not age_input.isdigit():
        print('Возраст должен быть числом!')
        return
    age = int(age_input)
    if age < 18:
        print('Вы еще слишком молоды.Регистрация только с 18 лет')
        return
    print('Добро пожаловать в систему,'+ name +'!')
register()